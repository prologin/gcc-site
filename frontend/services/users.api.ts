import BaseAPIService from '@/services/base.api';

import { UserType } from '@/models/user.interface';

export default class UsersAPIService extends BaseAPIService {
  constructor () {
    super('users');
  }

  async usersList(email: string) {
    return this.axiosCall({
      method: 'get',
      url: '/',
      params: {
        email,
      }
    })
  }

  async usersRead(id:number) {
    return this.axiosCall({
      method: 'get',
      url: `/${id}`,
    })
  }

  async usersMeRead () {
    return this.axiosCall({
      method: 'get',
      url: '/me/',
    })
  }

  async usersMeUpdate (user: UserType): Promise<UserType> {
    return this.axiosCall({
      method: 'get',
      url: '/me/',
      data: user
    });
  }

  async usersMePartialUpdate (user: UserType): Promise<UserType> {
    return this.axiosCall({
      method: 'get',
      url: '/me/',
      data: user
    });
  }
}

export const usersAPI = new UsersAPIService()
