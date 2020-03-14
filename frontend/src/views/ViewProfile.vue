<template>
    <div class="md:mx-24 sm:mx-0 lg:mx-0 xl:mx-0">
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <div v-if="!$store.state.isAuthenticated"
             class="bg-white w-full border-green-top px-4 lg:px-20 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16 h-64 relative">
            <NoLoginText/>
        </div>
        <div v-else
             class="bg-white w-full border-green-top px-4 sm:h-full lg:px-20 pb-16 mx-auto sm:mt-16 lg:mt-16 xl:mt-16">
            <div class="text-center text-2xl mb-10 mt-5 font-l">Profile</div>
            <div class="flex-none sm:flex justify-between mb-5">
                <h1 class="text-xl font-l text-gray">Email</h1>
                <h1 class="text-xl">{{this.$store.state.authUser.user.email}}</h1>
            </div>
            <div class="flex-none sm:flex justify-between mb-5">
                <h1 class="text-xl font-l text-gray">Firstname</h1>
                <div v-if="!isEditFirstname" class="md:flex lg:flex xl:flex relative">
                    <h1 class="text-xl">{{this.$store.state.authUser.user.first_name}}</h1>
                    <h1 @click="isEditFirstname = !isEditFirstname"
                        class="hidden sm:block text-sm text-right text-orange self-center ml-2">Edit</h1>
                    <h1 @click="isEditFirstname = !isEditFirstname"
                        class="block sm:hidden text-sm text-right text-orange self-center ml-2"
                        style="position: absolute;top: -9px;right: 15px;">Edit</h1>
                </div>
                <div v-else class="flex">
                    <el-input placeholder="Please input" v-model="newFirstname"></el-input>
                    <div v-if="!validation.firstError('newFirstname')" @click="editFirstname(newFirstname)"
                         class="w-12 bg-green rounded-lg ml-1 text-center">
                        <i class="fas fa-check text-white" style="padding: 12px;"></i>
                    </div>
                    <div v-else @click="isEditFirstname = !isEditFirstname"
                         class="w-12 bg-red rounded-lg ml-1 text-center">
                        <i class="material-icons text-white" style="padding: 8px;">clear</i>
                    </div>
                </div>
            </div>
            <div class="flex-none sm:flex justify-between mb-5">
                <h1 class="text-xl font-l text-gray">Lastname</h1>
                <div v-if="!isEditLastname" class="md:flex lg:flex xl:flex relative">
                    <h1 class="text-xl">{{this.$store.state.authUser.user.last_name}}</h1>
                    <h1 @click="isEditLastname = !isEditLastname"
                        class="hidden sm:block text-sm text-right text-orange self-center ml-2">Edit</h1>
                    <h1 @click="isEditLastname = !isEditLastname"
                        class="block sm:hidden text-sm text-right text-orange self-center ml-2"
                        style="position: absolute;top: -9px;right: 15px;">Edit</h1>
                </div>
                <div v-else class="flex">
                    <el-input placeholder="Please input" v-model="newLastname"></el-input>
                    <div v-if="!validation.firstError('newLastname')" @click="editLastname(newLastname)"
                         class="w-12 bg-green rounded-lg ml-1 text-center">
                        <i class="fas fa-check text-white text-center " style="padding: 12px;"></i>
                    </div>
                    <div v-else @click="isEditLastname = !isEditLastname"
                         class="w-12 bg-red rounded-lg ml-1 text-center">
                        <i class="material-icons text-white text-center" style="padding: 8px;">
                            clear
                        </i>
                    </div>
                </div>
            </div>
            <div class="flex-none sm:flex justify-between mb-5">
                <h1 class="text-xl font-l text-gray">Phone Number</h1>
                <div v-if="!isEditPhone" class="md:flex lg:flex xl:flex relative">
                    <h1 class="text-xl">{{this.$store.state.authUser.profile.tel}}</h1>
                    <h1 @click="isEditPhone = !isEditPhone"
                        class="hidden sm:block text-sm text-right text-orange self-center ml-2">
                        Edit</h1>
                    <h1 @click="isEditPhone = !isEditPhone"
                        class="block sm:hidden text-sm text-right text-orange self-center ml-2"
                        style="position: absolute;top: -9px;right: 15px;">Edit</h1>
                </div>
                <div v-else class="flex">
                    <el-input placeholder="Please input" v-model="newPhone" class="text-3xl"></el-input>
                    <div v-if="!validation.firstError('newPhone')" @click="editPhone(newPhone)"
                         class="w-12 bg-green rounded-lg ml-1 text-center">
                        <i class="fas fa-check text-white" style="padding: 12px;"></i>
                    </div>
                    <div v-else @click="isEditPhone = !isEditPhone" class="w-12 bg-red rounded-lg ml-1 text-center">
                        <i class="material-icons text-white text-center" style="padding: 8px;">
                            clear
                        </i>
                    </div>
                </div>
            </div>
            <div class="flex-none sm:flex justify-between mb-5">
                <h1 class="text-xl font-l text-gray">Date of Birth</h1>
                <div v-if="!isEditDOB" class="md:flex lg:flex xl:flex relative">
                    <h1 class="text-xl">{{this.$store.state.authUser.profile.dob}}</h1>
                    <h1 @click="isEditDOB = !isEditDOB"
                        class="hidden sm:block text-sm text-right text-orange self-center ml-2">
                        Edit</h1>
                    <h1 @click="isEditDOB = !isEditDOB"
                        class="block sm:hidden text-sm text-right text-orange self-center ml-2"
                        style="position: absolute;top: -9px;right: 15px;">Edit</h1>
                </div>
                <div v-else class="flex">
                    <el-date-picker
                            style="width: 100%;border-radius: 0px"
                            v-model="newDOB"
                            type="date"
                            placeholder="Pick a date"
                            default-value="2000-01-01"
                            format="yyyy-MM-dd"
                            value-format="yyyy-MM-dd">
                    </el-date-picker>
                    <div v-if="!validation.firstError('newDOB')" @click="editDOB(newDOB)"
                         class="w-12 bg-green rounded-lg ml-1 text-center">
                        <i class="fas fa-check text-white text-center" style="padding: 12px;"></i>
                    </div>
                    <div v-else @click="isEditDOB = !isEditDOB" class="w-12 bg-red rounded-lg ml-1 text-center"
                         style="padding-left: 3px ;padding-top: 3px;">
                        <i class="material-icons text-white text-center" style="padding: 8px;">
                            clear
                        </i>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {Validator} from "../main";
    import axios from "axios";
    import NoLoginText from "../components/NoLoginText";

    export default {
        components: {
            NoLoginText
        },
        data() {
            return {
                newFirstname: '',
                newLastname: '',
                newPhone: '',
                newDOB: '',
                isEditFirstname: false,
                isEditLastname: false,
                isEditPhone: false,
                isEditDOB: false,
                userData: {}
            }
        },
        validators: {
            newFirstname(value) {
                return Validator.value(value)
                    .required("กรุณาใส่อีเมลล์");
            },
            newLastname(value) {
                return Validator.value(value)
                    .required("กรุณาใส่รหัสผ่าน")
            },
            newPhone(value) {
                return Validator.value(value)
                    .required("กรุณาใส่รหัสผ่าน").digit().minLength(10, 'must more than 10 digit').maxLength(12, 'must less than 13 digit')
            },
            newDOB(value) {
                return Validator.value(value)
                    .required("กรุณาใส่รหัสผ่าน")
            },
            mockupData(value) {
                return Validator.value(value)
                    .required("กรุณาใส่รหัสผ่าน")
            }
        },
        created() {
            this.loadUserData()
        },
        methods: {
            loadUserData() {
                this.userData = {
                    firstname: this.$store.state.authUser.user.first_name,
                    lastname: this.$store.state.authUser.user.last_name,
                    email: this.$store.state.authUser.user.email,
                    phone: this.$store.state.authUser.profile.tel,
                    dob: this.$store.state.authUser.profile.dob
                }
                this.equal()
            },
            equal() {
                this.newFirstname = this.userData.firstname
                this.newLastname = this.userData.lastname
                this.newPhone = this.userData.phone
                this.newDOB = this.userData.dob
            },
            editFirstname(firstname) {
                axios.put(this.$store.state.endpoints.host + '/api/accounts/user/', {
                    tel: this.$store.state.authUser.profile.tel,
                    dob: this.$store.state.authUser.profile.dob,
                    email: this.$store.state.authUser.user.email,
                    first_name: firstname,
                    last_name: this.$store.state.authUser.user.last_name
                }, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                }).then(() => {
                    this.$store.commit("setNewFirstname", firstname);
                    this.isEditFirstname = false
                }).catch(e => {
                    this.$message.error('Oops, Something is Error. code ' + e.status + ', at edit Edit Firstname');
                    this.isEditFirstname = false
                })
            },
            editLastname(lastname) {
                this.userData.lastname = lastname
                this.equal()
                this.isEditLastname = false

                axios.put(this.$store.state.endpoints.host + '/api/accounts/user/', {
                    tel: this.$store.state.authUser.profile.tel,
                    dob: this.$store.state.authUser.profile.dob,
                    email: this.$store.state.authUser.user.email,
                    first_name: this.$store.state.authUser.user.first_name,
                    last_name: lastname
                }, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                }).then(() => {
                    this.$store.commit("setNewLastname", lastname);
                    this.isEditLastname = false
                }).catch(e => {
                    this.$message.error('Oops, Something is Error. code ' + e.status + ', at edit lastname');
                    this.isEditLastname = false
                })
            },
            editPhone(phone) {
                axios.put(this.$store.state.endpoints.host + '/api/accounts/profile/', {
                    user_id: this.$store.state.authUser.user.id,
                    tel: phone
                }, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                }).then(() => {
                    this.$store.commit("setNewTel", phone);
                    this.isEditPhone = false
                }).catch(e => {
                    this.$message.error('Oops, Something is Error. code ' + e.status + ', at edit phone');
                    this.isEditPhone = false
                })
            },
            editDOB(dob) {
                axios.put(this.$store.state.endpoints.host + '/api/accounts/profile/', {
                    user_id: this.$store.state.authUser.user.id,
                    tel: dob
                }, {
                    headers: {
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                }).then(() => {
                    this.$store.commit("setNewDOB", dob);
                    this.isEditDOB = false
                }).catch(e => {
                    this.$message.error('Oops, Something is Error. code ' + e.status + ', at edit Date of Barth');
                    this.isEditDOB = false
                })
            }
        }
    }
</script>

<style scoped>
    .el-input__inner {
        border-radius: 8px 0px 0px 8px;
    }
</style>