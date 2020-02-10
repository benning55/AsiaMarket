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

        <section class="mt-3 w-full">
            <h1 class="my-3 text-xl">Promotion</h1>
            <div class="flex flex-wrap">
                <div v-for="item in items" :key="item.id" class="w-1/2 sm:w-1/4 sc-480:w-1/3 sc-1400:w-1/5">
                    <ProductCard :productData="item"/>
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
    import axios from 'axios'

    export default {
        name: 'CategoryView',
        components: {
            VueSlickCarousel,
            ProductCard
        },
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
                },
                items:[]
            }
        },
        created() {
            this.loadCategory()
        },
        methods: {
            loadCategory() {
                this.items = []
                axios.post('http://localhost:8000/api/products/product/', {
                    "category_id": this.$route.params.id
                }).then(res=>this.items = res.data.data).catch()

            }
        },
        watch:{
            '$route.params.id'(){
                console.log("change")
                this.loadCategory()
            }
        }
    }
</script>

<style scoped>
    .grid-cols-2 {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    }

    .grid-cols-3 {
        grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
    }

    .grid-cols-4 {
        grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
    }

    .grid-cols-5 {
        grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
    }

    .grid {
        display: grid !important;
    }
</style>