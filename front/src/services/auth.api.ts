import axios from 'axios'

const AUTH_API_URL = '/api/v1/token'

export default class AuthAPIService {
  async login (username?: string, password?: string) {
    return axios.post(AUTH_API_URL + '/', { username, password }).then(
      ({ data }) => Promise.resolve(data),
      (error) => Promise.reject(error)
    )
  }

  async refreshToken (refresh?: string) {
    return axios.post(AUTH_API_URL + '/refresh/', { refresh }).then(
      ({ data }) => Promise.resolve(data),
      (error) => Promise.reject(error)
    )
  }
}

export const authAPI = new AuthAPIService()
