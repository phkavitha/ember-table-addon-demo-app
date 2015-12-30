import Ember from 'ember';

export default Ember.Mixin.create({
  _tables: [{
    name: "Array Data",
    description: "This is a faster experience for the end user because of lazy loading.",
    link: "arrayData"
  }, {
    name: "Tree Data",
    description: "Sort group data by groupers and columns",
    link: "treeData"
  }, {
    name: "Style Customization",
    description: 'Change the look and feel of your table',
    link: "styleCustomization"
  }],

  tables: Ember.computed.filter('_tables', function (table, index) {
    var newTable = Ember.copy(table);
    newTable.labelClass = this.get('title') === table.name ? 'active' : '';
    var delay = index > 4 ? 0 : (4 - index) * 100;
    Ember.set(newTable, 'delay', delay);
    return newTable;
  })
});
