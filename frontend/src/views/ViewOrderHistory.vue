<template>
    <div class="sm:mx-0 md:mx-24 lg:mx-0 xl:mx-0">
        <Loader v-if="isLoading"/>
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>

        <h1 class="sm:mt-16 lg:mt-16 xl:mt-16 py-1 text-xl font-l">Order History</h1>
        <div v-if="orders.length > 0" class="bg-white w-full px-4 sm:h-full lg:px-24 pb-5 mx-auto">
            <ListOrder v-for="order in orders" :key="order.id" :orderdata="order"/>
        </div>
        <div v-else-if="!$store.state.isAuthenticated" class="bg-white w-full px-4 h-64 lg:px-24 pb-5 mx-auto relative">
            <NoLoginText/>
        </div>
        <div v-else class="bg-white w-full px-4 h-64 lg:px-24 pb-5 mx-auto relative">
            <div class="center-y w-full">
                <h1 class="text-2xl text-center">You don't have any purchase orders</h1>
                <h1 @click="goHome" class="text-center text-orange cursor-pointer">Go back to Homepage</h1>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    import ListOrder from "../components/ListOrder";
    import NoLoginText from "../components/NoLoginText";
    import Loader from "../components/Loader";

    export default {
        components: {
            ListOrder, NoLoginText, Loader
        },
        data() {
            return {
                orders: [],
                isLoading:false
            }
        },
        created() {
            this.getOrder()
        },
        methods: {
            getOrder() {
                this.isLoading = true
                axios.get(`${this.$store.state.endpoints.host}/api/orders/order/`, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    }
                })
                    .then(res => {
                        this.isLoading = false
                        this.orders = res.data.data
                    })
                    .catch(e => {
                        this.isLoading = false
                        this.$message.error('Oops, Something is Error. code ' + e.status + ', at Load Order');
                    })
            },
            goHome() {
                this.$router.push({
                    name: 'Homepage'
                })
            },
            goLogin() {
                this.$router.push({
                    name: 'login'
                })
            }
        }
    }
</script>