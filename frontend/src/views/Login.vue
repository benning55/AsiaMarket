<template lang="html">
    <div>
        <Loader v-if="isLoading"/>
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <div class="auth">
            <form class="mt-16 w-11/12 sm:w-4/5 md:w-3/5 lg:w-4/5 xl:w-full mx-auto bg-white shadow-md px-3 sm:px-3 md:px-5 lg:px-16 xl:px-16 pt-6 pb-8 mb-4"
                  style="border-top: 6px solid #619F21;">
                <el-alert v-if="error" type="error" show-icon @close="closeError">
                    {{error}}
                </el-alert>
                <div class="text-center text-2xl mb-10 mt-5 font-l">{{$t('login')}}</div>
                <div class="mb-4 sm:px-10 md:px-16 lg:px-10">
                    <label v-if="!validation.firstError('username')"
                           class="block text-sm mb-2"
                           for="username"> {{$t('username')}}</label>
                    <label v-else
                           class="block text-red text-sm mb-2"
                           for="username">{{$t(`${validation.firstError('username')}`)}}</label>
                    <el-input id="username"
                              @keyup.enter.native="$refs.password.focus"
                              ref="username"
                              type="text"
                              placeholder="Please input"
                              v-model="username">
                    </el-input>
                </div>
                <div class="mb-6 sm:px-10 md:px-16 lg:px-10">
                    <label v-if="!validation.firstError('password')"
                           class="block text-sm mb-2"
                           for="password">{{$t('password')}}</label>
                    <label v-else
                           class="block text-red text-sm mb-2"
                           for="password">{{$t(validation.firstError('password'))}}</label>
                    <el-input id="password"
                              ref="password"
                              @keyup.enter.native="authenticate"
                              placeholder="Please input"
                              v-model="password"
                              show-password>
                    </el-input>
                </div>

                <div class="mb-6 sm:px-10 md:px-16 lg:px-10">
                    <button @click="authenticate()"
                            class="w-full bg-green text-white py-2 px-20 focus:outline-none"
                            type="button">{{$t('login')}}
                    </button>
                    <div class="text-center font-l mt-4" style="font-size: 10px">{{$t('use_asian_market_in_first_time')}} <span
                            @click="goRegister" class="text-orange cursor-pointer">{{$t('register_now')}}</span></div>
                    <div class="text-center font-l mt-4" style="font-size: 10px">{{$t('forget_your_password')}} <span
                            @click="goForgetPassword" class="text-orange cursor-pointer">{{$t('click_here')}}</span></div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import {Validator} from "../main";
    import Loader from "../components/Loader";

    export default {
        name: "Login",
        components:{
            Loader
        },
        data() {
            return {
                username: '',
                password: '',
                LoginForm: {
                    username: '',
                    password: ''
                },
                error: '',
                isLoading: false
            }
        },
        validators: {
            username(value) {
                return Validator.value(value)
                    .required("error_user_username_require");
            },
            password(value) {
                return Validator.value(value)
                    .required("error_user_password_require")
                    .minLength(6, "error_user_password_length");
            }
        },
        mounted() {
            this.focusInput();
        },
        methods: {
            focusInput() {
                this.$refs.username.focus();
            },
            goRegister() {
                this.$router.push({
                    name: 'register'
                })
            },
            closeError() {
                console.log('close')
                this.error = ''
            },
            goForgetPassword() {
                this.$router.push({
                    name: 'ForgetPassword'
                })
            },
            authenticate() {
                this.$validate(["username", "password"]);
                if (
                    this.validation.firstError("username") == null &&
                    this.validation.firstError("password") == null
                ) {
                    const payload = {username: this.username, password: this.password};
                    this.isLoading = true
                    axios.post(this.$store.state.endpoints.obtainJWT, payload)
                        .then((response) => {
                            this.$store.commit('updateToken', response.data.token);
                            //get and set auth user
                            const base = {
                                baseURL: this.$store.state.endpoints.baseUrL,
                                headers: {
                                    // Set your Authorization to 'JWT', not Bearer!!!
                                    Authorization: `JWT ${this.$store.state.jwt}`,
                                    'Content-Type': 'application/json'
                                },
                                xhrFields: {
                                    withCredentials: true
                                }
                            };
                            const axiosInstance = axios.create(base);
                            axiosInstance({
                                url: "/user/",
                                method: "get",
                                params: {}
                            }).then((response) => {
                                this.$store.commit("setAuthUser",
                                    {authUser: response.data, isAuthenticated: true}
                                );
                                this.isLoading = false
                                this.$router.push("/")
                                // location.reload();
                            }).catch(e => {
                                this.isLoading = false
                                this.$message.error('Oops, Something is Error. code ' + e.status + ', at Login');
                            })
                        })
                        .catch((error) => {
                            this.isLoading = false
                            if (error.status == '400') {
                                this.error = 'Username or Password incorrect'
                            } else {
                                this.error = 'Something is wrong. Try again later'
                            }
                        })
                }
            }
        }
    }
</script>

<style lang="css">
    .auth {
        max-width: 42rem;
        margin: auto;
    }
</style>