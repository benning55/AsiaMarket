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
                <el-select v-model="city" :placeholder="$t('error_address_city')">
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

        <div class="text-center">
            <el-checkbox v-model="checked">Save in My Address</el-checkbox>
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
        props:[
            "dataAddress","chooseNewAddress"
        ],
        data() {
            return {
                recipient:'',
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
                checked: false
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
            if(this.chooseNewAddress){
                this.recipient = this.dataAddress.recipient
                this.house_number = this.dataAddress.house_number
                this.street = this.dataAddress.street
                this.city = this.dataAddress.city
                this.post_code = this.dataAddress.post_code
            }
        },
        methods: {
            add() {
                this.$validate().then(success => {
                    if (success) {
                        this.$emit('updateAddress',this.recipient, this.house_number, this.street, this.city, this.post_code,this.checked);
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