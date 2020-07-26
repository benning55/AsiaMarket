<template>
    <div>
        <Loader v-if="isLoading"/>
        <NavbarSpace/>
        <div class="auth">
            <form class="mt-16 w-11/12 sm:w-4/5 md:w-3/5 lg:w-4/5 xl:w-2/3 mx-auto bg-white shadow-md px-8 pt-6 pb-8 mb-4"
                  style="border-top: 6px solid #619F21;">
                <h1 class="text-3xl font-hairline text-center mb-5">{{$t('register')}}</h1>
                <div v-if="state == 0">
                    <div class="flex flex-wrap sm:px-10 md:px-16 lg:px-8">
                        <div class="mb-4 pr-2 w-1/2">
                            <label v-if="!validation.firstError('firstname')"
                                   class="block text-sm mb-2"
                                   for="firstname">{{$t('firstname')}}</label>
                            <label v-else
                                   class="block text-red text-sm mb-2"
                                   for="firstname">{{$t(validation.firstError('firstname'))}}</label>
                            <el-input id="firstname"
                                      ref="firstname"
                                      @keyup.enter.native="$refs.lastname.focus"
                                      placeholder="Please input"
                                      v-model="firstname">
                            </el-input>
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <label v-if="!validation.firstError('lastname')"
                                   class="block text-sm mb-2"
                                   for="lastname">{{$t('lastname')}}</label>
                            <label v-else class="block text-red text-sm mb-2"
                                   for="lastname">{{$t(validation.firstError('lastname'))}}</label>
                            <el-input id="lastname"
                                      ref="lastname"
                                      @keyup.enter.native="$refs.houseNumber.focus"
                                      placeholder="Please input"
                                      v-model="lastname">
                            </el-input>
                        </div>
                    </div>

                    <div class="mb-6 sm:px-10 md:px-16 lg:px-16 w-full text-center ">
                        <label v-if="!validation.firstError('sex')"
                               class="block text-sm mb-2 text-left"
                               for="sex">{{$t('select_gender')}}</label>
                        <label v-else
                               class="block text-red text-sm mb-2 text-left"
                               for="sex">{{$t(validation.firstError('sex'))}}</label>
                        <el-radio-group id="sex" v-model="sex" style="border-radius: 0px">
                            <el-radio-button label="Male">{{$t('male')}}</el-radio-button>
                            <el-radio-button label="Female">{{$t('female')}}</el-radio-button>
                            <!--                            <el-radio-button label="LTGB">{{$t('ltgb')}}</el-radio-button>-->
                        </el-radio-group>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-8 w-full">
                        <label v-if="!validation.firstError('houseNumber')"
                               class="block text-sm mb-2"
                               for="houseNumber">{{$t('Street_&_House_Number')}}</label>
                        <label v-else
                               class="block text-red text-sm mb-2"
                               for="houseNumber">{{$t(validation.firstError('houseNumber'))}}</label>
                        <el-input id="houseNumber"
                                  ref="houseNumber"
                                  @keyup.enter.native="$refs.street.focus"
                                  placeholder="Please input"
                                  v-model="houseNumber">
                        </el-input>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-8 w-full">
                        <label v-if="!validation.firstError('street')"
                               class="block text-sm mb-2"
                               for="houseNumber">{{$t('city')}}</label>
                        <label v-else class="block text-sm mb-2 text-red"
                               for="street">{{$t(validation.firstError('street'))}}</label>
                        <el-input id="street"
                                  ref="street"
                                  @keyup.enter.native="$refs.city.focus"
                                  placeholder="Please input"
                                  v-model="street">
                        </el-input>
                    </div>
                    <div class="flex flex-wrap sm:px-10 md:px-16 lg:px-8">
                        <div class="mb-4 pr-2 w-1/2">
                            <label v-if="!validation.firstError('city')"
                                   class="block text-sm mb-2">{{$t('state')}}</label>
                            <label v-else
                                   class="block text-red text-sm mb-2">{{$t(validation.firstError('city'))}}</label>
                            <!--                            <el-select v-model="city" ref="city" placeholder="Select">-->
                            <!--                                <el-option-->
                            <!--                                        v-for="item in cityOptions"-->
                            <!--                                        :key="item"-->
                            <!--                                        :label="item"-->
                            <!--                                        :value="item">-->
                            <!--                                </el-option>-->
                            <!--                            </el-select>-->
                            <el-input id="city"
                                      ref="city"
                                      @keyup.enter.native="$refs.city.focus"
                                      placeholder="Please input"
                                      v-model="city">
                            </el-input>
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <label v-if="!validation.firstError('postalCode')"
                                   class="block text-sm mb-2"
                                   for="postal">{{$t('postal')}}</label>
                            <label v-else
                                   class="block text-red text-sm mb-2"
                                   for="postal">{{$t(validation.firstError('postalCode'))}}</label>
                            <el-input id="postal"
                                      ref="postal"
                                      @keyup.enter.native="$refs.dob.focus"
                                      placeholder="Please input"
                                      v-model="postalCode">
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
                    <div class="flex flex-wrap sm:px-10 md:px-16 lg:px-8">
                        <div class="mb-4 pr-2 w-1/2">
                            <label v-if="!validation.firstError('dob')"
                                   class="block text-sm mb-2">{{$t('date_of_birth')}}</label>
                            <label v-else
                                   class="block text-red text-sm mb-2">{{$t(validation.firstError('dob'))}}</label>
                            <el-date-picker
                                    ref="dob"
                                    @keyup.enter.native="$refs.phone.focus"
                                    style="width: 100%;border-radius: 0px"
                                    v-model="dob"
                                    type="date"
                                    placeholder="Pick a date"
                                    :picker-options="pickerOptions"
                                    :editable="false"
                                    format="dd MMMM yyyy"
                                    value-format="yyyy-MM-dd">
                            </el-date-picker>
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <label v-if="!validation.firstError('phone')"
                                   class="block text-sm mb-2"
                                   for="phone">{{$t('phone_number')}}</label>
                            <label v-else
                                   class="block text-red text-sm mb-2"
                                   for="phone">{{$t(validation.firstError('phone'))}}</label>
                            <el-input id="phone"
                                      ref="phone"
                                      @keyup.enter.native="addState"
                                      placeholder="Please input"
                                      type="number"
                                      v-model="phone">
                            </el-input>
                        </div>
                    </div>
                    <div class="flex flex-wrap sm:px-10 md:px-16 lg:px-8">
                        <div class="mb-4 w-1/2">
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <button @click="addState()"
                                    class="w-full bg-green text-white text-center py-2 focus:outline-none"
                                    type="button">{{$t('next')}}
                            </button>
                        </div>
                    </div>
                </div>
                <div v-if="state == 1">
                    <div class="mb-4 sm:px-10 md:px-16 lg:px-8 w-full">
                        <el-alert v-if="error" type="error" show-icon @close="closeError">
                            {{$t(error)}}
                        </el-alert>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-8 w-full">
                        <label v-if="!validation.firstError('email')"
                               class="block text-sm mb-2"
                               for="email">{{$t('email')}}</label>
                        <label v-else
                               class="block text-red text-sm mb-2"
                               for="email">{{$t(validation.firstError('email'))}}</label>
                        <el-input id="email"
                                  ref="email"
                                  @keyup.enter.native="$refs.facebook.focus"
                                  placeholder="Please input"
                                  v-model="email">
                        </el-input>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-8 w-full">
                        <label v-if="!validation.firstError('facebook')"
                               class="block text-sm mb-2"
                               for="facebook">{{$t('facebook')}}</label>
                        <label v-else
                               class="block text-red text-sm mb-2"
                               for="facebook">{{$t(validation.firstError('facebook'))}}</label>
                        <el-input id="facebook"
                                  auto-complete="false"
                                  ref="facebook"
                                  @keyup.enter.native="$refs.password.focus"
                                  placeholder="Please input"
                                  v-model="facebook">
                        </el-input>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-8 w-full">
                        <label v-if="!validation.firstError('password')"
                               class="block text-sm mb-2"
                               for="password">{{$t('password')}}</label>
                        <label v-else
                               class="block text-red text-sm mb-2"
                               for="password">{{$t(validation.firstError('password'))}}</label>
                        <el-input id="password"
                                  ref="password"
                                  @keyup.enter.native="$refs.password2.focus"
                                  placeholder="Please input"
                                  v-model="password"
                                  show-password>
                        </el-input>
                    </div>
                    <div class="mb-6 sm:px-10 md:px-16 lg:px-8 w-full">
                        <label v-if="!validation.firstError('password2')"
                               class="block text-sm mb-2"
                               for="password2">{{$t('repassword')}}</label>
                        <label v-else
                               class="block text-red text-sm mb-2"
                               for="password2">{{$t(validation.firstError('password2'))}}</label>
                        <el-input id="password2"
                                  ref="password2"
                                  @keyup.enter.native="addState()"
                                  placeholder="Please input"
                                  v-model="password2"
                                  show-password>
                        </el-input>
                    </div>
                    <div class="flex justify-between sm:px-10 md:px-8 lg:px-8">
                        <div class="mb-4 pr-2 w-1/3">
                            <button @click="state--"
                                    class="w-full bg-white text-black_p py-2 focus:outline-none flex justify-start"
                                    type="button">
                                <p class="inline-flex ml-0">
                                    <i class="material-icons">keyboard_arrow_left</i><span>{{$t('previous')}}</span>
                                </p>
                            </button>
                        </div>
                        <div class="mb-6 pl-2 w-1/2">
                            <button @click="addState()"
                                    class="w-full bg-green text-white text-center py-2 focus:outline-none "
                                    type="button">{{$t('register')}}
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
    import Loader from "../components/Loader";
    import NavbarSpace from "../components/NavbarSpace";

    export default {
        name: 'Register',
        components: {
            Loader,
            NavbarSpace
        },
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
                facebook: '',
                username: '',
                password: '',
                password2: '',
                state: 0,
                country:'',
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
                pickerOptions: {
                    disabledDate(time) {
                        return time.getTime() > Date.now();
                    },
                },
                error: '',
                isLoading: false
            }
        },
        validators: {
            firstname(value) {
                return Validator.value(value)
                    .required("error_profile_firstname_require");
            },
            lastname(value) {
                return Validator.value(value)
                    .required("error_profile_lastname_require")
            },
            sex(value) {
                return Validator.value(value)
                    .required("error_profile_gender_require")
            },
            houseNumber(value) {
                return Validator.value(value)
                    .required("Street_&_House_Number")
            },
            street(value) {
                return Validator.value(value)
                    .required("error_address_city")
            },
            city(value) {
                return Validator.value(value)
                    .required("error_address_state")
            },
            postalCode(value) {
                return Validator.value(value)
                    .required("error_address_postalCode_require")
                // .length(5, "error_address_postalCode_number")
            },
            country(value) {
                return Validator.value(value)
                    .required("error_address_county")
                // .length(5, "error_address_postalCode_number")
            },
            dob(value) {
                return Validator.value(value)
                    .required("error_profile_dob_require")
            },
            phone(value) {
                return Validator.value(value)
                    .required("error_profile_phone_require")
            },
            email(value) {
                return Validator.value(value)
                    .required("error_user_email_require")
                    .email('error_user_email_invalid')
            },
            facebook(value) {
                return Validator.value(value)
                    .required("error_user_facebook_require")
            },
            // username(value) {
            //     return Validator.value(value)
            //         .required("error_user_username_require")
            //         .minLength(4, "error_user_username_length");
            // },
            password(value) {
                return Validator.value(value)
                    .required("error_user_password_require")
                    .minLength(6, "error_user_password_length");
            },
            password2(value) {
                return Validator.value(value)
                    .required("error_user_repassword_require")
                    .match(this.password, 'error_user_repassword_not_match')
            }
        },
        methods: {
            addState() {
                if (this.state == 0) {
                    this.$validate(['firstname', 'lastname', 'sex', 'houseNumber', 'street', 'city', 'postalCode','country', 'dob', 'phone'])
                    if (
                        this.validation.firstError('firstname') == null &&
                        this.validation.firstError('lastname') == null &&
                        this.validation.firstError('sex') == null &&
                        this.validation.firstError('houseNumber') == null &&
                        this.validation.firstError('street') == null &&
                        this.validation.firstError('city') == null &&
                        this.validation.firstError('postalCode') == null &&
                        this.validation.firstError('country') == null &&
                        this.validation.firstError('dob') == null &&
                        this.validation.firstError('phone') == null
                    ) {
                        this.state++
                    }
                } else if (this.state == 1) {
                    this.$validate(['email', 'facebook', 'password', 'password2'])
                    if (
                        this.validation.firstError('email') == null &&
                        this.validation.firstError('facebook') == null &&
                        this.validation.firstError('password') == null &&
                        this.validation.firstError('password2') == null
                    ) {
                        this.registered()
                    }
                }
            },
            registered() {
                this.isLoading = true
                const payload = {
                    email: this.email,
                    facebook: this.facebook,
                    password: this.password,
                    username: this.email,
                    firstname: this.firstname,
                    lastname: this.lastname,
                    phone: this.phone,
                    dob: this.dob,
                    sex: this.sex,
                    address: {
                        address: this.houseNumber, // address
                        city: this.street, // city
                        state: this.city, // state
                        postalCode: this.postalCode,
                        country:this.country
                    }
                };
                axios.post(this.$store.state.endpoints.registerUrL, payload)
                    .then(() => {
                        this.isLoading = false
                        this.$router.push({
                            name: "login"
                        })
                    })
                    .catch((error) => {
                        this.isLoading = false
                        if (error.response.status == 400) {
                            if (error.response.data.error.user.password) {
                                this.error = 'error_user_password_alert_easy'
                            } else if (error.response.data.error.user.email) {
                                this.error = error.response.data.error.user.email[0]
                            } else if (error.response.data.error.user.username) {
                                this.error = error.response.data.error.user.username[0]
                            }
                        } else {
                            this.error = 'something_is_wrong_try_again_later'
                        }

                    })
            },
            closeError() {
                this.error = ''
            },
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