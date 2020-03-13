import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        authUser: {},
        isAuthenticated: false,
        jwt: localStorage.getItem('token'),
        endpoints: {
            host: `https://${window.location.hostname}`,
            obtainJWT: `https://${window.location.hostname}/auth/obtain_token/`,
            refreshJWT: `https://${window.location.hostname}/auth/refresh_token/`,
            baseUrL: `https://${window.location.hostname}/api/accounts/`,
            registerUrL: `https://${window.location.hostname}/api/accounts/register/`,
            productUrL: `https://${window.location.hostname}/api/products/product/`,
            recommendProduct: `https://${window.location.hostname}/api/products/recommend/`,
            newestProduct: `https://${window.location.hostname}/api/products/new/`,
            forgotPasswordUrL: `https://${window.location.hostname}/api/accounts/forget-password/`,
            editInCart: `https://${window.location.hostname}/api/products/cart-detail/`,
            addressUrL: `https://${window.location.hostname}/api/accounts/user/address/`,
            cartAPI: `https://${window.location.hostname}/api/products/cart/`
        },
        inCart: {
            cart_detail: []
        },
        userAddress: [],
        indexUserAddress:0,
        allOrder:[]
    },
    mutations: {
        setAuth(state, isAuthenticated) {
            Vue.set(state, 'isAuthenticated', isAuthenticated)
        },
        setAuthUser(state, {
            authUser,
            isAuthenticated
        }) {
            Vue.set(state, 'authUser', authUser)
            Vue.set(state, 'isAuthenticated', isAuthenticated)
        },
        updateToken(state, newToken) {
            localStorage.setItem('token', newToken)
            state.jwt = newToken;
        },
        removeToken(state) {
            localStorage.removeItem('token')
            state.authUser = null
            state.jwt = null
            state.isAuthenticated = false
            state.indexUserAddress = 0
            state.inCart = {
                cart_detail: []
            }
        },
        setIncart(state, incart) {
            state.inCart = incart
        },
        setUserAddress(state, address) {
            state.userAddress = address
        },
        setNewFirstname(state,firstname){
            state.authUser.user.first_name = firstname
        },
        setNewLastname(state,lastname){
            state.authUser.user.last_name = lastname
        },
        setNewTel(state,tel){
            state.authUser.profile.tel = tel
        },
        setNewDOB(state,dob){
            state.authUser.profile.dob = dob
        },
        setIndexUserAddress(state,index){
            state.indexUserAddress = index
        },
        setAllOrder(state,allOrder){
            state.allOrder = allOrder
        }
    },
    getters: {
        getCount(state) {
            return state.inCart.cart_detail
        }
    },
    actions: {},
    modules: {},
    plugins: [new VuexPersistence().plugin]
})
