<template>
    <div class="sm:mx-0 md:mx-24 lg:mx-0 xl:mx-0">
        <Loader v-if="isLoader"/>
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <div v-if="!$store.state.isAuthenticated"
             class="bg-white h-64 w-full border-green-top px-4 lg:px-24 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16 relative">
            <NoLoginText/>
        </div>
        <div v-else
             class="bg-white w-full border-green-top px-4 sm:h-full lg:px-24 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16">
            <div class="text-center text-2xl mb-10 mt-5 font-l">{{$t('my_address')}}</div>
            <div v-for="(address,index) in addresses" :key='address.id'>
                <ListAddress :address="address"/>
                <hr v-if="index != addresses.length-1">
            </div>
            <div @click="goAddAddress"
                 class="w-64 mx-auto bg-green text-white text-center mt-10 py-2 px-2 focus:outline-none cursor-pointer">
                {{$t('add_new_address')}}
            </div>
        </div>
    </div>
</template>
<script>
    import axios from 'axios'
    import ListAddress from "../components/ListAddress";
    import NoLoginText from "../components/NoLoginText";
    import Loader from "../components/Loader";

    export default {
        components: {
            ListAddress,
            NoLoginText,
            Loader
        },
        data() {
            return {
                addresses: [],
                isLoading: false
            }
        },
        created() {
            this.loadAddress()
        },
        methods: {
            loadAddress() {
                this.isLoading = true
                axios.get(this.$store.state.endpoints.addressUrL, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    }
                }).then((res) => {
                        this.addresses = res.data.address
                        this.$store.commit("setUserAddress", res.data.address);
                        this.isLoading = false
                    }
                ).catch(e => {
                    this.isLoading = false
                    this.$message.error(this.$t('error_Oops_') + e.status + ', at Load address');
                })
            },
            goAddAddress() {
                this.$router.push({
                    name: 'AddAddress'
                })
            }
        }
    }
</script>