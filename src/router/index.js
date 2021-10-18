import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
const router = new VueRouter({
  routes: [
    {
      path: '/',
      // redirect: "/",
      component: () => import('@/views/home.vue')
    }
  ]
});
export default router