import Ember from 'ember';
import ColumnDefinition from 'ember-table/models/column-definition';

export default Ember.Controller.extend({

  columns: function () {
    var rowNumberColumn, activityColumn, statusColumn;
    rowNumberColumn = ColumnDefinition.create({
      columnWidth: 20,
      textAlign: 'text-align-left',
      headerCellName: 'No.',
      getCellContent: function(row) {
        return row.get('rowNumber');
      }
    });

    activityColumn = ColumnDefinition.create({
      columnWidth: 150,
      textAlign: 'text-align-left',
      headerCellName: 'Activity',
      getCellContent: function (row) {
        return row.get('activity');
      }
    });
    statusColumn = ColumnDefinition.create({
      columnWidth: 100,
      headerCellName: 'status',
      getCellContent: function (row) {
        return row.get('status');
      }
    });

    return [rowNumberColumn, activityColumn, statusColumn];
  }.property(),

  tableContent: function () {
    var generatedContent = this.get('model');
    return generatedContent;
  }.property(),

  numRows: Ember.computed('tableContent', function() {
    return this.get('tableContent').length;
  })
});