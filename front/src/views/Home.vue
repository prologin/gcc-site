<template>
  <Menu isConnected="false" />
  <HomeBanner />
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Menu from '@/components/Menu.vue'
import HomeBanner from '@/components/HomeBanner.vue'

export default defineComponent({
  name: 'Home',
  components: {
    Menu,
    HomeBanner
  }
})
</script>
