import BaseAPIService from '@/services/base.api'

export default class EventsAPIService extends BaseAPIService {
  constructor () {
    super('events')
  }

  async getEventList () {
    return this.axiosCall({ method: 'get', url: '/events' })
  }

  async getEventBasicInfo (eventId: number) {
    return this.axiosCall({ method: 'get', url: `/event/${eventId}` })
  }

  async getEventDetailedInfo (eventId: number) {
    return this.axiosCall({ method: 'get', url: `/event/${eventId}/details` })
  }

  async getEventQuestions (eventId: number) {
    return this.axiosCall({ method: 'get', url: `/event/${eventId}/questions` })
  }
}

export const eventsAPI = new EventsAPIService()
