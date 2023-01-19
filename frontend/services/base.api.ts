// Base class for API calls, new API services should inherit from it.
//
// https://dev.to/blindkai/managing-api-layers-in-vue-js-with-typescript-hno
// https://itnext.io/vue-tricks-smart-api-module-for-vuejs-b0cae563e67b

import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';

export default class BaseAPIService {
  private axiosInstance: AxiosInstance

  constructor(resource: string) {
    this.axiosInstance = axios.create({
      baseURL: '/rest/v1/' + resource
    });
  }

  protected async axiosCall (config: AxiosRequestConfig) {
    try {
      const { data } = await this.axiosInstance.request(config)
      return Promise.resolve(data)
    } catch (error) {
      return Promise.reject(error)
    }
  }
}
