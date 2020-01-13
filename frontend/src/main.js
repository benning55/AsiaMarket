import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import jQuery from  'jquery'
import VueAxios from "vue-axios";
import axios from 'axios';

window.$ = window.jQuery = jQuery;
import 'popper.js'
import 'bootstrap'
import VueSession from "vue-session/index.esm";
import  './assets/app.scss'

Vue.use(VueSession)
Vue.use(VueAxios, axios)

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
