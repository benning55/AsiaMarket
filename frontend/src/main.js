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
import './assets/css/element-variables.scss'

// import locale from 'element-ui/lib/locale/lang/th'
import enLocale from 'element-ui/lib/locale/lang/en'
import ElementLocale from 'element-ui/lib/locale'

import VueDragscroll from 'vue-dragscroll'
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.css'
import 'popper.js'
import 'bootstrap'
import VueSession from "vue-session/index.esm";
import './assets/app.scss'
import ImageUploader from 'vue-image-upload-resize'
import VueLazyload from 'vue-lazyload'

ElementLocale.i18n((key, value) => i18n.t(key, value))

Vue.use(ImageUploader);

Vue.use(VueLazyload, {
  preLoad: 10.3,
  error: './assets/icon/Rolling-1s-44px.svg',
  loading: 'public/favicon.ico',
  attempt: 1
})


Vue.use(VueAwesomeSwiper, /* { default global options } */)

Vue.use(VueDragscroll)
Vue.use(ElementUI, );

window.$ = window.jQuery = jQuery;

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
