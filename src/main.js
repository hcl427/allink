import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import service from './request/http'

Vue.use(ElementUI);
Vue.prototype.$axios = service
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
