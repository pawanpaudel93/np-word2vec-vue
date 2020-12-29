import Vue from "vue";
import VueRouter from "vue-router";
import Similar from "@/views/Similar.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Similar",
    component: Similar
  },
  {
    path: "/similarity-measure",
    name: "Measure",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Measure.vue")
  },
  {
    path: "/odd-word",
    name: "OddWord",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/OddWord.vue")
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
