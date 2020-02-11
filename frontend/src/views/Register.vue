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
                            <label v-if="!validation.firstError('firstname')"
                                   class="block text-sm mb-2"
                                   for="firstname"> Firstname</label>
                            <label v-else
                                   class="block text-red text-sm mb-2"
                                   for="firstname">Please input Firstname</label>
                            <el-input id="firstname"
                                      placeholder="Please input"
                                      v-model="firstname">
                            </el-input>
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <label v-if="!validation.firstError('lastname')"
                                   class="block text-sm mb-2"
                                   for="lastname">Lastname</label>
                            <label v-else class="block text-red text-sm mb-2"
                                   for="lastname">Please input Lastname</label>
                            <el-input id="lastname"
                                      placeholder="Please input"
                                      v-model="lastname">
                            </el-input>
                        </div>
                    </div>

                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full text-center ">
                        <label v-if="!validation.firstError('sex')"
                               class="block text-sm mb-2 text-left"
                               for="sex">Select Gender</label>
                        <label v-else
                               class="block text-red text-sm mb-2 text-left"
                               for="sex">Please Select Gender</label>
                        <el-radio-group id="sex" v-model="sex" style="border-radius: 0px">
                            <el-radio-button label="Male">Male</el-radio-button>
                            <el-radio-button label="Female">Female</el-radio-button>
                        </el-radio-group>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full">
                        <label v-if="!validation.firstError('houseNumber')"
                               class="block text-sm mb-2"
                               for="houseNumber">House Number</label>
                        <label v-else
                               class="block text-red text-sm mb-2"
                               for="houseNumber">Please input House Number</label>
                        <el-input id="houseNumber"
                                  placeholder="Please input"
                                  v-model="houseNumber">
                        </el-input>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full">
                        <label v-if="!validation.firstError('street')"
                               class="block text-sm mb-2"
                               for="houseNumber">Street</label>
                        <label v-else class="block text-sm mb-2 text-red"
                               for="street">Please input Street</label>
                        <el-input id="street"
                                  placeholder="Please input"
                                  v-model="street">
                        </el-input>
                    </div>
                    <div class="flex flex-wrap sm:px-10 md:px-16 lg:px-16">
                        <div class="mb-4 pr-2 w-1/2">
                            <label v-if="!validation.firstError('city')"
                                   class="block text-sm mb-2"> City</label>
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
                        <div class="mb-6 pl-2 w-1/2">
                            <label v-if="!validation.firstError('postalCode')"
                                   class="block text-sm mb-2"
                                   for="postal">Postal</label>
                            <label v-else
                                   class="block text-red text-sm mb-2"
                                   for="postal">Please input Postal</label>
                            <el-input id="postal"
                                      placeholder="Please input"
                                      type="number"
                                      v-model="postalCode">
                            </el-input>
                        </div>
                    </div>
                    <div class="flex flex-wrap sm:px-10 md:px-16 lg:px-16">
                        <div class="mb-4 pr-2 w-1/2">
                            <label v-if="!validation.firstError('dob')"
                                   class="block text-sm mb-2">Date of Birth</label>
                            <label v-else
                                   class="block text-red text-sm mb-2">Please input Date of Birth</label>
                            <el-date-picker
                                    style="width: 100%;border-radius: 0px"
                                    v-model="dob"
                                    type="date"
                                    placeholder="Pick a date"
                                    default-value="2000-01-01"
                                    format="yyyy-MM-dd"
                                    value-format="yyyy-MM-dd">
                            </el-date-picker>
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <label v-if="!validation.firstError('phone')"
                                   class="block text-sm mb-2"
                                   for="phone">Phone Number</label>
                            <label v-else
                                   class="block text-red text-sm mb-2"
                                   for="phone">Please input Phone Number</label>
                            <el-input id="phone"
                                      placeholder="Please input"
                                      type="number"
                                      v-model="phone">
                            </el-input>
                        </div>
                    </div>
                    <div class="flex flex-wrap sm:px-10 md:px-16 lg:px-16">
                        <div class="mb-4 w-1/2">
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <button @click="addState()"
                                    class="w-full bg-green text-white py-2 px-20 focus:outline-none"
                                    type="button">Next
                            </button>
                        </div>
                    </div>
                </div>
                <div v-if="state == 1">
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full">
                        <label v-if="!validation.firstError('email')"
                               class="block text-sm mb-2"
                               for="email">Email</label>
                        <label v-else
                               class="block text-red text-sm mb-2"
                               for="email">Please input Email</label>
                        <el-input id="email"
                                  placeholder="Please input"
                                  v-model="email">
                        </el-input>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full">
                        <label v-if="!validation.firstError('username')"
                               class="block text-sm mb-2"
                               for="username">Username</label>
                        <label v-else
                               class="block text-red text-sm mb-2"
                               for="username">Please input Username</label>
                        <el-input id="username"
                                  placeholder="Please input"
                                  v-model="username">
                        </el-input>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full">
                        <label v-if="!validation.firstError('password')"
                               class="block text-sm mb-2"
                               for="password">Password</label>
                        <label v-else
                               class="block text-red text-sm mb-2"
                               for="password">Please input Password</label>
                        <el-input id="password"
                                  placeholder="Please input"
                                  v-model="password"
                                  show-password>
                        </el-input>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full">
                        <label v-if="!validation.firstError('password2')"
                               class="block text-sm mb-2"
                               for="password2">Password Again</label>
                        <label v-else
                               class="block text-red text-sm mb-2"
                               for="password2">Please input Password Again</label>
                        <el-input id="password2"
                                  placeholder="Please input"
                                  v-model="password2"
                                  show-password>
                        </el-input>
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
                            <button @click="addState()"
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
    import {Validator} from "../main";

    export default {
        name: 'Register',
        data() {
            return {
                firstname: '',
                lastname: '',
                sex: '',
                houseNumber: '',
                street: '',
                city: '',
                postalCode: '',
                dob: '',
                phone: '',
                email: '',
                username: '',
                password: '',
                password2: '',
                state: 0,
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
            firstname(value) {
                return Validator.value(value)
                    .required("firstname");
            },
            lastname(value) {
                return Validator.value(value)
                    .required("lastname")
                // .minLength(6, "รหัสผ่านต้องมีมากกว่า 6 ตัวขึ้นไป");
            },
            sex(value) {
                return Validator.value(value)
                    .required("sex")
            },
            houseNumber(value) {
                return Validator.value(value)
                    .required("address")
            },
            street(value) {
                return Validator.value(value)
                    .required("address")
            },
            city(value) {
                return Validator.value(value)
                    .required("city")
            },
            postalCode(value) {
                return Validator.value(value)
                    .required("postalCode")
            },
            dob(value) {
                return Validator.value(value)
                    .required("dob")
            },
            phone(value) {
                return Validator.value(value)
                    .required("phone")
                // .minLength(6, "รหัสผ่านต้องมีมากกว่า 6 ตัวขึ้นไป");
            },
            email(value) {
                return Validator.value(value)
                    .required("email")
                    .email('invalid')
            },
            username(value) {
                return Validator.value(value)
                    .required("username")
                // .minLength(6, "รหัสผ่านต้องมีมากกว่า 6 ตัวขึ้นไป");
            },
            password(value) {
                return Validator.value(value)
                    .required("password")
                // .minLength(6, "รหัสผ่านต้องมีมากกว่า 6 ตัวขึ้นไป");
            },
            password2(value) {
                return Validator.value(value)
                    .required("password2")
                    .match(this.password, 'รหัสผ่านไม่ตรงกัน')
            }
        },
        methods: {
            addState() {
                if (this.state == 0) {
                    this.$validate(['firstname', 'lastname', 'sex', 'houseNumber', 'street', 'city', 'postalCode', 'dob', 'phone'])
                    if (
                        this.validation.firstError('firstname') == null &&
                        this.validation.firstError('lastname') == null &&
                        this.validation.firstError('sex') == null &&
                        this.validation.firstError('houseNumber') == null &&
                        this.validation.firstError('street') == null &&
                        this.validation.firstError('city') == null &&
                        this.validation.firstError('postalCode') == null &&
                        this.validation.firstError('dob') == null &&
                        this.validation.firstError('phone') == null
                    ) {
                        this.state++
                    }
                } else if (this.state == 1) {
                    this.$validate(['email', 'username', 'password', 'password2'])
                    if (
                        this.validation.firstError('email') == null &&
                        this.validation.firstError('username') == null &&
                        this.validation.firstError('password') == null &&
                        this.validation.firstError('password2') == null
                    ) {
                        this.registered()
                    }
                }
            },
            registered() {
                const payload = {
                    email: this.email,
                    password: this.password,
                    username: this.username,
                    firstname: this.firstname,
                    lastname: this.lastname,
                    phone: this.phone,
                    dob: this.dob,
                    sex: this.sex,
                    address: {
                        house_number: this.houseNumber,
                        street: this.street,
                        city: this.city,
                        postalCode: this.postalCode
                    }
                };
                const payloa = {
                    email: "60050@kmitl.ac.th",
                    password: "ning123456",
                    username: "ningNongz",
                    firstname: "woranan",
                    lastname: "buathong",
                    phone: "0895652189",
                    dob: "2012-12-12",
                    sex: "Male",
                    address: {
                        house_number: "45/9 village 1",
                        street: "xxx road, green building",
                        city: "Berlin",
                        postalCode: "12021"
                    }
                };
                console.log(payloa)
                console.log(payload)
                axios.post(this.$store.state.endpoints.registerUrL, payload)
                    .then((response) => {
                        console.log(response.data);
                        this.$router.push({
                            name: "login"
                        })
                    })
                    .catch((error) => {
                        console.log(error);
                        alert(error.message);
                    })
            }
        },
    }
</script>

<style scoped>
    input {
        border-radius: 0;
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
    }

    .el-input--suffix .el-input__inner {
        padding-right: 30px;
        border-radius: 0px;
    }
</style>