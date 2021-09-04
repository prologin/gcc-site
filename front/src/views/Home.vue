<template>
  <div class="home">
    <Menu isConnected="false" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Menu from '@/components/Menu.vue'

export default defineComponent({
  name: 'Home',
  components: {
    Menu
  }
})
</script>
