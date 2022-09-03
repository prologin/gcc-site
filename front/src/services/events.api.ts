import BaseAPIService from '@/services/base.api'

export default class EventsAPIService extends BaseAPIService {
  constructor () {
    super('events')
  }

  async eventsList (onlyOpen?: boolean, center?: string, startsAfter?: string, endsBefore?: string, signupStartsAfter?: string, signupEndsBefore?: string) {
    return this.axiosCall({
      method: 'get',
      url: '/',
      params: {
        only_open: onlyOpen,
        center,
        starts_after: startsAfter,
        ends_before: endsBefore,
        signup_starts_after: signupStartsAfter,
        signup_ends_before: signupEndsBefore
      }
    })
  }

  async eventsRead (id: number) {
    return this.axiosCall({ method: 'get', url: `/${id}` })
  }

  async eventsDocs (id: number) {
    return this.axiosCall({ method: 'get', url: `/${id}/docs` })
  }

  async eventsQuestions (id: number) {
    return this.axiosCall({ method: 'get', url: `/${id}/questions` })
  }
}

export const eventsAPI = new EventsAPIService()
