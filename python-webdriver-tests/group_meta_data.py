import re
from sort_condition_provider import SortConditionProvider

class GroupMetadata:
    def __init__(self, zipped_row):
        self.levels = []
        self.column_value_prefixes = zipped_row.copy()
        self.parse_meta_str(self.column_value_prefixes.pop("groupName"))

    def make_group_rows(self):
        first_group_level = self.get_group_level(0)
        normal_order_rows = first_group_level.expand_this_level(VirtualTopRow(), None)
        # asc_rows = first_group_level.expand_this_level(VirtualTopRow(), 'asc')
        # desc_rows = first_group_level.expand_this_level(VirtualTopRow(), 'desc')
        return normal_order_rows

    def parse_meta_str(self, pattern_str):
        levels = pattern_str.split('-')
        for l in levels:
            level_name, id_range = self.analysis_value(l)
            self.levels.append((level_name, id_range))

    def get_group_names(self):
        return [level[0] for level in self.levels]

    def get_group_level(self, level_index):
        level = self.levels[level_index]
        if level_index == len(self.levels) - 1:
            return LastGroupLevel(level[0], level[1], self, level_index)
        return GroupLevel(level[0], level[1], self, level_index)

    def get_column_value_prefixes(self):
        return self.column_value_prefixes

    def analysis_value(self, value):
        search = re.search('(.+?)\[([\d|,]+)\]', value)
        level_name = search.group(1)
        val = search.group(2)
        values = range(1, int(val) + 1) if val.isalnum() else [int(i) for i in val.split(',')]
        return level_name, values

class GroupLevel:
    def __init__(self, level_name, id_range, group_metadata, level_index):
        self.level_name = level_name
        self.id_range = id_range
        self.group_metadata = group_metadata
        self.level_index = level_index

    def expand_this_level(self, parent_row, sort_direction=None):
        result = []
        id_range = self.make_id_range(sort_direction)
        rows = [GroupRow(self, parent_row, index) for index, x in enumerate(id_range)]
        query = parent_row.get_query()
        rows_values = [row.make_row_values() for row in rows]
        result.append({"query": query, "body": rows_values})

        children_results = self.expand_next_level(rows, sort_direction)
        result = sum(children_results, result)
        return result

    def expand_next_level(self, rows, sort_direction):
        next_group_level = self.next_group_level()
        return [next_group_level.expand_this_level(row, sort_direction) for row in rows]

    def make_id_range(self, sort_direction=None):
        return self.id_range

    def next_group_level(self):
        return self.group_metadata.get_group_level(self.level_index + 1)

    def get_query(self, group_name):
        return {self.level_name:  group_name}

    def make_column_values(self, path, index=None):
        prefixes = self.group_metadata.get_column_value_prefixes()
        result = {}
        for key in prefixes:
            prefix = self.get_prefix(prefixes[key])
            value = self.handle_prefixes(prefixes[key], index)
            local_path = path[:]
            local_path.append(value)
            if(prefix):
                result[key] = prefix + '-'.join([str(i) for i in local_path])
            else:
                result[key] = reduce(lambda res, i: res*100 + i, local_path, 0)
        result[self.level_name] = result["id"]
        return result

    def handle_prefixes(self, key, index):
        return index

    def get_prefix(self, value):
        search = re.match('^(.*?)(\[|$)', value)
        return search.group(1) if search else None


class LastGroupLevel(GroupLevel):

    def column_names(self):
        return self.group_metadata.column_value_prefixes.keys()

    def expand_this_level(self, parent_row, sort_direction=None):
        result = []
        id_range = self.make_id_range(sort_direction)
        rows = [GroupRow(self, parent_row, index) for index, x in enumerate(id_range)]
        query = parent_row.get_query()
        rows_values = [row.make_row_values() for row in rows]
        result.append({"query": query, "body": rows_values})
        children_results = self.expand_next_level(rows, sort_direction)
        result = sum(children_results, result)
        sortColumns = ["id", "beginningDr", "beginningCr", "netBeginning"]
        provider = SortConditionProvider(list(set(sortColumns) & set(self.column_names())))
        sort_criteria_arr = provider.filterBy(
            "id/asc", "id/desc",
            "beginningDr/asc", "beginningDr/desc",
            "beginningCr/asc",
            "beginningDr/asc beginningCr/asc",
            "beginningDr/desc beginningCr/asc",
            "beginningCr/asc netBeginning/asc",
            "beginningDr/asc beginningCr/asc netBeginning/asc"
        )
        for sort_criteria in sort_criteria_arr:
            localQuery = query.copy()
            data = sort_criteria.sort(rows_values[:])
            localQuery.update(sort_criteria.to_query())
            result.append({"query": localQuery, "body": data})
            result = sum(children_results, result)
        return result


    def expand_next_level(self, rows, sort_direction):
        return []

    def make_id_range(self, sort_direction=None):
        id_range = self.id_range[:]
        if sort_direction == 'desc':
            id_range.sort(reverse=True)
        elif sort_direction == 'asc':
            id_range.sort()
        return id_range

    def handle_prefixes(self, key, index):
        res = re.search('\[(.*?)\]', key)
        if(res):
            val = res.group(1)
            values = range(1, int(val) + 1) if val.isalnum() else [int(i) for i in val.split(',')]
            return values[index - 1]
        else:
            return index

    def next_group_level(self):
        return None

    def get_query(self, group_name):
        return {}


class GroupRow:
    def __init__(self, group_level, parent_row, index):
        self.index = index + 1
        self.group_level = group_level
        self.parent_row = parent_row

    def get_query(self):
        result = {}
        value = reduce(lambda res, i: res * 100 + i, self.get_path(), 0)
        result.update(self.group_level.get_query(value))
        result.update(self.parent_row.get_query())

        return result

    def get_path(self):
        path = self.parent_row.get_path()
        path.append(self.index)
        return path

    def make_row_values(self):
        result = self.group_level.make_column_values(self.parent_row.get_path(), self.index)
        result.update(self.get_query())
        return result


class VirtualTopRow(GroupRow):
    def __init__(self):
        "mock group row"

    def concat_child_group_name(self, child_name):
        return child_name

    def get_query(self):
        return {}

    def make_row_values(self):
        return {}

    def get_path(self):
        return []
