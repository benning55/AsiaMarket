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

        <div v-dragscroll class="overflow-auto">
            <div class="flex mt-3 w-4/1 sm:w-2/1 sc-480:w-266per sc-1400:w-16/10">
                <div class="w-1/4" v-for="category in mockup.categorys" :key="category.id">
                    <button
                            class="w-full bg-white  cs-border hover:bg-unHilight text-black py-2 px-4 h-full">
                        {{category.type}}
                    </button>
                </div>
            </div>
        </div>

        <section class="mt-3">
            <h1 class="my-3 text-xl">Promotion</h1>
            <div v-dragscroll class=" overflow-auto">
                <div class="flex w-4/1 sm:w-2/1 sc-480:w-266per sc-1400:w-16/10">
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                </div>
            </div>
        </section>

        <section class="mt-3">
            <h1 class="my-3 text-xl">Recommend</h1>
            <div v-dragscroll class=" overflow-auto">
                <div class="flex w-4/1 sm:w-2/1 sc-480:w-266per sc-1400:w-16/10">
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                </div>
            </div>
        </section>

        <section class="mt-3">
            <h1 class="my-3 text-xl">New Product</h1>
            <div v-dragscroll class=" overflow-auto">
                <div class="flex w-4/1 sm:w-2/1 sc-480:w-266per sc-1400:w-16/10">
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                    <div class="w-1/4">
                        <ProductCard/>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
    import VueSlickCarousel from 'vue-slick-carousel'
    import 'vue-slick-carousel/dist/vue-slick-carousel.css'
    import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
    import ProductCard from "../components/ProductCard";
    import {dragscroll} from 'vue-dragscroll'
    // import axios from 'axios'

    export default {
        name: 'MyComponent',
        directives: {
            dragscroll
        },
        components: {VueSlickCarousel, ProductCard},
        data() {
            return {
                setting1: {
                    "dots": true,
                    "dotsClass": "slick-dots custom-dot-class",
                    "edgeFriction": 0.35,
                    "infinite": true,
                    "speed": 500,
                    "slidesToShow": 1,
                    "slidesToScroll": 1,
                    "autoplay": true,
                    "autoplaySpeed": 3000,
                    "pauseOnDotsHover": true,
                    "pauseOnFocus": true,
                    "pauseOnHover": true
                },
                setting2: {
                    "dots": false,
                    "infinite": false,
                    "initialSlide": 0,
                    "speed": 500,
                    "slidesToShow": 5,
                    "slidesToScroll": 1,
                    "arrows": false,
                    "swipeToSlide": true,

                    "responsive": [
                        {
                            "breakpoint": 1024,
                            "settings": {
                                "slidesToShow": 5,
                            }
                        },
                        {
                            "breakpoint": 640,
                            "settings": {
                                "slidesToShow": 4,
                            }
                        },
                        {
                            "breakpoint": 480,
                            "settings": {
                                "slidesToShow": 3,
                            }
                        }
                    ]
                },
                setting3: {
                    "dots": false,
                    "infinite": false,
                    "initialSlide": 0,
                    "speed": 500,
                    "slidesToShow": 5,
                    "slidesToScroll": 1,
                    "arrows": false,
                    "swipeToSlide": true,
                    "touchThreshold": 4,
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
                            "breakpoint": 640,
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
                        {id: 0, type: "Fruits and Vegetables", color: "green"},
                        {id: 1, type: "Dry goods and Seasonings", color: "blue"},
                        {id: 2, type: "Rice Flour and Noodles", color: "yellow"},
                        {id: 3, type: "Condiments and Sauces", color: "red"},
                        {id: 4, type: "Normal and Alcoholic Beverages", color: "black"},
                        {id: 5, type: "Snack", color: "orange"},
                        {id: 6, type: "Frozen Products", color: "purple"},
                        {id: 7, type: "Other", color: "pink"},
                    ]
                }
            }
        },
        created() {
            // axios.get(this.$store.state.endpoints.productUrL).then((res) => {
            //     console.log(res)
            // }).catch()
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

    .cs-border {
        border: 3px solid #e3e4e3;
        border-style: none solid none none
    }

    .w-25-per {
        width: 25%;
    }
</style>