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
            host: `http://${window.location.hostname}:8000`,
            obtainJWT: `http://${window.location.hostname}:8000/auth/obtain_token/`,
            refreshJWT: `http://${window.location.hostname}:8000/auth/refresh_token/`,
            baseUrL: `http://${window.location.hostname}:8000/api/accounts/`,
            registerUrL: `http://${window.location.hostname}:8000/api/accounts/register/`,
            productUrL: `http://${window.location.hostname}:8000/api/products/product/`,
            recommendProduct: `http://${window.location.hostname}:8000/api/products/recommend/`,
            newestProduct: `http://${window.location.hostname}:8000/api/products/new/`,
            forgotPasswordUrL: `http://${window.location.hostname}:8000/api/accounts/forget-password/`,
            editInCart: `http://${window.location.hostname}:8000/api/products/cart-detail/`,
            addressUrL: `http://${window.location.hostname}:8000/api/accounts/user/address/`
        },
        inCart: {
            cart_detail: []
        },
        userAddress: []
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
            state.inCart = {
                cart_detail: []
            }
        },
        setIncart(state, incart) {
            state.inCart = incart
        },
        setUserAddress(state, address) {
            state.userAddress = address
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
