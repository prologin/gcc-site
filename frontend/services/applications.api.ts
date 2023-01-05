import BaseAPIService from '@/services/base.api'

export default class ApplicationsAPIService extends BaseAPIService {
  constructor () {
    super('applications')
  }

  async applicationsList (user_id?:number, event_id?:number) {
    return this.axiosCall({
      method: 'get',
      url: '/',
      params: {
        user_id: user_id,
        event_id:event_id
      }
    })
  }

  async applicationsRead (id: number) {
    return this.axiosCall({ method: 'get', url: `/${id}/` })
  }
}

export const applicationsAPI = new ApplicationsAPIService()
