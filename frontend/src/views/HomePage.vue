<template>
    <div>
        <ul class="w-full py-6">
            <li class="inline-block px-5">LOGO</li>
        </ul>
        <VueSlickCarousel v-bind="setting1">
            <img v-for="image in mockup.showCarousel" :key="image.id" class="object-cover w-full h-56"
                 :src="image.image"
                 alt="Promotion">
        </VueSlickCarousel>

        <VueSlickCarousel v-bind="setting2">
            <button v-for="category in mockup.categorys" :key="category.id"
                    class="bg-white mt-3 cs-border hover:bg-unHilight text-black py-2 px-4">
                {{category.title}}
            </button>
        </VueSlickCarousel>

        <section class="mt-3">
            <h1 class="my-3 text-xl">Promotion</h1>
            <VueSlickCarousel v-bind="setting3">
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
            </VueSlickCarousel>
        </section>

        <section class="mt-3">
            <h1 class="my-3 text-xl">Recommend</h1>
            <VueSlickCarousel v-bind="setting3">
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
            </VueSlickCarousel>
        </section>

        <section class="mt-3">
            <h1 class="my-3 text-xl">New Product</h1>
            <VueSlickCarousel v-bind="setting3">
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
                <ProductCard/>
            </VueSlickCarousel>
        </section>
    </div>
</template>

<script>
    import VueSlickCarousel from 'vue-slick-carousel'
    import 'vue-slick-carousel/dist/vue-slick-carousel.css'
    import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
    import ProductCard from "../components/ProductCard";

    export default {
        name: 'MyComponent',
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
                            "breakpoint": 600,
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
                    "touchThreshold":4,
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
                        {id: 0, title: "friut"},
                        {id: 1, title: "friut"},
                        {id: 2, title: "friut"},
                        {id: 3, title: "friut"},
                        {id: 4, title: "friut"},
                        {id: 5, title: "friut"},
                        {id: 6, title: "friut"},
                    ]
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

    .cs-border {
        border: 3px solid #e3e4e3;
        border-style: none solid none none
    }
</style>