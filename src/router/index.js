import Vue from "vue";
import VueRouter from "vue-router";
import Similar from "@/views/Similar.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Similar",
    component: Similar,
    meta: {
      title: "Similar Words"
    }
  },
  {
    path: "/similarity-measure",
    name: "Measure",
    component: () =>
      import("@/views/Measure.vue"),
    meta: {
      title: "Similarity Measure"
    }
  },
  {
    path: "/odd-word",
    name: "OddWord",
    component: () =>
      import("@/views/OddWord.vue"),
    meta: {
      title: "Odd Word"
    }
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
