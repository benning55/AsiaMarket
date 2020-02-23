<template>
    <div>
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>
        <VueSlickCarousel v-bind="setting1">
            <img v-for="image in mockup.showCarousel" :key="image.id" class="object-cover w-full h-56"
                 :src="image.image"
                 alt="Promotion">
        </VueSlickCarousel>

        <div class="mt-3 w-full">
            <swiper :options="swiperOption">
                <swiper-slide v-for="category in mockup.categorys" :key="category.key">
                    <button @click="goCategory(category)"
                            class="w-full bg-white cs-border-2 hover:bg-unHilight text-black py-2 h-full text-center" style="height: 48px">
                        {{category.type}}
                    </button>
                </swiper-slide>
            </swiper>
        </div>


        <!--        <div v-dragscroll class="overflow-auto">-->
        <!--            <div class="flex mt-3 w-4/1 sm:w-2/1 sc-480:w-266per sc-1400:w-16/10">-->
        <!--                <div class="w-1/4" v-for="category in mockup.categorys" :key="category.id">-->
        <!--                    <button @click="goCategory(category)"-->
        <!--                            class="w-full bg-white  cs-border hover:bg-unHilight text-black py-2 px-4 h-full">-->
        <!--                        {{category.type}}-->
        <!--                    </button>-->
        <!--                </div>-->
        <!--            </div>-->
        <!--        </div>-->

        <section class="mt-3">
            <h1 class="my-3 text-xl">Recommend</h1>
            <SwiperItem :dataItem="recommendProduct"/>
            <!--            <div class="overflow-auto">-->
            <!--                <div class="flex w-4/1 sm:w-2/1 sc-480:w-266per sc-1400:w-16/10">-->
            <!--                    <div v-for="product in recommendProduct" :key="product.key" class="w-1/4">-->
            <!--                        <ProductCard :productData="product"/>-->
            <!--                    </div>-->
            <!--          -->
            <!--                </div>-->
            <!--            </div>-->
        </section>

        <section class="mt-3">
            <h1 class="my-3 text-xl">New Product</h1>
            <SwiperItem :dataItem="newestProduct"/>
            <!--            <div v-dragscroll class=" overflow-auto">-->
            <!--                <div class="flex w-4/1 sm:w-2/1 sc-480:w-266per sc-1400:w-16/10">-->
            <!--                    <div v-for="product in newestProduct" :key="product.key" class="w-1/4">-->
            <!--                        <ProductCard :productData="product"/>-->
            <!--                    </div>-->
            <!--                </div>-->
            <!--            </div>-->
        </section>
        <!--        <vuescroll>-->
        <!--            <div class="flex w-4/1 sm:w-2/1 sc-480:w-266per sc-1400:w-16/10">-->
        <!--                <div v-for="product in newestProduct" :key="product.key" class="w-1/4">-->
        <!--                    <ProductCard :productData="product"/>-->
        <!--                </div>-->
        <!--            </div>-->
        <!--        </vuescroll>-->
    </div>
</template>

<script>
    import VueSlickCarousel from 'vue-slick-carousel'
    import 'vue-slick-carousel/dist/vue-slick-carousel.css'
    import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
    // import ProductCard from "../components/ProductCard";
    // import {dragscroll} from 'vue-dragscroll'
    import axios from 'axios'
    // import vuescroll from 'vuescroll';
    import SwiperItem from "../components/SwiperItem";

    export default {
        name: 'MyComponent',
        // directives: {
        //     dragscroll
        // },
        components: {VueSlickCarousel, SwiperItem},
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
                setting1: {
                    "dots": true,
                    "dotsClass": "slick-dots custom-dot-class",
                    "edgeFriction": 0.35,
                    "infinite": false,
                    "speed": 500,
                    "slidesToShow": 1,
                    "slidesToScroll": 1,
                    "autoplay": true,
                    "autoplaySpeed": 3000,
                    "pauseOnDotsHover": true,
                    "pauseOnFocus": true,
                    "pauseOnHover": true
                },
                mockup: {
                    showCarousel: [
                        {
                            image: 'https://images.unsplash.com/photo-1565564331571-c3a69a159944?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1053&q=80'
                        },
                        {
                            image: 'https://images.unsplash.com/photo-1565564331571-c3a69a159944?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1053&q=80'
                        },
                        {
                            image: 'https://images.unsplash.com/photo-1565564331571-c3a69a159944?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1053&q=80'
                        },
                        {
                            image: 'https://images.unsplash.com/photo-1565564331571-c3a69a159944?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1053&q=80'
                        }
                    ],
                    categorys: [
                        {id: 1, type: "Fruits and Vegetables", color: "green"},
                        {id: 2, type: "Dry goods and Seasonings", color: "blue"},
                        {id: 3, type: "Rice Flour and Noodles", color: "yellow"},
                        {id: 4, type: "Condiments and Sauces", color: "red"},
                        {id: 5, type: "Normal and Alcoholic Beverages", color: "black"},
                        {id: 6, type: "Snack", color: "orange"},
                        {id: 7, type: "Frozen Products", color: "purple"},
                        {id: 8, type: "Other", color: "pink"},
                    ]
                },
                recommendProduct: [],
                newestProduct: []
            }
        },
        created() {
            axios.get(this.$store.state.endpoints.recommendProduct).then(res => {
                this.recommendProduct = res.data.data.slice(0, 8)
            }).catch()
            axios.get(this.$store.state.endpoints.newestProduct).then(res => {
                this.newestProduct = res.data.data.slice(0, 8)
            }).catch()
        },
        methods: {
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