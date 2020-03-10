<template>
    <div class="sm:mx-0 md:mx-24 lg:mx-0 xl:mx-0">
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <div v-if="!$store.state.isAuthenticated"
             class="bg-white h-64 w-full border-green-top px-4 lg:px-24 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16 relative">
            <NoLoginText/>
        </div>
        <div v-else
             class="bg-white w-full border-green-top px-4 sm:h-full sm:px-8 md:px-10 lg:px-24 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16">
            <div class="text-center text-2xl mb-10 mt-5 font-l">Edit Address</div>
            <div class="mb-6 sm:px-10 md:px-16 lg:px-0">
                <label v-if="!validation.firstError('recipient')"
                       class="block text-sm mb-2"
                       for="recipient">Firstname and Lastname of Recipient</label>
                <label v-else
                       class="block text-red text-sm mb-2"
                       for="recipient">Please input Firstname and Lastname of Recipient</label>
                <el-input id="recipient"
                          placeholder="Please input"
                          v-model="recipient">
                </el-input>
            </div>


            <div class="mb-6 sm:px-10 md:px-16 lg:px-0">
                <label v-if="!validation.firstError('house_number')"
                       class="block text-sm mb-2"
                       for="house_number">House number</label>
                <label v-else
                       class="block text-red text-sm mb-2"
                       for="house_number">Please input House number</label>
                <el-input id="house_number"
                          placeholder="Please input"
                          v-model="house_number">
                </el-input>
            </div>


            <div class="mb-6 sm:px-10 md:px-16 lg:px-0">
                <label v-if="!validation.firstError('street')"
                       class="block text-sm mb-2"
                       for="street">Street</label>
                <label v-else
                       class="block text-red text-sm mb-2"
                       for="street">Please input Street</label>
                <el-input id="street"
                          placeholder="Please input"
                          v-model="street">
                </el-input>
            </div>


            <div class="mb-6 flex justify-between sm:px-10 md:px-16 lg:px-0">
                <div class="w-1/2 pr-1">
                    <label v-if="!validation.firstError('city')"
                           class="block text-sm mb-2">City</label>
                    <label v-else
                           class="block text-red text-sm mb-2">Please input City</label>
                    <el-select v-model="city" placeholder="Select">
                        <el-option
                                v-for="item in cityOptions"
                                :key="item"
                                :label="item"
                                :value="item">
                        </el-option>
                    </el-select>
                </div>
                <div class="w-1/2 pl-1">
                    <label v-if="!validation.firstError('post_code')"
                           class="block text-sm mb-2"
                           for="post_code">Postal Code</label>
                    <label v-else
                           class="block text-red text-sm mb-2"
                           for="post_code">Please input Postal Code</label>
                    <el-input id="post_code"
                              placeholder="Please input"
                              v-model="post_code">
                    </el-input>
                </div>
            </div>

            <div class="flex">
                <!--                case the uer address length = 1-->
                <div v-if="$store.state.userAddress.length == 1"
                     class="w-64 mx-auto bg-red text-white text-center mt-10 py-2 px-2 focus:outline-none cursor-not-allowed opacity-50">
                    Delete Address
                </div>

                <!--                case user address > 1-->
                <div v-else @click="deleteAddress"
                     class="w-64 mx-auto bg-red text-white text-center mt-10 py-2 px-2 focus:outline-none cursor-pointer">
                    Delete Address
                </div>

                <div @click="editAddress"
                     class="w-64 mx-auto bg-green text-white text-center mt-10 py-2 px-2 focus:outline-none cursor-pointer">
                    Save
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {Validator} from "../main";
    import axios from "axios";
    import NoLoginText from "../components/NoLoginText";

    export default {
        components: {
            NoLoginText
        },
        data() {
            return {
                index: '',
                recipient: '',
                house_number: '',
                street: '',
                city: '',
                post_code: '',
                cityOptions: [
                    'Baden-Württemberg',
                    'Bayern',
                    'Berlin',
                    'Brandenburg',
                    'Bremen',
                    'Hamburg',
                    'Hessen',
                    'Niedersachsen',
                    'Mecklenburg-Vorpommern',
                    'Nordrhein-Westfalen',
                    'Rheinland-Pfalz',
                    'Saarland',
                    'Sachsen',
                    'Sachsen-Anhalt',
                    'Schleswig-Holstein',
                    'Thüringen'
                ]
            }
        },
        validators: {
            recipient(value) {
                return Validator.value(value)
                    .required("recipient");
            },
            house_number(value) {
                return Validator.value(value)
                    .required("house_number");
            },
            street(value) {
                return Validator.value(value)
                    .required("street");
            },
            city(value) {
                return Validator.value(value)
                    .required("city");
            },
            post_code(value) {
                return Validator.value(value)
                    .required("post_code");
            },
        },
        created() {
            this.index = this.$store.state.userAddress.findIndex(item => item.id == this.$route.params.id)
            console.log(this.$store.state.userAddress[this.index])
            this.recipient = this.$store.state.userAddress[this.index].recipient
            this.house_number = this.$store.state.userAddress[this.index].house_number
            this.street = this.$store.state.userAddress[this.index].street
            this.city = this.$store.state.userAddress[this.index].city
            this.post_code = this.$store.state.userAddress[this.index].post_code
        },
        methods: {
            editAddress() {
                axios.put(`http://${window.location.hostname}:8000/api/accounts/user/address/`, {
                    id: this.$route.params.id,
                    recipient: this.recipient,
                    street: this.street,
                    house_number: this.house_number,
                    post_code: this.post_code,
                    city: this.city
                }, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                }).then(() => {
                    this.$router.push({
                        name: 'ViewAddress'
                    })
                }).catch()
            },
            deleteAddress() {
                if (this.$store.state.userAddress.length == 1) {
                    alert("can not delete")
                } else if (this.$store.state.userAddress[this.$store.state.indexUserAddress].id == this.$route.params.id) {
                    this.$store.commit("setIndexUserAddress", this.$store.state.indexUserAddress - 1);
                    axios.delete(`http://${window.location.hostname}:8000/api/accounts/user/address/` + this.$route.params.id + '/', {
                        headers: {
                            Authorization: `JWT ${this.$store.state.jwt}`,
                            'Content-Type': 'application/json'
                        },
                    }).then(() => {
                        this.$router.push({
                            name: 'ViewAddress'
                        })
                    }).catch()
                }
            }
        }
    }
</script>

<style scoped>
    .el-select {
        display: inline-block;
        position: relative;
        width: 100%;
    }
</style>