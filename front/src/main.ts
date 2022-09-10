import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/css/bootstrap.css'

import './assets/css/main.css'

Vue.mixin({
  methods: {
    scrollTo (index: string, pos?: ScrollLogicalPosition) {
      const selectedElement = window.document.getElementById(index)
      if (selectedElement !== null) {
        selectedElement.scrollIntoView({ block: pos || 'start', behavior: 'smooth' })
      }
    }
  }
})

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
