<template>
<div>
  <b-container fluid class="home-banner">
      <b-col class="ml-0 ml-sm-5 pl-3 mt-5 pt-2 pt-sm-5 pt-md-4 pt-lg-5 text-center text-sm-left col-sm-5 col-md-6 col-lg-5">
        <h1> Stage d'initiation à l'informatique pour collégiennes et lycéennes. </h1>
        <b-button @click="scrollTo('event-list')" class="primary-button subtitleSize mt-4" block> Voir les stages </b-button>
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
