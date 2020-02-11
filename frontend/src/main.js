import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import jQuery from 'jquery'
import VueAxios from "vue-axios";
import axios from 'axios';
import '@/assets/css/tailwind.css'
import SimpleVueValidation from 'simple-vue-validator';
import i18n from "./plugins/i18n";
import VueSlickCarousel from 'vue-slick-carousel'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import VueDragscroll from 'vue-dragscroll'

Vue.use(VueDragscroll)
Vue.use(ElementUI);

window.$ = window.jQuery = jQuery;
import 'popper.js'
import 'bootstrap'
import VueSession from "vue-session/index.esm";
import './assets/app.scss'

Vue.use(VueSession)
Vue.use(VueAxios, axios)
Vue.use(SimpleVueValidation);
Vue.use(VueSlickCarousel)

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false

export const Validator = SimpleVueValidation.Validator; // define validator lib

new Vue({
    router,
    store,
    SimpleVueValidation,
    i18n,
    render: h => h(App)
}).$mount('#app')
