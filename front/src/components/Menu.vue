<template>
<b-navbar toggleable="md">
  <b-navbar-brand to="/">
    <img class="menu-logo ml-5 pl-3" src="../assets/GCC_3.svg" alt="Logo des stages Girls Can Code" />
  </b-navbar-brand>
  <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

  <b-collapse id="nav-collapse" is-nav>
    <b-navbar-nav class="ml-auto" align="left">
      <b-nav-item v-bind:href="'/api/sso/login/prologin?next=' + currentLocation()">
        <b-button class="secondary-button"> S'inscrire </b-button>
      </b-nav-item>
      <b-nav-item v-bind:href="'/api/sso/login/prologin?next=' + currentLocation()">
        <b-button class="primary-button"> Se connecter </b-button>
      </b-nav-item>
    </b-navbar-nav>
  </b-collapse>
</b-navbar>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'Menu',
  methods: {
    currentLocation: function () {
      if (window.location !== undefined) {
        return window.location.href
      }
      return 'filler'
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
</style>
