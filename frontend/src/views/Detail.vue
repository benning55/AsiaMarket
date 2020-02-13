<template>
    <div>
        <ul class="w-full py-6">
            <li class="inline-block px-5">LOGO</li>
        </ul>
        <section class="bg-white p-5 my-5">
            <a><span>Home</span> > {{dataProduct.category_name}} > {{dataProduct.title}}</a>
        </section>
        <section class="my-5 mb-10">
            <div class="flex-none sm:flex md:flex lg:flex xl:flex mb-4 bg-white">
                <div class="w-full sm:w-3/12 md:4/12 lg:4/12">
                    <VueSlickCarousel
                            ref="c1"
                            :asNavFor="$refs.c2"
                            :focusOnSelect="true"
                            :dots="false"
                            :arrows="false">
                        <div v-for="img in mockup.detail.data.image" :key="img.id" class="w-full p-10 md:p-5">
                            <img :src="img" alt="s">
                        </div>
                        <div v-for="img in mockup.detail.data.image" :key="img.id"><img :src="img"/></div>
                    </VueSlickCarousel>
                    <div class="px-5">
                        <VueSlickCarousel
                                ref="c2"
                                :asNavFor="$refs.c1"
                                :slidesToShow="3"
                                :focusOnSelect="true"
                                :arrows="true">
                            <div v-for="img in mockup.detail.data.image" :key="img.id" class="11/12 p-2">
                                <img :src="img" alt="s">
                            </div>
                        </VueSlickCarousel>
                    </div>
                </div>
                <div class="w-full sm:w-5/12 md:5/12 lg:md:5/12 px-10 pt-12">
                    <h1 class="text-3xl">{{dataProduct.title}}</h1>
                    <h1 class="text-lightGray">unit</h1>
                    <p class="mt-10"> {{dataProduct.description}}</p>
                </div>
                <div class="w-full sm:w-4/12 px-10 pt-12">
                    <h1 class="text-4xl">{{dataProduct.price}} $</h1>
                    <div @mouseover="hover = true"
                         @mouseleave="hover = false"
                         v-if="hover"
                         class="button-area flex justify-between">
                        <div class="button-increase  bg-green">
                            <i class="material-icons">remove</i>
                        </div>
                        <div class="text-2xl">2</div>
                        <div class="button-decrease bg-green">
                            <i class="material-icons">add</i>
                        </div>
                    </div>
                    <div @mouseover="hover = true"
                         @mouseleave="hover = false"
                         v-if="!hover"
                         class="button-area flex justify-between" style="border: 1.5px solid #707070">
                        <div class="text-xl" style="margin: auto">Add</div>
                    </div>
                    <h1 class="text-lightGray my-5">{{dataProduct.quantity}} Left</h1>
                </div>
            </div>
        </section>

        <section class="mt-3">
            <h1 class="mb-2 text-xl">You may also like</h1>
            <SwiperItem :dataItem="recommendProduct"/>
        </section>


    </div>
</template>

<script>
    import VueSlickCarousel from 'vue-slick-carousel'
    import 'vue-slick-carousel/dist/vue-slick-carousel.css'
    import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
    // import ProductCard from "../components/ProductCard";
    import axios from "axios";
    import SwiperItem from "../components/SwiperItem";

    export default {
        name: 'Detail',
        components: {
            VueSlickCarousel,
            // ProductCard,
            SwiperItem
        },
        data() {
            return {
                mockup: {
                    detail: {
                        data: {
                            "id": 0,
                            "category_id": 0,
                            "title": "apple",
                            "image": [
                                "https://charliesfruitonline.com.au/wp-content/uploads/2014/03/green-cabbage.jpg",
                                "https://charliesfruitonline.com.au/wp-content/uploads/2014/03/green-cabbage.jpg",
                                "https://charliesfruitonline.com.au/wp-content/uploads/2014/03/green-cabbage.jpg",
                                "https://charliesfruitonline.com.au/wp-content/uploads/2014/03/green-cabbage.jpg"
                            ],
                            "description": "this is apple",
                            "price": "10.00",
                            "quantity": 12
                        }
                    }
                },
                setting3: {
                    "dots": false,
                    "infinite": false,
                    "initialSlide": 3,
                    "speed": 500,
                    "slidesToShow": 5,
                    "slidesToScroll": 1,
                    "arrows": false,
                    "swipeToSlide": true,
                    "responsive": [
                        {
                            "breakpoint": 1400,
                            "settings": {
                                "slidesToShow": 4,
                            }
                        },
                        {
                            "breakpoint": 1024,
                            "settings": {
                                "slidesToShow": 4,
                            }
                        },
                        {
                            "breakpoint": 600,
                            "settings": {
                                "slidesToShow": 3,
                            }
                        },
                        {
                            "breakpoint": 480,
                            "settings": {
                                "slidesToShow": 2,
                            }
                        }
                    ]
                },
                hover: false,
                recommendProduct: [],
                dataProduct: [],
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
                }
            }
        },
        created() {
            axios.get(this.$store.state.endpoints.productUrL + this.$route.params.id + "/").then(res => {
                this.dataProduct = res.data.data
            }).catch()
            axios.get(this.$store.state.endpoints.recommendProduct).then(res => {
                this.recommendProduct = res.data.data.slice(0, 8)
            }).catch()
        }
    }
</script>

<style scoped>
    .button-area {
        border: 1.5px solid #619F21;
        width: 100%;
        height: 40px;
    }

    .button-increase {
        color: white;
        font-size: 23px;
        text-align: center;
        width: 36px;
        height: 37px;
        padding-top: 5px;
    }

    .button-decrease {
        color: white;
        font-size: 23px;
        text-align: center;
        width: 36px;
        height: 37px;
        padding-top: 5px;
    }

    /*.slick-slider[data-v-6bed67a2] {*/
    /*    max-height: 330px;*/
    /*}*/

</style>