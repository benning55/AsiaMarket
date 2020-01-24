<template>
    <!--    <div class="w-full h-16 bg-white absolute top-0 left-0">-->
    <!--        <ul class="flex h-16">-->
    <!--            <li class="float-left px-5">LOGO</li>-->
    <!--            <li class="px-5 inline-block"> 55</li>-->
    <!--            <li class="float-right px-5"><a @click="changeLocale(`en`)">EN </a> | <a @click="changeLocale(`th`)"> TH</a>-->
    <!--            </li>-->
    <!--        </ul>-->
    <!--    </div>-->
    <nav class="flex items-center justify-between flex-wrap bg-white py-6">
        <ul class="w-full">
            <li class="inline-block px-5">LOGO</li>

            <li class="float-right px-5 flex-grow"><a @click="changeLocale(`en`)">EN </a> | <a @click="changeLocale(`th`)"> TH</a>
            </li>
        </ul>
    </nav>
</template>
<script>
    import i18n from "../plugins/i18n";

    export default {
        name: "Navbar",
        data() {
            return {}
        },
        methods: {
            changeLocale(locale) {
                i18n.locale = locale
            }
        }
    }
</script>