<template>
    <div class="sm:mx-0 md:mx-24 lg:mx-0 xl:mx-0">
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <div class="bg-white w-full border-green-top px-4 sm:h-full lg:px-24 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16">
            <ListOrder v-for="order in orders" :key="order.id" :orderdata="order"/>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    import ListOrder from "../components/ListOrder";

    export default {
        components: {
            ListOrder
        },
        data() {
            return {
                orders:[]
            }
        },
        created() {
            this.getOrder()
        },
        methods: {
            getOrder() {
                axios.get(`http://${window.location.hostname}:8000/api/orders/order/`, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    }
                })
                    .then(res => {
                        console.log(res.data.data)
                        this.orders = res.data.data
                    })
                    .catch(e => console.log(e))
            }
        }
    }
</script>