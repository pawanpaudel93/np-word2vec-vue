<template>
  <v-container>
    <v-card :width="width" class="mx-auto mt-3 rounded-lg" outlined shaped tile elevation="1">
      <v-row align="center" justify="space-around">
        <v-card-title justify="center">Find Two Words Similarity Measure</v-card-title>
      </v-row>
      <v-divider></v-divider>
       <v-form ref="form" lazy-validation @submit.prevent="Find">
        <v-card-text>
          <v-text-field
            v-model="word1"
            :error-messages="wordErrors1"
            label="Nepali word1"
            required
            outlined
            filled 
            autocomplete="on"
          ></v-text-field>
          <v-text-field
            v-model="word2"
            :error-messages="wordErrors2"
            label="Nepali word2"
            required
            outlined
            filled 
            autocomplete="on"
          ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-row align="center" justify="space-around">
            <v-btn
              type="submit"
              class="mr-4"
              color="success"
              large
            >
              Find
            </v-btn>
          </v-row>
        </v-card-actions>
      </v-form>
    </v-card>
    <v-row align="center" justify="space-around">
      <v-chip
        v-if="chip && error"
        class="ma-2"
        close
        color="red"
        text-color="white"
        @click:close="chip = false"
      >
        {{error}}
      </v-chip>
    </v-row>
    <v-row align="center" justify="space-around">{{similarityMeasure}}</v-row>
  </v-container>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required } from 'vuelidate/lib/validators'
  import { mapGetters } from "vuex";

  export default {
    mixins: [validationMixin],

    validations: {
      word1: { required },
      word2: { required }
    },

    data () {
      return {
        chip: true,
        word1: '',
        word2: ''
      }
    },
    computed: {
      wordErrors1 () {
        const errors = []
        if (!this.$v.word1.$dirty) return errors
        !this.$v.word1.required && errors.push('Nepali word1 is required.')
        return errors
      },
      wordErrors2 () {
        const errors = []
        if (!this.$v.word2.$dirty) return errors
        !this.$v.word2.required && errors.push('Nepali word2 is required.')
        return errors
      },
      width() {
        switch (this.$vuetify.breakpoint.name) {
            case 'xs': return 450
            case 'sm': return 450
            case 'md': return 450
            case 'lg': return 450
            case 'xl': return 500
        }
      },
      ...mapGetters({
        "error": "getError",
        "similarityMeasure": "getSimilarityMeasure"
      })
    },

    methods: {
      Find () {
        this.$v.$touch()
        this.chip = true;
        if (this.$v.$dirty && !this.$v.$error) {
          const payload = {
            word1: this.word1,
            word2: this.word2,
          }
          this.$store.dispatch("SimilarityMeasure", payload)
        }
      },
      clear () {
        this.$v.$reset()
        this.word1 = ''
        this.word2 = ''
      },
    },
    mounted () {
      this.$store.commit("SET_ERROR", "")
    }
  }
</script>