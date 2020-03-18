<template>
    <div>
        <Loader v-if="isLoading"/>
        <ul class="w-full py-6">
            <li class="inline-block px-5"></li>
        </ul>

        <Carousel/>

        <div class="mt-3 w-full">
            <swiper :options="swiperOption">
                <swiper-slide v-for="category in mockup.categorys" :key="category.key">
                    <button @click="goCategory(category)"
                            class="w-full bg-white cs-border-2 hover:bg-unHilight text-black py-2 h-full text-center"
                            style="height: 48px">
                        {{category.type}}
                    </button>
                </swiper-slide>
            </swiper>
        </div>

        <section class="mt-3">
            <h1 class="my-3 text-xl">{{$t('recommend')}}</h1>
            <SwiperItem :dataItem="recommendProduct"/>
        </section>

        <section class="mt-3">
            <h1 class="my-3 text-xl">{{$t('new_product')}}</h1>
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

    export default {
        name: 'MyComponent',
        components: {VueSlickCarousel, SwiperItem, Loader, Carousel},
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
                this.$message.error('Oops, Something is Error. code ' + e.status + ', at load recommend');
            })
            axios.get(this.$store.state.endpoints.newestProduct).then(res => {
                this.newestProduct = res.data.data.slice(0, 8)
                this.isLoading = false
            }).catch(e => {
                this.$message.error('Oops, Something is Error. code ' + e.status + ', at load new Product');
            })

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