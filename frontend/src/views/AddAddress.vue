<template>
    <div class="sm:mx-0 md:mx-24 lg:mx-0 xl:mx-0">
        <Loader v-if="isLoading"/>
        <NavbarSpace/>
        <div v-if="!$store.state.isAuthenticated"
             class="bg-white h-64 w-full border-green-top px-4 lg:px-24 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16 relative">
            <NoLoginText/>
        </div>
        <div v-else
             class="bg-white w-full border-green-top px-4 sm:h-full sm:px-8 md:px-10 lg:px-24 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16">
            <div class="text-center text-2xl mb-10 mt-5 font-l">{{$t('add_new_address')}}</div>
            <div class="mb-6 sm:px-10 md:px-16 lg:px-0">
                <label v-if="!validation.firstError('recipient')"
                       class="block text-sm mb-2"
                       for="recipient">{{$t('firstname_and_lastname_of_recipient')}}</label>
                <label v-else
                       class="block text-red text-sm mb-2"
                       for="recipient">{{$t(validation.firstError('recipient'))}}</label>
                <el-input id="recipient"
                          :placeholder="$t('')"
                          v-model="recipient">
                </el-input>
            </div>


            <div class="mb-6 sm:px-10 md:px-16 lg:px-0">
                <label v-if="!validation.firstError('house_number')"
                       class="block text-sm mb-2"
                       for="house_number">{{$t('house_number')}}</label>
                <label v-else
                       class="block text-red text-sm mb-2"
                       for="house_number">{{$t(validation.firstError('house_number'))}}</label>
                <el-input id="house_number"
                          :placeholder="$t('')"
                          v-model="house_number">
                </el-input>
            </div>


            <div class="mb-6 sm:px-10 md:px-16 lg:px-0">
                <label v-if="!validation.firstError('street')"
                       class="block text-sm mb-2"
                       for="street">{{$t('street')}}</label>
                <label v-else
                       class="block text-red text-sm mb-2"
                       for="street">{{$t(validation.firstError('street'))}}</label>
                <el-input id="street"
                          :placeholder="$t('')"
                          v-model="street">
                </el-input>
            </div>


            <div class="mb-6 flex justify-between sm:px-10 md:px-16 lg:px-0">
                <div class="w-1/2 pr-1">
                    <label v-if="!validation.firstError('city')"
                           class="block text-sm mb-2">{{$t('city')}}</label>
                    <label v-else
                           class="block text-red text-sm mb-2">{{$t(validation.firstError('city'))}}</label>
                    <el-select v-model="city" :placeholder="$t('')">
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
                           for="post_code">{{$t('postal')}}</label>
                    <label v-else
                           class="block text-red text-sm mb-2"
                           for="post_code">{{$t(validation.firstError('post_code'))}}</label>
                    <el-input id="post_code"
                              :placeholder="$t('')"
                              type="number"
                              v-model="post_code">
                    </el-input>
                </div>
            </div>


            <div @click="addAddress"
                 class="w-64 mx-auto bg-green text-white text-center mt-10 py-2 px-2 focus:outline-none cursor-pointer">
                {{$t('add_new_address')}}
            </div>

            <button class="w-32 mt-5 text-black_p py-2 focus:outline-none flex justify-start"
                    type="button">
                <p @click="$router.go(-1)" class="inline-flex ml-0">
                    <i class="material-icons">keyboard_arrow_left</i><span>{{$t('previous')}}</span>
                </p>
            </button>

        </div>
    </div>
</template>

<script>
    import {Validator} from "../main";
    import axios from "axios";
    import NoLoginText from "../components/NoLoginText";
    import Loader from "../components/Loader";
    import NavbarSpace from "../components/NavbarSpace";

    export default {
        components: {
            NoLoginText,
            Loader,
            NavbarSpace
        },
        data() {
            return {
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
                ],
                isLoading:false
            }
        },
        validators: {
            recipient(value) {
                return Validator.value(value)
                    .required("error_address_recipient");
            },
            house_number(value) {
                return Validator.value(value)
                    .required("error_address_house_number");
            },
            street(value) {
                return Validator.value(value)
                    .required("error_address_street");
            },
            city(value) {
                return Validator.value(value)
                    .required("error_address_city");
            },
            post_code(value) {
                return Validator.value(value)
                    .required("error_address_postalCode_require")
                    .length(5, "error_address_postalCode_number")
            },
        },
        created() {
            window.scrollTo(0, 0);
        },
        methods: {
            addAddress() {
                this.$validate().then(success => {
                    if (success) {
                        this.isLoading = true
                        axios.post(this.$store.state.endpoints.host + '/api/accounts/user/address/', {
                            recipient: this.recipient,
                            house_number: this.house_number,
                            street: this.street,
                            city: this.city,
                            post_code: this.post_code
                        }, {
                            headers: {
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                        }).then(() => {
                            this.isLoading = false
                            this.$router.push({
                                name: 'ViewAddress'
                            })
                        }).catch(e => {
                            this.isLoading = false
                            this.$message.error(this.$t('error_Oops_') + e.response.status+', at add address');
                        })

                    }
                })
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