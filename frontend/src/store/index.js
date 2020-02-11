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
      obtainJWT: 'http://localhost:8000/auth/obtain_token/',
      refreshJWT: 'http://localhost:8000/auth/refresh_token/',
      baseUrL: 'http://localhost:8000/api/accounts/',
      registerUrL: 'http://localhost:8000/api/accounts/register/',
      productUrL: 'http://localhost:8000/api/products/product/',
      recommendProduct:'http://localhost:8000/api/products/recommend/',
      newestProduct:'http://localhost:8000/api/products/new/'
    }
  },
  mutations: {
    setAuth(state, isAuthenticated){
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    setAuthUser(state, {authUser,
        isAuthenticated
    }) {
      Vue.set(state, 'authUser', authUser)
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    updateToken(state, newToken){
      localStorage.setItem('token', newToken)
      state.jwt = newToken;
    },
    removeToken(state) {
      localStorage.removeItem('token')
      state.authUser = null
      state.jwt = null
      state.isAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  },
  plugins: [new VuexPersistence().plugin]
})
