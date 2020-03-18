//i18n.js
import Vue from 'vue'
import VueI18n from 'vue-i18n'
import en from '../languages/en.json'
import th from '../languages/th.json'
import enLocale from 'element-ui/lib/locale/lang/en'
import thLocale from 'element-ui/lib/locale/lang/th'
import ElementLocale from 'element-ui/lib/locale'

Vue.use(VueI18n)

let e = en;
let d = {...enLocale}
e.el = d.el

let t = th;
let dd = {...thLocale}
t.el = dd.el


const messages = {
    'en': e,
    'th': t,
}

console.log(localStorage.getItem("setLocalLanguage"))

const i18n = new VueI18n({

    locale: localStorage.getItem("setLocalLanguage") === null ? "en" : localStorage.getItem("setLocalLanguage"), // set locale
    fallbackLocale: 'th', // set fallback locale
    messages //set locale messages
})

ElementLocale.i18n((key, value) => i18n.t(key, value))

export default i18n