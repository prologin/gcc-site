<template>
  <div class="home">
    <Menu isConnected="false" />
    <HomeBanner />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Menu from '@/components/Menu.vue'
import HomeBanner from '@/components/HomeBanner.vue'

export default Vue.extend({
  name: 'Home',
  components: {
    Menu,
    HomeBanner
  }
})
</script>
