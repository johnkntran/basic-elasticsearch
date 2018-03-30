var vm = new Vue({
  el: '#app',
  data: {
    appName: 'Elastic',
    query: '',
    quotes: [],
  },
  watch: {
    query() {
        this.executeSearch();
    }
  },
  created() {
    $.getJSON('../data/data.json')
      .done(data => {
        this.quotes = data.slice(0, 10);
    });
  },
  methods: {
    executeSearch() {
      // Replace this with search endpoint from Elastic
      this.appName = (this.appName == 'Elastic') ? 'ElasticSearch' : 'Elastic';
    }
  }
})
