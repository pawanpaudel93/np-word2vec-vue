<template>
  <v-card
    max-width="450"
		class="mx-auto mt-5"
  >
    <v-toolbar
      color="indigo"
      dark
    >
      <v-toolbar-title v-if="word">Similar Words for {{word}}</v-toolbar-title>
    </v-toolbar>

    <v-list three-line class="overflow-y-auto" max-height="445" v-if="words.length != 0 && word">
      <template v-for="(item, index) in words">
        <v-divider
					v-if="index != 0"
          :key="index"
          inset
        ></v-divider>
        <v-list-item
          :key="item.index"
        >
          <v-list-item-content>
            <v-list-item-title v-html="item[0]"></v-list-item-title>
            <v-list-item-subtitle v-html="'Similarity Score: '+item[1]"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
    <v-list v-else>
      <v-list-item-content>
        <v-list-item-title align="center">No similar words</v-list-item-title>
      </v-list-item-content>
    </v-list>
  </v-card>
</template>

<script>
  export default {
		name: "Words",
		computed: {
			words() {
				return this.$store.getters.getSimilarWords;
			}
    },
    props: ["word"],
  }
</script>