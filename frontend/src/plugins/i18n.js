//i18n.js
import Vue from 'vue'
import VueI18n from 'vue-i18n'
import en from '../languages/en.json'
import th from '../languages/th.json'
Vue.use(VueI18n)
const messages = {
  'en': en,
  'th': th
}
const i18n = new VueI18n({
  locale: 'en', // set locale
  fallbackLocale: 'th', // set fallback locale
  messages //set locale messages
})
export default i18n