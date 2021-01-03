<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card :width="width" class="mx-auto mt-3 rounded-lg" outlined shaped tile elevation="1">
          <v-row align="center" justify="space-around">
            <v-card-title justify="center">Find Most Similar Words</v-card-title>
          </v-row>
          <v-divider></v-divider>
          <v-form ref="form" lazy-validation @submit.prevent="Find">
            <v-card-text>
              <v-text-field
                v-model="word"
                :error-messages="wordErrors"
                label="Nepali word"
                required
                outlined
                filled 
                autocomplete="on"
                v-on:input="checkWord"
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
      </v-col>
      <v-col>
        <Words :word="word"/>
      </v-col>
    </v-row>
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
  </v-container>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required } from 'vuelidate/lib/validators'
  import { mapGetters } from "vuex";
  import Words from "@/components/Words"

  export default {
    mixins: [validationMixin],

    validations: {
      word: { required },
    },

    data () {
      return {
        chip: true,
        word: '',
      }
    },
    components: {
      Words
    },
    computed: {
      wordErrors () {
        const errors = []
        if (!this.$v.word.$dirty) return errors
        !this.$v.word.required && errors.push('Nepali word is required.')
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
        "words": "getSimilarWords"
      })
    },

    methods: {
      Find () {
        this.$v.$touch()
        this.chip = true;
        if (this.$v.$dirty && !this.$v.$error) {
          const payload = {
            word: this.word,
            topn: 10,
          }
          this.$store.dispatch("SimilarWords", payload)
        }
      },
      clear () {
        this.$v.$reset()
        this.word = ''
      },
      checkWord () {
        if (this.word == "") {
          this.$store.commit("SET_SIMILAR_WORDS", [])
        }
      }
    },
    mounted () {
      this.$store.commit("SET_ERROR", "")
      this.$store.commit("SET_SIMILAR_WORDS", [])
    }
  }
</script>