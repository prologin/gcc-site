import BaseAPIService from '@/services/base.api'

export default class UsersAPIService extends BaseAPIService {
  constructor () {
    super('users')
  }

  async usersMeRead () {
    return this.axiosCall({
      method: 'get',
      url: '/me/'
    })
  }

  async usersMeUpdate (user) {
    return this.axiosCall({
      method: 'get',
      url: '/me/',
      data: user
    })
  }

  async usersMePartialUpdate (user) {
    return this.axiosCall({
      method: 'get',
      url: '/me/',
      data: user
    })
  }
}

export const usersAPI = new UsersAPIService()
