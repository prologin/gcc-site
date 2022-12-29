import BaseAPIService from '@/services/base.api'

export default class ApplicationsAPIService extends BaseAPIService {
  constructor () {
    super('applications')
  }

  async applicationsList (event_id?:number) {
    return this.axiosCall({
      method: 'get',
      url: '/',
      params: {
        event_id:event_id
      }
    })
  }

  async applicationsRead (id: number) {
    return this.axiosCall({ method: 'get', url: `/${id}/` })
  }
}

export const applicationsAPI = new ApplicationsAPIService()
