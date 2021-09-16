<template>
<div>
  <b-container fluid class="home-banner">
      <b-col class="ml-5 mt-5 pt-5 w-50">
        <h1> Stage d'initiation à l'informatique pour collégiennes et lycéennes. </h1>
        <b-button @click="scrollTo('event-list')" class="primary-button subtitleSize" block size="lg"> Voir les stages </b-button>
      </b-col>
  </b-container>
</div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'HomeBanner',
  methods: {
    scrollTo (index) {
      document.getElementById(index).scrollIntoView({ behavior: 'smooth' })
    }
  }
})
</script>

<style scoped>
  .home-banner {
    height: 70vh;
    background-size: cover;
    background-image: url('~@/assets/girls_class.svg');
    background-repeat: no-repeat;
    background-position: bottom 0 right 0;
  }
</style>
