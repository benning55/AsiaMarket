import Vue from 'vue'
import VueRouter from 'vue-router'

const HomePage = () => import('../views/HomePage')
const Login = () => import('../views/Login')
const Register = () => import('../views/Register')
// import HomePage from "../views/HomePage";
const Detail = () => import("../views/Detail");
const CategoryView = () => import("../views/CategoryView");
const ViewProfile = () => import("../views/ViewProfile");
const ViewAddress = () => import("../views/ViewAddress");
const ForgetPassword = () => import("../views/ForgetPassword");
const AddAddress = () => import("../views/AddAddress");
const EditAddress = () => import("../views/EditAddress");
const ConfirmOrder = () => import("../views/ConfirmOrder");
// import SelectPayment from "../views/SelectPayment";
const ViewOrderHistory = () => import("../views/ViewOrderHistory");
const ViewEachOrder = () => import("../views/ViewEachOrder");
const PageNotFound = () => import("../views/PageNotFound");
const Help_01 = () => import("../views/Help_01")
const Help_02 = () => import("../views/Help_02")
const Help_03 = () => import("../views/Help_03")
const SearchView = () => import('../views/SearchView')


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage,
        meta: {
            title: 'ThaiMarket Express'
        }
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/register',
        name: 'register',
        component: Register
    },
    {
        path: '/category=:id',
        name: 'Category',
        component: CategoryView
    },
    {
        path: '/search=:id',
        name: 'SearchView',
        component: SearchView
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
        path: '/orders',
        name: 'ViewOrderHistory',
        component: ViewOrderHistory
    },
    {
        path: '/orders/:id',
        name: 'ViewEachOrder',
        component: ViewEachOrder
    },
    {
        path: "*",
        component: PageNotFound
    },
    {
        path: "/help-01",
        name: "Help01",
        component: Help_01
    },
    {
        path: "/help-02",
        name: "Help02",
        component: Help_02
    },
    {
        path: "/help-03",
        name: "Help03",
        component: Help_03
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
