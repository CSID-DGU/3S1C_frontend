import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import VueWordCloud from 'vuewordcloud';
Vue.config.productionTip = false
Vue.component(VueWordCloud.name, VueWordCloud);

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
