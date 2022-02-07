// Based on https://www.smashingmagazine.com/2020/10/authentication-in-vue-js/

const state = {
  user: {
    firstName: '',
    lastName: '',
    email: ''
  }
}

const getters = {
  isAuthenticated: (state) => !!state.user.firstName && !!state.user.lastName,
  getFirstName: (state) => state.user.firstName,
  getLastName: (state) => state.user.lastName,
  getEmail: (state) => state.user.email
}

const actions = {
  async LogIn ({ commit }, user) {
    // TODO: Add the real login method
    await commit('SET_USER', user)
  },

  async LogOut ({ commit }) {
    const user = {
      firstName: '',
      lastName: '',
      email: ''
    }
    commit('SET_USER', user)
  }
}

const mutations = {
  SET_USER (state, user) {
    state.user = user
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
