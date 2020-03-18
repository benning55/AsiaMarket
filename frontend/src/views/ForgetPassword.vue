<template>
    <div class="md:mx-24 sm:mx-0 lg:mx-0 xl:mx-0">
        <Loader v-if="isLoading" />
        <NavbarSpace/>
        <div class="bg-white w-full border-green-top px-4 sm:h-full lg:px-64 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16">
            <div class="text-center text-2xl mb-10 mt-5 font-l">{{$t('please_input_your_email')}}</div>
            <div class="mb-3">
                <el-alert v-if="error" type="error" show-icon @close="closeError">
                    {{error}}
                </el-alert>
                <el-alert v-else-if="success" type="success" show-icon @close="closeError">
                    {{$t('you_email_has_been_sent')}}
                </el-alert>
            </div>
            <label v-if="validation.firstError('email')"
                   class="block text-sm mb-2 text-red"
                   for="email">{{$t(validation.firstError('email'))}}</label>
            <el-input id="email"
                      placeholder="Please input email"
                      v-model="email">
            </el-input>
            <div class="mb-6 pl-2 w-1/2 mx-auto mt-8">
                <button @click="sentEmail()"
                        class="w-full bg-green text-white text-center py-2 focus:outline-none "
                        type="button">{{$t('sent_to_email')}}Sent to email
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import {Validator} from "../main";
    import Loader from "../components/Loader";
    import NavbarSpace from "../components/NavbarSpace";

    export default {
        components:{
            Loader,
            NavbarSpace
        },
        data() {
            return {
                email: '',
                error: '',
                success: false,
                isLoading:false
            }
        },
        validators: {
            email(value) {
                return Validator.value(value)
                    .required("error_user_email_require")
                    .email('error_user_email_invalid')
            }
        },
        methods: {
            sentEmail() {
                this.isLoading = true
                this.$validate(["email"]);
                if (this.validation.firstError("email") == null) {
                    axios.post(this.$store.state.endpoints.forgotPasswordUrL, {
                        "email": this.email
                    }).then(res => {
                        this.isLoading = false
                        this.success = true
                        this.error = ""
                    }).catch(e => {
                        this.isLoading = false
                        if (e.response.status == 404) {
                            this.error = 'error_user_email_not_found'
                        } else {
                            this.error = 'something_is_wrong_try_again_later'
                        }
                    })
                } else {
                    this.isLoading = false
                }

            },
            closeError() {
                this.error = ''
            }
        }
    }
</script>