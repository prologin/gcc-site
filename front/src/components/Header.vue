<template>
  <b-navbar toggleable="md" class="navbar fixed-top" :class="{ 'navbar-hidden': !showNavbar }">
    <b-navbar-brand :to="{ name: 'home' }">
      <img class="menu-logo ml-0 ml-sm-5 pl-3" :src="require('@/assets/logo_gcc_text_right.svg')" alt="Logo des stages Girls Can Code" />
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="ml-auto text-right">
        <b-nav-item v-bind:href="'/api/sso/login/prologin?next=' + currentLocation()">
          <b-button class="secondary-button"> S'inscrire </b-button>
        </b-nav-item>
        <b-nav-item v-bind:href="'/api/sso/login/prologin?next=' + currentLocation()">
          <b-button class="primary-button"> Se connecter </b-button>
        </b-nav-item>
        <b-nav-item>
          <hr class="my-1">
        </b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'Header',
  data () {
    return {
      showNavbar: true,
      lastScrollPosition: 0
    }
  },
  mounted () {
    window.addEventListener('scroll', this.onScroll)
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.onScroll)
  },
  methods: {
    currentLocation: function () {
      if (window.location !== undefined) {
        return window.location.href
      }
      return 'filler'
    },
    onScroll () {
      // Based on https://medium.com/@Taha_Shashtari/hide-navbar-on-scroll-down-in-vue-fb85acbdddfe

      // Get the current scroll position
      const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop
      // Because of momentum scrolling on mobiles, we shouldn't continue if it is less than zero
      if (currentScrollPosition < 0) {
        return
      }

      // Stop executing this function if the difference between
      // current scroll position and last scroll position is less than some offset
      if (Math.abs(currentScrollPosition - this.lastScrollPosition) < 60) {
        return
      }

      // Here we determine whether we need to show or hide the navbar
      this.showNavbar = currentScrollPosition < this.lastScrollPosition
      // Set the current scroll position as the last scroll position
      this.lastScrollPosition = currentScrollPosition
    }
  },
  props: {
    isConnected: Boolean,
    name: String,
    surname: String
  }
})
</script>

<style>
.menu-logo {
  width: 6em;
}

.navbar {
  background-color: white;
  transition: top 0.5s ease;
}

.navbar.navbar-hidden {
  top: -100px;
}
</style>
