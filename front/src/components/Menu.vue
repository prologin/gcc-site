<template>
<b-navbar toggleable="md">
  <div class="col-1"> </div>
  <b-navbar-brand to="/">
    <img class="menu-logo" src="../assets/GCC_3.svg" alt="Logo des stages Girls Can Code" />
  </b-navbar-brand>
  <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

  <b-collapse id="nav-collapse" is-nav>
    <b-navbar-nav class="ml-auto" align="left">
      <b-nav-item href="#">
        <b-button class="secondary-button"> S'inscrire </b-button>
      </b-nav-item>
      <b-nav-item href="#">
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
  props: {
    isConnected: Boolean,
    name: String,
    surname: String
  }
})
</script>

<style>
  .menu-logo {
    width: 5em;
  }
</style>
