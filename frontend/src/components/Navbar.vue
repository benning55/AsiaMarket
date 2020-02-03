<template>
    <nav class="shadow-lg flex items-center justify-between flex-wrap bg-white py-6 fixed w-full z-10">
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