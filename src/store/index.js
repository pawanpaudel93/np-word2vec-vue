import Vue from "vue";
import Vuex from "vuex";
import axios from "axios"

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    endpoints: {
      similarWords: "/api/v1/similar-words",
      similarityMeasure: "/api/v1/similarity",
      oddWord: "/api/v1/oddoneout"
    },
    similarWords: [],
    similarityMeasure: "",
    oddWord: "",
    error: "",
  },
  mutations: {
    'SET_SIMILAR_WORDS' (state, data) {
      state.similarWords = data;
    },
    'SET_ERROR' (state, data) {
      state.error = data;
    },
    'SET_SIMILARITY_MEASURE' (state, data) {
      state.similarityMeasure = data;
    },
    'SET_ODD_WORD' (state, data) {
      state.oddWord = data;
    }
  },
  actions: {
    SimilarWords({commit, state}, payload) {
      axios.post(state.endpoints.similarWords, payload)
        .then(res => {
          commit("SET_SIMILAR_WORDS", res.data)
          commit("SET_ERROR", "")
        })
        .catch(err => {
          commit("SET_ERROR", err.response.data.error)
          commit("SET_SIMILAR_WORDS", [])
        })
    },
    SimilarityMeasure({commit, state}, payload) {
      axios.post(state.endpoints.similarityMeasure, payload)
        .then(res => {
          commit("SET_SIMILARITY_MEASURE", res.data.similarityMeasure)
          commit("SET_ERROR", "")
        })
        .catch(err => {
          commit("SET_SIMILARITY_MEASURE", "")
          commit("SET_ERROR", err.response.data.error)
        })
    },
    OddWord({commit, state}, payload) {
      axios.post(state.endpoints.oddWord, payload)
        .then(res => {
          commit("SET_ODD_WORD", res.data.oddOne)
          commit("SET_ERROR", "")
        })
        .catch(err => {
          commit("SET_ODD_WORD", "")
          commit("SET_ERROR", err.response.data.error)
          console.log(state)
        })
    }
  },
  getters: {
    getSimilarWords(state) {
      return state.similarWords;
    },
    getError(state) {
      return state.error;
    },
    getSimilarityMeasure(state) {
      return state.similarityMeasure;
    },
    getOddWord (state) {
      return state.oddWord;
    }
  },
  modules: {}
});
