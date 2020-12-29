<template>
  <v-container>
    <v-card :width="width" class="mx-auto mt-3 rounded-lg" outlined shaped tile elevation="1">
      <v-row align="center" justify="space-around">
        <v-card-title justify="center">Find Odd Word</v-card-title>
      </v-row>
      <v-divider></v-divider>
       <v-form ref="form" lazy-validation @submit.prevent="Find">
        <v-row align="center" justify="space-around">Enter Nepali words seperated by commas</v-row>
        <v-card-text>
          <v-text-field
            v-model="words"
            :error-messages="wordsErrors"
            label="Nepali words"
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
    <v-row align="center" justify="space-around">{{oddWord}}</v-row>
  </v-container>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required } from 'vuelidate/lib/validators'
  import { mapGetters } from "vuex";

  export default {
    mixins: [validationMixin],

    validations: {
      words: { required },
    },

    data () {
      return {
        chip: true,
        words: '',
      }
    },
    computed: {
      wordsErrors () {
        const errors = []
        if (!this.$v.words.$dirty) return errors
        !this.$v.words.required && errors.push('Nepali words is required.')
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
        "oddWord": "getOddWord",
      })
    },

    methods: {
      Find () {
        this.$v.$touch()
        this.chip = true;
        if (this.$v.$dirty && !this.$v.$error) {
          const payload = {
            words: this.words,
          }
          this.$store.dispatch("OddWord", payload)
        }
      },
      clear () {
        this.$v.$reset()
        this.words = ''
      },
    },
    mounted () {
      this.$store.commit("SET_ERROR", "")
    }
  }
</script>