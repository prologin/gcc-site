import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '@/views/Home.vue'
import About from '@/views/About.vue'
import Inscription from '@/views/Inscription.vue'
import PageNotFound from '@/views/PageNotFound.vue'
import LegalNotices from '@/views/LegalNotices.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/inscription',
    name: 'inscription',
    component: Inscription
  },
  {
    path: '/legal',
    name: 'legal',
    component: LegalNotices
  },
  {
    path: '*',
    component: PageNotFound
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
