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
          </ul>
          <div class="card-body links">
          <a v-bind:href="business.url" class="card-link"><img class="card-link"src="static/assets/yelp_fullcolor.png"></a>
    </div>

  `
})

Vue.component('randcard', {
  props: [
    'randomBiz',
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
          </ul>
          <div class="card-body links">
          <a v-bind:href="business.url" class="card-link"><img class="card-link"src="static/assets/yelp_fullcolor.png"></a>
    </div>

  `
})

const app2 = new Vue({
  el: '#app2',
  delimiters: ['[[',']]'],
  data: {
    randomBiz: null,
    business: null,
    info: null,
    loading: true,
    errored: false,
    what: '',
    where: '',
    queued: false,
    queue: null,
    test:[]
  },
  methods: {
    randomResto: function() {
      this.randomBiz = this.queue[Math.floor(Math.random()*app2.queue.length)]
      return console.log('sucess')
    },
    parseAddress: function(display_address) {
      const address = display_address.join(', ')
      return address
    },
    getQueue: function() {
    axios.get(site_root+'add_queue')
    .then(response => {
      this.queue = JSON.parse(response.data)
      console.log(this.queue)
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
  // parseAddress: function(display_address) {
  //   const address = display_address.join(', ')
  //   return address
  // }
},

  mounted: function() {
    this.getQueue()

  }
});
