<template>
  <div class="menu">
    <img class="menu-logo" src="../assets/GCC_3.svg" />
    <div v-if="isConnected">
       <a class="secondary-button" id="inscription" > S'inscrire </a> <!-- TODO: add link to ProloginAuth -->
       <a class="primary-button" id="connect" > Se connecter </a>
    </div>
    <div v-else>
      Bonjour {{ name }} {{ surname }} !
    </div>

  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Menu',
  props: {
    isConnected: Boolean,
    name: String,
    surname: String
  }
})
</script>

<style scoped>
.menu-logo {
  width: 5%;
  padding-left: 5%;
}

#connect {
  padding-right: 2%;
  padding-left: 2%;
  position: fixed;
}
</style>
