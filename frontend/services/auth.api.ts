import axios from 'axios';

const AUTH_API_URL = '/rest/v1/token';

export default class AuthAPIService {
  async login (email?: string, password?: string) {
    return axios.post(AUTH_API_URL + '/', { email, password }).then(
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
