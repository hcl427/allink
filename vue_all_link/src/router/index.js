import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
const router = new VueRouter({
  routes: [
    {
      path: '/',
      redirect: "/home",
      name: "layout",
      component: () => import('@/views/layout.vue'),
      children: [
        {
          path: '/home',
          name: 'home',
          component: () => import('@/views/home.vue'),
        },
        {
          path: '/messageBoard',
          component: () => import('@/views/messageBoard/home.vue')
        }
      ]
    },

  ]
});
export default router