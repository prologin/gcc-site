import BaseAPIService from '@/services/base.api';

import { UserType } from '@/models/user.interface';

export default class UsersAPIService extends BaseAPIService {
  constructor () {
    super('users');
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
