<template>
    <div class="px-3 md:px-5 lg:px-10 mt-5">
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
            <label v-if="!validation.firstError('address')"
                   class="block text-sm mb-2"
                   for="address">{{$t('address')}}</label>
            <label v-else
                   class="block text-red text-sm mb-2"
                   for="address">{{$t(validation.firstError('address'))}}</label>
            <el-input id="address"
                      :placeholder="$t('')"
                      v-model="address">
            </el-input>
        </div>


        <div class="mb-6 sm:px-10 md:px-16 lg:px-0">
            <label v-if="!validation.firstError('city')"
                   class="block text-sm mb-2"
                   for="city">{{$t('city')}}</label>
            <label v-else
                   class="block text-red text-sm mb-2"
                   for="city">{{$t(validation.firstError('city'))}}</label>
            <el-input id="city"
                      :placeholder="$t('')"
                      v-model="city">
            </el-input>
        </div>


        <div class="mb-6 flex justify-between sm:px-10 md:px-16 lg:px-0">
            <div class="w-1/2 pr-1">
                <label v-if="!validation.firstError('state')"
                       class="block text-sm mb-2">{{$t('state')}}</label>
                <label v-else
                       class="block text-red text-sm mb-2">{{$t(validation.firstError('state'))}}</label>
                <el-input id="state"
                          :placeholder="$t('')"
                          v-model="state">
                </el-input>
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
                          v-model="post_code">
                </el-input>
            </div>
        </div>

        <div class="flex flex-wrap sm:px-10 md:px-16 lg:px-8" style="place-content: center;">
            <div class="mb-4 pr-2 w-1/2">
                <label v-if="!validation.firstError('country')"
                       class="block text-sm mb-2">{{$t('country')}}</label>
                <label v-else
                       class="block text-red text-sm mb-2">{{$t(validation.firstError('country'))}}</label>
                <el-select v-model="country" ref="country" placeholder="Select Country">
                    <el-option
                            v-for="item in countryOptions"
                            :key="item"
                            :label="item"
                            :value="item">
                    </el-option>
                </el-select>
            </div>
        </div>

        <div class="text-center">
            <el-checkbox v-model="checked">{{$t('save_my_address')}}</el-checkbox>
        </div>

        <div @click="add"
             class="w-64 mx-auto bg-green text-white text-center mt-10 py-2 px-2 focus:outline-none cursor-pointer">
            {{$t('add_new_address')}}
        </div>
    </div>
</template>
<script>
    import {Validator} from "../main";
    import axios from "axios";

    export default {
        props: [
            "dataAddress", "chooseNewAddress"
        ],
        data() {
            return {
                recipient: '',
                address: '',
                city: '',
                state: '',
                post_code: '',
                country: '',
                countryOptions: [
                    'Russia',
                    'Germany',
                    'United Kingdom',
                    'France',
                    'Italy',
                    'Spain',
                    'Ukraine',
                    'Poland',
                    'Romania',
                    'Netherlands',
                    'Belgium',
                    'Czech Republic (Czechia)',
                    'Greece',
                    'Portugal',
                    'Sweden',
                    'Hungary',
                    'Belarus',
                    'Austria',
                    'Serbia',
                    'Switzerland',
                    'Bulgaria',
                    'Denmark',
                    'Finland',
                    'Slovakia',
                    'Norway',
                    'Ireland',
                    'Croatia',
                    'Moldova',
                    'Bosnia and Herzegovina',
                    'Albania',
                    'Lithuania',
                    'North Macedonia',
                    'Slovenia',
                    'Latvia',
                    'Estonia',
                    'Montenegro',
                    'Luxembourg',
                    'Malta',
                    'Iceland',
                    'Andorra',
                    'Monaco',
                    'Liechtenstein',
                    'San Marino',
                    'Holy See',
                ].sort(),
                stateOptions: [
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
                checked: false
            }
        },
        validators: {
            recipient(value) {
                return Validator.value(value)
                    .required("error_address_recipient");
            },
            address(value) {
                return Validator.value(value)
                    .required("error_address_street");
            },
            city(value) {
                return Validator.value(value)
                    .required("error_address_city");
            },
            state(value) {
                return Validator.value(value)
                    .required("error_address_state");
            },
            post_code(value) {
                return Validator.value(value)
                    .required("error_address_postalCode_require")
                    // .length(5, "error_address_postalCode_number")
            },
            country(value) {
                return Validator.value(value)
                    .required("error_address_country");
            },
        },
        created() {
            if (this.chooseNewAddress) {
                this.recipient = this.dataAddress.recipient
                this.address = this.dataAddress.house_number
                this.city = this.dataAddress.street
                this.state = this.dataAddress.city
                this.post_code = this.dataAddress.post_code
            }
        },
        methods: {
            add() {
                this.$validate().then(success => {
                    if (success) {
                        this.$emit('updateAddress', this.recipient, this.address, this.city, this.state, this.post_code,this.country, this.checked);
                        this.recipient = ''
                    }
                })
            },
            cancel() {

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