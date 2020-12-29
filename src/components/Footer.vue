<template>
    <v-card height="100">
        <v-footer
            absolute
            class="font-weight-medium"
            color="indigo"
            dark
        >
        <v-col
            class="py-4 text-center white--text"
            cols="12"
        >
            &copy;{{ new Date().getFullYear() }} — <strong>NP Word2Vec</strong>
        </v-col>
        </v-footer>
    </v-card>
</template>

<script>
export default {
    name: "Footer"
}
</script>