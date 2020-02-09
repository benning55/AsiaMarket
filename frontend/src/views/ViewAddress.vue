<template>
    <div class="md:mx-24 sm:mx-0 lg:mx-0 xl:mx-0">
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <div class="bg-white w-full border-green-top px-4 sm:h-full lg:px-32 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16">
            <div class="text-center text-2xl mb-10 mt-5 font-l">My Address</div>
            <div v-for="address in addresses" :key='address.id' >
                <ListAddress :address="address"/>
            </div>
        </div>
    </div>
</template>
<script>
    import ListAddress from "../components/ListAddress";

    export default {
        components: {
            ListAddress
        },
        data() {
            return {
                addresses: []
            }
        },
        created() {
            this.loadAddress()
        },
        methods:{
            loadAddress(){
                this.addresses = [
                    {
                        user_id:0,
                        address:'45/23',
                        addition:'none',
                        city:'eeeeee',
                        postalCode:'45161'
                    },
                    {
                        user_id:0,
                        address:'45/23',
                        addition:'nonesss',
                        city:'xxxxx',
                        postalCode:'151515'
                    }
                ]
            }
        }
    }
</script>