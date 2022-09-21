import BaseAPIService from './base.api'

export default class PartnersAPIService extends BaseAPIService {
  constructor () {
    super('partners')
  }

  async partnersList (isOnFrontPage?: string, isFeatured?: string) {
    return this.axiosCall({
      method: 'get',
      url: '/',
      params: {
        is_on_front_page: isOnFrontPage,
        featured: isFeatured
      }
    })
  }

  async partnersRead (id: number) {
    return this.axiosCall({ method: 'get', url: `/${id}/` })
  }
}

export const partnersAPI = new PartnersAPIService()
