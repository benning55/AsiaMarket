<template>
    <div class="">
        <div class="relative">
            <img class="absolute" style="width: 28%;top: 18%;left: 18%;z-index: 1;max-width: 290px"
                 src="../assets/png/boat.png"
                 alt="boat">
            <img class="absolute" style="width: 32%;top: 10%;left: 61%;z-index: 1;max-width: 350px;-webkit-transform: scaleX(-1);
  transform: scaleX(-1);" src="../assets/png/boat.png"
                 alt="boat">
            <svg class="absolute" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
                <path fill="#ffffff" fill-opacity="1"
                      d="M0,192L48,181.3C96,171,192,149,288,149.3C384,149,480,171,576,186.7C672,203,768,213,864,197.3C960,181,1056,139,1152,133.3C1248,128,1344,160,1392,176L1440,192L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
            </svg>
            <svg class="" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
                <path fill="#EFF0EF" fill-opacity="1"
                      d="M0,224L48,218.7C96,213,192,203,288,181.3C384,160,480,128,576,122.7C672,117,768,139,864,165.3C960,192,1056,224,1152,234.7C1248,245,1344,235,1392,229.3L1440,224L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
            </svg>
        </div>
        <div class="bg-white flex flex-wrap mx-auto px-10 sm:px-16 md:px-40 lg:px-56 xl:px-64 pb-10">
            <div class="h-32 w-full sm:w-1/2 lg:w-1/4 pb-5 relative">
                <div class="center" style="font-size: 22px">ThaiMarket Express</div>
            </div>
            <div class=" w-full sm:w-1/2 lg:w-1/4 pb-5 ">
                <div class="">
                    <h1 class="text-xl mb-3">{{$t('contact_us')}}</h1>
                    <p v-if="footerData[1].phone!=null"><i class="fas fa-phone-alt"></i>{{footerData[1].phone}}</p>
                    <p v-if="footerData[2].phone!=''"><i class="fas fa-phone-alt"></i>{{footerData[2].phone}}</p>
                    <p v-if="footerData[1].email!=null"><i class="fas fa-envelope"></i>{{footerData[1].email}}</p>
                    <p v-if="footerData[2].email!=null"><i class="fas fa-envelope"></i>{{footerData[2].email}}</p>
                </div>
            </div>
            <div class="py-10 w-full sm:w-1/2 lg:w-1/4 ">
                <div class="flex pr-2 ">
                    <i class="fas fa-map-marker-alt"></i>
                    <p>{{footerData[1].address}}</p>
                </div>
            </div>
            <div class=" w-full sm:w-1/2 lg:w-1/4 ">
                <div class="">
                    <h1 class="text-xl mb-3">{{$t('help')}}</h1>
                    <p>{{$t('how_to_order')}}</p>
                    <p>{{$t('how_to_payment')}}</p>
                    <p>{{$t('how_to_manage_address')}}</p>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import axios from "axios";

    export default {
        data() {
            return {
                footerData: [
                    {
                        phone: "",
                        email: ''
                    },
                    {
                        phone: "",
                        email: ''
                    }
                ]
            }
        },
        created() {
            this.getFooterData()
        },
        methods: {
            getFooterData() {
                axios.get(`${this.$store.state.endpoints.host}/api/footer/`).then(res => {
                    this.footerData = res.data.data
                    console.log(this.footerData)
                    this.isLoading = false
                }).catch(e => {
                    this.$message.error(this.$t('error_Oops_') + e.status + ', at load recommend');
                })
            }
        }
    }
</script>

<style scoped>
    i {
        margin-right: 5px;
    }

    .vertical-center {
        margin: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .vertical-centerx {
        margin: 0;
        position: absolute;
        left: 50%;
        -ms-transform: translateX(-50%);
        transform: translateX(-50%);
    }

    .center {
        margin: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
    }
</style>