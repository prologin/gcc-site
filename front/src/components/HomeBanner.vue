<template>
<div>
  <b-container fluid class="home-banner">
      <b-col class="ml-5 mt-5 pt-5 w-50">
        <h1> Stage d'initiation à l'informatique pour collégiennes et lycéennes. </h1>
        <!-- TODO: use vue-router link -->
        <b-button to="/inscription" class="primary-button subtitleSize" block size="lg"> S'inscrire à un stage </b-button>
      </b-col>
  </b-container>
</div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'HomeBanner',
  props: {
  }
})
</script>

<style scoped>
  .home-banner {
    height: 70vh;
    background-size: cover;
    background-image: url('../assets/girls_class.svg');
    background-repeat: no-repeat;
    background-position: bottom 0 right 0;
  }
</style>
