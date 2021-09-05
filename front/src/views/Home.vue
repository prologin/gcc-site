<template>
  <div>
    <Menu  />
    <HomeBanner />
    <EventList />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Menu from '@/components/Menu.vue'
import HomeBanner from '@/components/HomeBanner.vue'
import EventList from '@/components/EventList.vue'

export default Vue.extend({
  name: 'Home',
  components: {
    Menu,
    HomeBanner,
    EventList
  }
})
</script>
