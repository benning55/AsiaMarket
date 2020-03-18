<template>
    <div>
        <Loader v-if="isLoading"/>
        <NavbarSpace/>

        <Carousel/>

        <div class="mt-3 w-full">
            <swiper :options="swiperOption">
                <swiper-slide v-for="category in categorys" :key="category.key">
                    <button @click="goCategory(category)"
                            class="w-full bg-white cs-border-2 hover:bg-unHilight text-black py-2 h-full text-center"
                            style="height: 48px">
                        {{nameTranslate(category.type)}}
                    </button>
                </swiper-slide>
            </swiper>
        </div>

        <section class="mt-3">
            <div class="flex justify-between">
                <h1 class="ml-2 lg:ml-0 my-3 text-xl">{{$t('recommend')}}</h1>
                <router-link :to="{ name: 'Category', params: { id: 'new-product' }}">
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
    import VueSlickCarousel from 'vue-slick-carousel'
    import 'vue-slick-carousel/dist/vue-slick-carousel.css'
    import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
    import axios from 'axios'
    import SwiperItem from "../components/SwiperItem";
    import Carousel from '../components/Carousel'
    import Loader from "../components/Loader";
    import NavbarSpace from "../components/NavbarSpace";

    export default {
        name: 'MyComponent',
        components: {VueSlickCarousel, SwiperItem, Loader, Carousel,NavbarSpace},
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
                categorys: [
                    {id: 1, type: "Fruits and Vegetables(ผักและผลไม้)", color: "green"},
                    {id: 2, type: "Dry goods and Seasonings(ของแห้งและเครื่องปรุงรส)", color: "blue"},
                    {id: 3, type: "Rice Flour and Noodles( แป้งและเส้น)", color: "yellow"},
                    {id: 4, type: "Condiments and Sauces(เครื่องปรุงรสและซอส)", color: "red"},
                    {id: 5, type: "Normal and Alcoholic Beverages(เครื่องดื่มและแอลกอฮอล์)", color: "black"},
                    {id: 6, type: "Snack(ขนมขบเคี้ยว)", color: "orange"},
                    {id: 7, type: "Frozen Products(อาหารแช่แข็ง)", color: "purple"},
                    {id: 8, type: "Other(อื่น ๆ)", color: "pink"},
                ],
                recommendProduct: [],
                newestProduct: [],
                isLoading: true,
                carousel: ''
            }
        },
        created() {
            axios.get(this.$store.state.endpoints.recommendProduct).then(res => {
                this.recommendProduct = res.data.data.slice(0, 8)
                this.isLoading = false
            }).catch(e => {
                this.$message.error(this.$t('error_Oops_') + e.response.status + ', at load recommend');
            })
            axios.get(this.$store.state.endpoints.newestProduct).then(res => {
                this.newestProduct = res.data.data.slice(0, 8)
                this.isLoading = false
            }).catch(e => {
                this.$message.error(this.$t('error_Oops_') + e.response.status + ', at load new Product');
            })

        },
        methods: {
            nameTranslate(text) {
                let list = text.split(')').join('(').split('(')
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