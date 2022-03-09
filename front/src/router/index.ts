import VueRouter, { RouteConfig } from 'vue-router'
import Vue from 'vue'

import About from '@/views/About.vue'
import Applications from '@/views/ApplicationsView.vue'
import Home from '@/views/Home.vue'
import Inscription from '@/views/Inscription.vue'
import LegalNotices from '@/views/LegalNotices.vue'
import PageNotFound from '@/views/PageNotFound.vue'
import PartnersPage from '@/views/PartnersPage.vue'
import Privacy from '@/views/Privacy.vue'
import LoginView from '@/views/Login.vue'

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
    path: '/privacy',
    name: 'privacy',
    component: Privacy
  },
  {
    path: '/partenaires',
    name: 'partners',
    component: PartnersPage
  },
  {
    path: '/applications',
    name: 'applications',
    component: Applications
  },
  {
    path: '/connexion',
    name: 'login',
    component: LoginView
  },
  {
    path: '*',
    component: PageNotFound
  }
]

const scrollBehavior = () => {
  return { x: 0, y: 0 }
}

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior
})

export default router
