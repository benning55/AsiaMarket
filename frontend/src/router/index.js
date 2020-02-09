import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import HomePage from "../views/HomePage";
import Detail from "../views/Detail";
import CategoryView from "../views/CategoryView";
import ViewProfile from "../views/ViewProfile";
import ViewAddress from "../views/ViewAddress";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/Register')
  },
  {
    path: '/category=:id',
    name: 'Category',
    component: CategoryView
  },
  {
    path:'/detail',
    name:'detail',
    component:Detail
  },
  {
    path:'/profile',
    name:'ViewProfile',
    component:ViewProfile
  },
  {
    path:'/address',
    name:'ViewAddress',
    component:ViewAddress
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
