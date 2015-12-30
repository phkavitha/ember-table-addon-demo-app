import Ember from 'ember';
import TableFeatures from '../mixins/features';
import TreeDataGridMixin from '../mixins/tree-data-grid';

export default Ember.Controller.extend(TableFeatures, TreeDataGridMixin, {
  tableContent: [],
  title: "Tree Data",
  features: [
    {
      name: 'Lazy Loading',
      icon: 'fa-flash',
      description: 'This allows you to partially load table data from the server based on what is being displayed in the table'
    },
    {
      name: 'Column Group',
      icon: 'fa-arrows-v',
      description: 'Excel like column groups enable you to make larger tables more readable.'
    },
    {
      name: 'Sort',
      icon: 'fa-sort',
      description: 'Built in sorting with no extra code required'
    }
  ]
});
