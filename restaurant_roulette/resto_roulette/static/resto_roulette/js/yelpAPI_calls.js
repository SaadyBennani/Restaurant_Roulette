const proxy = 'https://cors-anywhere.herokuapp.com/'
const api_key = 'Hmh3X44EOndrwanfrC5AdftCTWwD4TrvIO7xkS3WfE4XejMYUY0DsGiBM6WRV6K5HhdjjIsIa12XWGSlC1InJQSHS_F-jO03c_jxgREbESESKaqDXwc-8CZ-tbbHXHYx'
const site_root = 'http://127.0.0.1:8000/'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

Vue.component('card', {
  props: [
    'business',
    'address',
    'stars',
    'url',
    'id',
  ],
  template: `
  <div class="col-md-4">
      <div class="card border-danger text-center" id="featured_cards">
      <img class="card-img-top " v-bind:src="business.image_url"/>
      <div class="card-body">
        <h4>{{business.name}}</h4>
        </div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item">{{address}}</li>
          <li class="list-group-item">{{business.display_phone}}</li>
          <li class="list-group-item">
            <img v-bind:src='stars'></img>
          </li>
          <li class="list-group-item">
          <div class="form-check">
<input class="form-check-input" type="checkbox" value="" v-bind:id="id">
<label class="form-check-label" v-bind:for="id">
  Add to Queue
</label>
</div>
          </li>
          </ul>
          <div class="card-body links">
          <a v-bind:href="business.url" class="card-link"><img class="card-link"src="static/assets/yelp_fullcolor.png"></a>
    </div>
  `
})

const app = new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    business: null,
    info: null,
    loading: true,
    errored: false,
    what: '',
    where: '',
    queued: false,
    queue: [],
    endpoint: proxy + 'https://api.yelp.com/v3/businesses/search',
    headers: {'Authorization': `bearer ${api_key}`},
  },
  methods: {
    addToQueue: function() {
      this.queue = this.info.filter((business) => {
        const id = business.id
        return document.getElementById(id).checked===true
      })

    },
    redirectToQueue: function() {
      this.addToQueue()
      axios
        .post(site_root+'add_queue', {
            'biz_queue': this.queue
        })
        .then(response => {
          console.log(this.queue);
          console.log(eval(response));

          window.location.href=site_root+'queue';

        })
        .catch(function (error) {
    console.log(error);
  })
    },
    getBusinesses: function() {
      axios
      .get(this.endpoint, {
        params: {
          'term': this.what,
          'location': this.where,
          'limit': 6,
          'radius': 10000,
        },
        headers: this.headers
      })
      .then(response => {
        this.info = response.data.businesses
      })
    },
    getStarRating: function(rating) {
      const stars = {
        0: 'regular_0',
        1.5: 'regular_1_half',
        2: 'regular_2',
        2.5: 'regular_2',
        3: 'regular_3',
        3.5: 'regular_3_half',
        4: 'regular_4',
        4.5: 'regular_4_half',
        5: 'regular_5',

      }
      return `../../static/assets/${stars[rating]}.png/`
    },
    parseAddress: function(display_address) {
      const address = display_address.join(', ')
      return address
    }
  },

  mounted: function() {
    this.what = what
    this.where = where
    this.getBusinesses()
  }
});
