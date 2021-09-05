<template>
<div>
  <b-container fluid class="home-banner hidden-phone">
    <b-row>
      <b-col class="banner-headline" offset="1" sm="12" md="5">
        <h1> Stage d'initiation à l'informatique pour collégiennes et lycéennes. </h1>
        <b-button class="primary-button headline-button" block size="lg">S'inscrire à un stage</b-button>
      </b-col>
    </b-row>
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
    height: 90vh;
    background-size: cover;
    background-image: url('../assets/girls_class.svg');
    background-repeat: no-repeat;
    background-position: bottom 0 right 0;
  }

  .banner-headline {
    margin-top: 5em;
  }

  .banner-headline h1 {
    font-weight: 700;
    font-size: 3em;
  }

  .headline-button {
    margin-top: 3em;
    font-weight: 600;
  }
</style>
