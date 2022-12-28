import { authAPI } from '../services/auth.api'
import { usersAPI } from '../services/users.api'

let user = null
const initialState = user ? { user: user } : { user: null }

if(process.browser)
    user = JSON.parse(localStorage.getItem('user'))

export const state = () => initialState


export const getters = {
    isAuthenticated: (state) => { return !!state.user },
    getFirstName: (state) => {return state.user ? state.user.first_name : null},
    getLastName: (state) => { return state.user ? state.user.last_name : null },
    getEmail: (state) => { return state.user ? state.user.email : null },
    getAddress: (state) => { return state.user ? state.user.address : null },
    getCity: (state) => { return state.user ? state.user.city : null },
    getZipCode: (state) => { return state.user ? state.user.zip_code : null },
    getCountry: (state) => { return state.user ? state.user.country : null }
}

export const actions = {
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


export const mutations = {
    loginSuccess(state, user) {
        state.user = user
  },

  loginFailure (state) {
    state.user = null
  },

  logout (state) {
    state.user = null
  }
}
