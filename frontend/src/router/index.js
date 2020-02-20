import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import HomePage from "../views/HomePage";
import Detail from "../views/Detail";
import CategoryView from "../views/CategoryView";
import ViewProfile from "../views/ViewProfile";
import ViewAddress from "../views/ViewAddress";
import ForgetPassword from "../views/ForgetPassword";
import AddAddress from "../views/AddAddress";
import EditAddress from "../views/EditAddress";
import ConfirmOrder from "../views/ConfirmOrder";
import SelectPayment from "../views/SelectPayment";
import ViewOrderHistory from "../views/ViewOrderHistory";

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
        path: '/detail=:id',
        name: 'Detail',
        component: Detail
    },
    {
        path: '/profile',
        name: 'ViewProfile',
        component: ViewProfile
    },
    {
        path: '/address',
        name: 'ViewAddress',
        component: ViewAddress
    },
    {
        path: '/forget-password',
        name: 'ForgetPassword',
        component: ForgetPassword
    },
    {
        path: '/address/add',
        name: 'AddAddress',
        component: AddAddress
    },
    {
        path: '/address/edit@:id',
        name: 'EditAddress',
        component: EditAddress
    },
    {
        path: '/confirm-order',
        name: 'ConfirmOrder',
        component: ConfirmOrder
    },
    {
        path: '/select-payment/:id',
        name: 'SelectPayment',
        component: SelectPayment
    },
    {
        path:'/orders',
        name:'ViewOrderHistory',
        component: ViewOrderHistory
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
