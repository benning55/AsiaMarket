<template lang="html">
    <div>
        <ul class="w-full py-6">
            <li class="inline-block px-5"> </li>
        </ul>
        <div class="auth">
            <form class="mt-16 w-11/12 sm:w-4/5 md:w-3/5 lg:w-3/5 xl:w-3/5 mx-auto bg-white shadow-md px-3 sm:px-3 md:px-5 lg:px-16 xl:px-16 pt-6 pb-8 mb-4"
                  style="border-top: 6px solid #619F21;">
                <div class="text-center text-2xl mb-10 mt-5 font-l">Login</div>
                <div class="mb-4 sm:px-10 md:px-16 lg:px-16">
                    <label v-if="!validation.firstError('username')"
                           class="block text-sm mb-2"
                           for="username"> {{$t('username')}}</label>
                    <label v-else
                           class="block text-red text-sm mb-2"
                           for="username">Please input Username</label>
                    <input
                            v-model="username"
                            v-bind:class="{ 'border-red': validation.firstError('username') }"
                            class="appearance-none border w-full py-2 px-3 text-gray leading-tight focus:outline-none"
                            id="username"
                            type="text"
                    />

                </div>
                <div class="mb-6 sm:px-10 md:px-16 lg:px-16">
                    <label v-if="!validation.firstError('password')"
                           class="block text-sm mb-2"
                           for="password">{{$t('password')}}</label>
                    <label v-else
                           class="block text-red text-sm mb-2"
                           for="password">Please input Password</label>
                    <input v-model="password"
                           v-bind:class="{ 'border-red': validation.firstError('password') }"
                           class="appearance-none border w-full py-2 px-3 text-gray mb-3 leading-tight focus:outline-none"
                           id="password"
                           type="text"/>
                </div>

                <div class="mb-6 sm:px-10 md:px-16 lg:px-16">
                    <button @click="authenticate()"
                            class="w-full bg-green text-white py-2 px-20 focus:outline-none"
                            type="button">{{$t('login')}}
                    </button>
                    <div class="text-center font-l mt-4" style="font-size: 10px">Use Asian market in First time? <span class="text-orange">Register Now</span></div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import {Validator} from "../main";

    export default {
        name: "Login",
        comments: {
        },
        data() {
            return {
                username: '',
                password: '',
                LoginForm: {
                    username: '',
                    password: ''
                }
            }
        },
        validators: {
            username(value) {
                return Validator.value(value)
                    .required("กรุณาใส่อีเมลล์");
            },
            password(value) {
                return Validator.value(value)
                    .required("กรุณาใส่รหัสผ่าน")
                // .minLength(6, "รหัสผ่านต้องมีมากกว่า 6 ตัวขึ้นไป");
            }
        },
        methods: {
            authenticate() {
                this.$validate(["username", "password"]);
                console.log(this.validation.firstError("password"))
                if (
                    this.validation.firstError("username") == null &&
                    this.validation.firstError("password") == null
                ) {
                    const payload = {
                        username: this.username,
                        password: this.password
                    };
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
                            //Even though the authentication returned a user object that can be
                            //decoded, we fetch it again. This way we aren't super dependant on
                            //JWT and can plug in something else.
                            const axiosInstance = axios.create(base);
                            axiosInstance({
                                url: "/user/",
                                method: "get",
                                params: {}
                            }).then((response) => {
                                this.$store.commit("setAuthUser",
                                    {authUser: response.data, isAuthenticated: true}
                                );
                                console.log(this.$store.state.authUser);
                                console.log(this.$store.state.authUser['profile']);
                                this.$router.push("/movies")
                            }).catch((error) => {
                                console.log(error);
                                alert(this.$store.state.jwt)
                            })
                        })
                        .catch((error) => {

                            console.log(error);
                            console.debug(error);
                            console.dir(error);
                            alert('Fuck You')
                        })
                }

            }
        }
    }
</script>

<style lang="css">
</style>