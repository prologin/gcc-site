import VueRouter, { RouteConfig } from 'vue-router'
import Vue from 'vue'

import About from '@/views/About.vue'
import Applications from '@/views/ApplicationsView.vue'
import Home from '@/views/Home.vue'
import Inscription from '@/views/Inscription.vue'
import LegalNotices from '@/views/LegalNotices.vue'
import LoginRegisterView from '@/views/LoginRegisterView.vue'
import PageNotFound from '@/views/PageNotFound.vue'
import PartnersPage from '@/views/PartnersPage.vue'
import Privacy from '@/views/Privacy.vue'
import store from '@/store/index.ts'

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
    component: Inscription,
    // Only a logged-in user can register for a new course.
    meta: { requiresAuth: true }
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
    component: Applications,
    // Only logged-in users can see their applications.
    meta: { requiresAuth: true }
  },
  {
    path: '/connexion',
    name: 'login-register',
    component: LoginRegisterView
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

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  const isAuthenticated = store.getters.isAuthenticated
  if (requiresAuth && !isAuthenticated) {
    next({
      name: 'login-register',
      query: { redirect: to.fullPath }
    })
  } else if (requiresAuth && isAuthenticated) {
    next()
  } else {
    next()
  }
})

export default router
