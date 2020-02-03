<template>
    <div>
        <ul class="w-full py-6">
            <li class="inline-block px-5">LOGO</li>
        </ul>
        <div class="auth">
            <form class="mt-16 w-11/12 sm:w-4/5 md:w-2/3 lg:w-2/3 xl:w-2/3 mx-auto bg-white shadow-md px-8 pt-6 pb-8 mb-4"
                  style="border-top: 6px solid #619F21;">
                <h1 class="text-3xl font-hairline text-center mb-5">Register</h1>
                <div v-if="state == 0">
                    <div class="flex flex-wrap sm:px-10 md:px-16 lg:px-16">
                        <div class="mb-4 pr-2 w-1/2">
                            <label class="block text-sm mb-2"
                                   for="firstname"> Firstname</label>
                            <label class="block text-red text-sm mb-2"
                                   for="firstname">Please input Firstname</label>
                            <input v-model="firstname"
                                   class="appearance-none border w-full py-2 px-3 text-gray leading-tight focus:outline-none"
                                   id="firstname"
                                   type="text"/>
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <label class="block text-sm mb-2"
                                   for="lastname">Lastname</label>
                            <label class="block text-red text-sm mb-2"
                                   for="lastname">Please input Lastname</label>
                            <input v-model="lastname"
                                   class="appearance-none border w-full py-2 px-3 text-gray mb-3 leading-tight focus:outline-none"
                                   id="lastname"
                                   type="text"/>
                        </div>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full">
                        <label class="block text-sm mb-2"
                               for="address">Address</label>
                        <label class="block text-red text-sm mb-2"
                               for="address">Please input Address</label>
                        <input v-model="address"
                               class="appearance-none border w-full py-2 px-3 text-gray mb-3 leading-tight focus:outline-none"
                               id="address"
                               type="text"/>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full">
                        <label class="block text-sm mb-2"
                               for="addition">Addition Information</label>
                        <input v-model="addition"
                               class="appearance-none border w-full py-2 px-3 text-gray mb-3 leading-tight focus:outline-none"
                               id="addition"
                               type="text"/>
                    </div>
                    <div class="flex flex-wrap sm:px-10 md:px-16 lg:px-16">
                        <div class="mb-4 pr-2 w-1/2">
                            <label class="block text-sm mb-2"
                                   for="city"> City</label>
                            <label class="block text-red text-sm mb-2"
                                   for="city">Please input City</label>
                            <input v-model="username"
                                   class="appearance-none border w-full py-2 px-3 text-gray leading-tight focus:outline-none"
                                   id="city"
                                   type="text"/>
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <label class="block text-sm mb-2"
                                   for="postal">Postal</label>
                            <label class="block text-red text-sm mb-2"
                                   for="postal">Please input Postal</label>
                            <input v-model="password"
                                   class="appearance-none border w-full py-2 px-3 text-gray mb-3 leading-tight focus:outline-none"
                                   id="postal"
                                   type="text"/>
                        </div>
                    </div>
                    <div class="flex flex-wrap sm:px-10 md:px-16 lg:px-16">
                        <div class="mb-4 pr-2 w-1/2">
                            <label class="block text-sm mb-2"
                                   for="dob">Date of Birth</label>
                            <label class="block text-red text-sm mb-2"
                                   for="dob">Please input Date of Birth</label>
                            <input v-model="username"
                                   class="appearance-none border w-full py-2 px-3 text-gray leading-tight focus:outline-none"
                                   id="dob"
                                   type="text"/>
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <label class="block text-sm mb-2"
                                   for="phone">Phone Number</label>
                            <label class="block text-red text-sm mb-2"
                                   for="phone">Please input Phone Number</label>
                            <input v-model="password"
                                   class="appearance-none border w-full py-2 px-3 text-gray mb-3 leading-tight focus:outline-none"
                                   id="phone"
                                   type="text"/>
                        </div>
                    </div>
                    <div class="flex flex-wrap sm:px-10 md:px-16 lg:px-16">
                        <div class="mb-4 w-1/2">
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <button @click="state++"
                                    class="w-full bg-green text-white py-2 px-20 focus:outline-none"
                                    type="button">Next
                            </button>
                        </div>
                    </div>
                </div>
                <div v-if="state == 1">
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full">
                        <label class="block text-sm mb-2"
                               for="email">Email</label>
                        <label class="block text-red text-sm mb-2"
                               for="email">Please input Email</label>
                        <input v-model="email"
                               class="appearance-none border w-full py-2 px-3 text-gray mb-3 leading-tight focus:outline-none"
                               id="email"
                               type="text"/>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full">
                        <label class="block text-sm mb-2"
                               for="username">Username</label>
                        <label class="block text-red text-sm mb-2"
                               for="username">Please input Username</label>
                        <input v-model="username"
                               class="appearance-none border w-full py-2 px-3 text-gray mb-3 leading-tight focus:outline-none"
                               id="username"
                               type="text"/>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full">
                        <label class="block text-sm mb-2"
                               for="password">Password</label>
                        <label class="block text-red text-sm mb-2"
                               for="password">Please input Password</label>
                        <input v-model="password"
                               class="appearance-none border w-full py-2 px-3 text-gray mb-3 leading-tight focus:outline-none"
                               id="password"
                               type="text"/>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full">
                        <label class="block text-sm mb-2"
                               for="repassword">Password Again</label>
                        <label class="block text-red text-sm mb-2"
                               for="repassword">Please input Password Again</label>
                        <input v-model="repassword"
                               class="appearance-none border w-full py-2 px-3 text-gray mb-3 leading-tight focus:outline-none"
                               id="repassword"
                               type="text"/>
                    </div>
                    <div class="flex justify-between sm:px-10 md:px-16 lg:px-16">
                        <div class="mb-4 pr-2 w-1/3">
                            <button @click="state--"
                                    class="w-full bg-white text-black_p py-2 focus:outline-none flex justify-start"
                                    type="button">
                                    <p class="inline-flex ml-0">
                                        <i class="material-icons">keyboard_arrow_left</i><span>Previous</span>
                                    </p>
                            </button>
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <button @click="signin"
                                    class="w-full bg-green text-white py-2 px-20 focus:outline-none "
                                    type="button">Login
                            </button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    // import {Validator} from "../main";

    export default {
        name: 'Register',
        data() {
            return {
                firstname:'',
                lastname:'',
                email: '',
                username: '',
                password: '',
                password2: '',
                state: 0
            }
        },
        methods: {
            registered() {
                const payload = {
                    username: this.username,
                    password: this.password,
                    first_name: '',
                    last_name: '',
                    email: this.email
                };
                axios.post(this.$store.state.endpoints.registerUrL, payload)
                    .then((response) => {
                        console.log(response.data);
                        alert(response.data);
                    })
                    .catch((error) => {
                        console.log(error);
                        alert('fuck you');
                    })
            }
        },
    }
</script>