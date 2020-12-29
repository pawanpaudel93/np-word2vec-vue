<template>
    <v-app-bar app color="indigo" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Server Dashboard Logo"
          class="shrink mr-2"
          contain
          src="@/assets/logo.png"
          transition="scale-transition"
          width="40"
        />
      </div>
      <v-toolbar-title>NP Word2Vec</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="ml-3">
        <v-btn text to="/">Similar Words</v-btn>
        <v-btn text to="/similarity-measure">Similarity Measure</v-btn>
        <v-btn text to="/odd-word">Odd Word</v-btn>
      </v-toolbar-items>
    </v-app-bar>
</template>

<script>
  export default {
    name: "NavBar"
  };
</script>