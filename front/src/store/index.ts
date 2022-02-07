import Vue from 'vue'
import Vuex from 'vuex'

import Auth from '@/store/modules/auth.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    Auth
  }
})
