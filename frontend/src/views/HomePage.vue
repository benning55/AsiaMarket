<template>
    <div>
        <Loader v-if="isLoading"/>
        <NavbarSpace/>

        <Carousel/>

        <div class="mt-3 w-full hidden sm:block md:block lg:hidden">
            <swiper :options="swiperOption">
                <swiper-slide v-for="category in categorys" :key="category.key">
                    <button @click="goCategory(category)"
                            class="w-full bg-white cs-border-2 hover:bg-unHilight text-black p-2 h-full text-center"
                            style="height: 48px;" >
                        <div>
                              {{nameTranslate(category.type)}}
<!--                            <hr class="w-full text-lightGray" style="border-top-width:2.5px"-->
<!--                            :style="`color:${category.color}`">-->
                        </div>
                    </button>
                </swiper-slide>
            </swiper>
        </div>

        <section class="mt-3">
            <div class="flex justify-between">
                <h1 class="ml-2 lg:ml-0 my-3 text-xl">{{$t('recommend')}}</h1>
                <router-link :to="{ name: 'Category', params: { id: 'recommend' }}">
                    <h1 class="mr-2 lg:mr-0 my-3 text-md self-center text-gray">{{$t('see_more')}} ></h1>
                </router-link>
            </div>
            <SwiperItem :dataItem="recommendProduct"/>
        </section>

        <section class="mt-3">
            <div class="flex justify-between">
                <h1 class="ml-2 lg:ml-0 my-3 text-xl">{{$t('new_product')}}</h1>
                <router-link :to="{ name: 'Category', params: { id: 'new-product' }}">
                    <h1 class="mr-2 lg:mr-0 my-3 text-md self-center text-gray">
                        {{$t('see_more')}} >
                    </h1>
                </router-link>

            </div>
            <SwiperItem :dataItem="newestProduct"/>
        </section>
    </div>
</template>

<script>
    import 'vue-slick-carousel/dist/vue-slick-carousel.css'
    import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
    import axios from 'axios'
    import SwiperItem from "../components/SwiperItem";
    import Carousel from '../components/Carousel'
    import Loader from "../components/Loader";
    import NavbarSpace from "../components/NavbarSpace";

    export default {
        name: 'MyComponent',
        components: { SwiperItem, Loader, Carousel, NavbarSpace},
        data() {
            return {
                swiperOption: {
                    slidesPerView: 5,
                    pagination: {
                        el: '.swiper-pagination',
                        clickable: true
                    },
                    breakpoints: {
                        1400: {
                            slidesPerView: 4,
                        },
                        1024: {
                            slidesPerView: 4,
                        },
                        640: {
                            slidesPerView: 3,
                        },
                        480: {
                            slidesPerView: 2,
                        }
                    }
                },
                categorys: [],
                recommendProduct: [],
                newestProduct: [],
                isLoading: true,
                loadStatus:[],
                carousel: '',

            }
        },
        created() {
            this.getCategory()
            axios.get(this.$store.state.endpoints.recommendProduct).then(res => {
                this.recommendProduct = res.data.data.slice(0, 8)
                // this.isLoading = false
                this.loadStatus.push('done')
            }).catch(e => {
                this.$message.error(this.$t('error_Oops_') + e.response.status + ', at load recommend');
            })
            axios.get(this.$store.state.endpoints.newestProduct).then(res => {
                this.newestProduct = res.data.data.slice(0, 8)
                // this.isLoading = false
                this.loadStatus.push('done')
            }).catch(e => {
                this.$message.error(this.$t('error_Oops_') + e.response.status + ', at load new Product');
            })
            window.scrollTo(0, 0);

        },
        methods: {
            getCategory() {
                axios.get(`${this.$store.state.endpoints.host}/api/products/category/`).then(res => {
                    // console.log(res.data.data)
                    this.categorys = res.data.data
                    // this.isLoading = false
                }).catch(e => {
                    this.$message.error(this.$t('error_Oops_') + e.response.status + ', at load category');
                })
            },
            nameTranslate(text) {
                let list = text.split('|')
                if (list.length == 1) {
                    return text
                } else {
                    if (this.$i18n.locale == 'th') {
                        return list[1]
                    } else {
                        return list[0]
                    }
                }
            },
            goCategory(category) {
                this.$router.push({
                    name: 'Category',
                    params: {id: category.id}
                })
            }
        },
        watch:{
            loadStatus(){
                if(this.loadStatus.length >= 2){
                    this.isLoading = false
                }
            }
        }
    }
</script>

<style>
    .slick-dots {
        position: absolute;
        bottom: 10px;
        width: 100%;
        padding: 0;
        margin: 0;
        list-style: none;
        text-align: center;
        color: white;
    }

    .slick-dots li.slick-active button:before {
        opacity: 1;
        color: white;
    }

    .slick-dots li button:before {
        opacity: 0.5;
        color: white;
    }

    .slick-next {
        right: 15px;
    }

    .slick-prev {
        left: 15px;
        z-index: 3;
    }

    .cs-border-2 {
        /*border: 3px solid #e3e4e3;*/
        /*border-style: none solid none none*/
        -webkit-box-shadow: inset -1.5px 0px 0px 0px #e3e4e3;
        -moz-box-shadow: inset -1.5px 0px 0px 0px #e3e4e3;
        box-shadow: inset -1.5px 0px 0px 0px #e3e4e3;
    }

    .w-25-per {
        width: 25%;
    }
</style>