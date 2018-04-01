const vm = new Vue({
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
    $.getJSON('../api/search_famous_quotes.py')
      .done(data => {
        let hits = data.hits.hits.slice(0, 10);
        let qts = hits.map(hit => hit._source);
        this.quotes = qts;
    });
  },
  methods: {
    executeSearch() {

      $.post("../api/search_famous_quotes.py", `{"q":"${this.query}"}`)
        .done(data => {
          let hits = data.hits.hits.slice(0, 10);
          let qts = hits.map(hit => hit._source);
          this.quotes = qts;
        });

      /*
      $.getJSON('')
        .done(data => {
          let hits = data.hits.hits.slice(0, 10);
          let qts = hits.map(hit => hit._source);
          this.quotes = qts;
      });
      */
    }
  }
});
