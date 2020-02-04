<template>
    <div>
        <ul class="w-full py-6">
            <li class="inline-block px-5">LOGO</li>
        </ul>
        <section class="bg-white p-5 my-5">
            <a><span>Home</span> > {{mockup.detail.data.category_id}} > {{mockup.detail.data.title}}</a>
        </section>
        <section class="my-5 mb-10">
            <div class="flex mb-4 bg-white">
                <div class="w-3/12 md:4/12 lg:4/12">
                    <VueSlickCarousel
                            ref="c1"
                            :asNavFor="$refs.c2"
                            :focusOnSelect="true"
                            :dots="false"
                            :arrows="false">
                        <div v-for="img in mockup.detail.data.image" :key="img.id" class=" w-full p-10 md:p-5">
                            <img :src="img" alt="s">
                        </div>
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
                <div class="w-6/12 md:5/12 lg:md:5/12 px-10 pt-12">
                    <h1 class="text-3xl">Ctitle</h1>
                    <h1 class="text-lightGray">unit</h1>
                    <p class="mt-10">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                        Ipsum has been
                    </p>
                </div>
                <div class="w-3/12 px-10 pt-12">
                    <h1 class="text-4xl">30 $</h1>
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
                    <h1 class="text-lightGray my-5">10 Left</h1>
                </div>
            </div>
        </section>
        <h1 class="mb-2 text-xl">You may also like</h1>
        <section class="mt-3 bg-white">
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
        name: 'Detail',
        components: {
            VueSlickCarousel,
            ProductCard
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
                hover: false
            }
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

</style>