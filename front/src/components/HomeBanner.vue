<template>
<div>
  <div class="home-banner">
    <div class="banner-text">
      <h1 class="banner-title"> Stage d'initiation à l'informatique pour collégiennes et lycéennes. </h1>
      <b-button block size="lg" class="primary-button banner-button"> S'inscrire à un stage </b-button>
    </div>
  </div>
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
    height: 90vh;
    background-size: cover;
    background-image: url('../assets/girls_class.svg');
    background-repeat: no-repeat;
    background-position: bottom 0 right 0;
  }
  .banner-title {
    font-weight: 600;
    font-size: 3em;
    max-width: 14em;
  }
  .banner-text {
    position: absolute;
    top: 15%;
    left: 10%;
    display: block;
  }
  .banner-button {
    margin-top: 2em;
    font-weight: 600;
  }
</style>
