<template>
    <div class="md:mx-24 sm:mx-0 lg:mx-0 xl:mx-0">
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <div class="bg-white w-full border-green-top px-4 sm:h-full lg:px-64 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16">
            <div class="text-center text-2xl mb-10 mt-5 font-l">Please input your email</div>
            <label v-if="validation.firstError('email')"
                   class="block text-sm mb-2 text-red"
                   for="email">{{validation.firstError('email')}}</label>
            <el-input id="email"
                      placeholder="Please input email"
                      v-model="email">
            </el-input>
            <div class="mb-6 pl-2 w-1/2 mx-auto mt-8">
                <button @click="sentEmail()"
                        class="w-full bg-green text-white py-2 px-10 focus:outline-none "
                        type="button">Sent to email
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import {Validator} from "../main";

    export default {
        data() {
            return {
                email: ''
            }
        },
        validators: {
            email(value) {
                return Validator.value(value)
                    .required("please input email")
                    .email('invalid email')
            }
        },
        methods: {
            sentEmail() {
                this.$validate(["email"]);
                console.log(this.validation.firstError("email"))
                if (this.validation.firstError("email") == null) {
                    axios.post(this.$store.state.endpoints.forgotPasswordUrL, {
                        "email": this.email
                    }).then(res => {
                        console.log(res)
                    }).catch(e => console.log(e.message))
                }

            }
        }
    }
</script>