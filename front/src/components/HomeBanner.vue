<template>
  <div class="home-banner" >
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
</style>
