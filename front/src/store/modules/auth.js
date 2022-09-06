// Based on https://www.smashingmagazine.com/2020/10/authentication-in-vue-js/

import { authAPI } from '@/services/auth.api'
import { usersAPI } from '@/services/users.api'

const user = JSON.parse(localStorage.getItem('user'))
const initialSate = user ? { user: user } : { user: null }

const getters = {
  isAuthenticated: (state) => !!state.user,

  getFirstName: (state) => state.user ? state.user.first_name : null,
  getLastName: (state) => state.user ? state.user.last_name : null,
  getEmail: (state) => state.user ? state.user.email : null,
  getAddress: (state) => state.user ? state.user.address : null,
  getCity: (state) => state.user ? state.user.city : null,
  getZipCode: (state) => state.user ? state.user.zip_code : null,
  getCountry: (state) => state.user ? state.user.country : null
}

const actions = {
  async login ({ commit }, user) {
    return authAPI.login(user.email, user.password).then(
      (data) => {
        localStorage.setItem('access', data.access)
        localStorage.setItem('refresh', data.refresh)

        usersAPI.usersMeRead().then(user => {
          localStorage.setItem('user', JSON.stringify(user))
          commit('loginSuccess', user)
          return Promise.resolve(user)
        })
      }
    ).catch(
      (error) => {
        commit('loginFailure')
        return Promise.reject(error)
      }
    )
  },

  async logout ({ commit }) {
    localStorage.removeItem('user')
    localStorage.removeItem('access')
    localStorage.removeItem('refresh')

    commit('logout')
  },

  async register ({ dispatch }, user) {
    // TODO
    console.log('register method is not implemented')
  },

  async refreshToken ({ commit }) {
    authAPI.refreshToken(localStorage.getItem('refresh')).then(
      (access) => {
        localStorage.setItem('access', access)
      },
      () => {
        localStorage.removeItem('user')
        localStorage.removeItem('access')
        localStorage.removeItem('refresh')
      }
    )
  }
}

const mutations = {
  loginSuccess (state, user) {
    state.user = user
  },

  loginFailure (state) {
    state.user = null
  },

  logout (state) {
    state.user = null
  }
}

export default {
  state: initialSate,
  getters,
  actions,
  mutations
}
