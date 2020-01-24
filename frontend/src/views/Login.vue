<template lang="html">
    <div>
        <Navbar/>
        <div class="auth">

            <!--        <form>-->
            <!--            <h1>Log In</h1>-->
            <!--            <div class="form-group">-->
            <!--                <label for="exampleInputEmail1">Username</label>-->
            <!--                <input type="text" v-model="username" class="form-control" id="exampleInputEmail1"-->
            <!--                       aria-describedby="emailHelp"-->
            <!--                       placeholder="Enter Username">-->
            <!--                <small id="emailHelp" class="form-text text-muted">We'll never share your Username with anyone-->
            <!--                    else.</small>-->
            <!--            </div>-->

            <!--            <div class="form-group">-->
            <!--                <label for="exampleInputPassword1">Password</label>-->
            <!--                <input type="password" v-model="password" class="form-control" id="exampleInputPassword1"-->
            <!--                       placeholder="Password">-->
            <!--            </div>-->
            <!--            <router-link to="/register"><small>Don't have an account?</small></router-link>-->
            <!--            <br><br>-->
            <!--            <button type="submit" class="btn btn-primary" @click.prevent="authenticate">Submit</button>-->
            <!--        </form>-->
            <form

                    class="mt-16 w-full sm:w-4/5 md:w-2/3 lg:w-2/5 xl:w-1/3 mx-auto bg-white shadow-md px-8 pt-6 pb-8 mb-4"
                    style="border-top: 6px solid #619F21;"
            >
                <div class="mb-4 sm:px-10 md:px-16 lg:px-16">
                    <label
                            v-if="!validation.firstError('username')"
                            class="block text-gray-700 text-sm font-bold mb-2"
                            for="username"
                    >      {{$t('username')}}</label>
                    <label
                            v-else
                            class="block text-red-500 text-sm font-bold mb-2"
                            for="username"
                    >Please input Username</label>
                    <!-- <p v-if="usernameValidate" class="text-red-500 text-xs italic">Please input a Username.</p> -->
                    <input
                            v-model="username"
                            v-bind:class="{ 'is-invalid': validation.firstError('username') }"
                            class="appearance-none border w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                            id="username"
                            type="text"
                    />

                </div>
                <div class="mb-6 sm:px-10 md:px-16 lg:px-16">
                    <label
                            v-if="!validation.firstError('password')"
                            class="block text-gray-700 text-sm font-bold mb-2"
                            for="password"
                    >{{$t('password')}}</label>
                    <label
                            v-else
                            class="block text-red-500 text-sm font-bold mb-2"
                            for="password"
                    >Please input Password</label>
                    <!-- <p v-if="passwordValidate" class="text-red-500 text-xs italic">Please input a password.</p> -->
                    <input
                            v-model="password"
                            v-bind:class="{ 'border-red-500': validation.firstError('password') }"
                            class="appearance-none border w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                            id="password"
                            type="text"
                    />
                    <!-- <p class="text-red-500 text-xs italic">Please choose a password.</p> -->
                </div>

                <div class="mb-6 sm:px-10 md:px-16 lg:px-16">
                    <button
                            @click="authenticate()"
                            class="w-full bg-maingreen hover:bg-blue-700 text-white font-bold py-2 px-20 focus:outline-none focus:shadow-outline"
                            type="button"
                    >{{$t('login')}}
                    </button
                    >

                    <!--                <button-->
                    <!--                        v-else-->
                    <!--                        disabled-->
                    <!--                        class="w-full bg-green-500 text-white font-bold py-2 px-20 opacity-50 cursor-not-allowed"-->
                    <!--                >Sign In-->
                    <!--                </button>-->
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import {Validator} from "../main";
    import Navbar from "../components/Navbar";

    export default {
        name: "Login",
        components: {Navbar},
        comments: {
            Navbar
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