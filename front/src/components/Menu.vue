<template>
  <div class="menu">
    <img class="menu-logo" src="../assets/GCC_3.svg" />
    <div class="nav-buttons" v-if="isConnected">
       <b-button class="button primary-button"> S'inscrire </b-button>
       <b-button class="button secondary-button"> Se connecter </b-button>
    </div>
    <div v-else>
      Bonjour {{ name }} {{ surname }} !
    </div>

  </div>
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
  width: 10em;
  height: 3em;
  padding-left: 5%;
}

.menu {
  padding-top: 0.7em;
  flex-wrap: wrap;
  display: flex; /* flexbox */
  justify-content: space-between; /* space between direct children */
  align-items: center;
}

#connect {
}

.nav-buttons {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}
</style>
