// Base class for API calls, new API services should inherit from it.
//
// https://dev.to/blindkai/managing-api-layers-in-vue-js-with-typescript-hno
// https://itnext.io/vue-tricks-smart-api-module-for-vuejs-b0cae563e67b

import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';

import { authAPI } from '@/services/auth.api';

export default class BaseAPIService {
  private axiosInstance: AxiosInstance

  constructor(resource: string) {
    this.axiosInstance = axios.create({
      baseURL: '/api/v1/' + resource
    });

    // Add authorization header if there is one
    this.axiosInstance.interceptors.request.use(async (config) => {
      const access = localStorage.getItem('access');

      if (access) {
        config.headers = {
          ...config.headers,
          authorization: `Bearer ${access}`
        };
      }

      return config
    });

    this.axiosInstance.interceptors.response.use(
      (response) => response,
      async (error) => {
        const config = error.config
        if (
          config.url !== '/token/' &&
          error.response &&
          error.response.status === 401 &&
          !config._retry
        ) {
          config._retry = true
          await authAPI
            .refreshToken(localStorage.getItem('refresh') || '')
            .then(
              (data) => {
                localStorage.setItem('access', data.access)
                return this.axiosCall(config)
              },
              (error) => Promise.reject(error)
            )
        }
        return Promise.reject(error)
      }
    )
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
