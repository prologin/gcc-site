<template>
  <div>
    <Menu  />
    <HomeBanner />
    <EventList />
    <Newsletter />
    <Footer />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Menu from '@/components/Menu.vue'
import HomeBanner from '@/components/HomeBanner.vue'
import EventList from '@/components/EventList.vue'
import Newsletter from '@/components/Newsletter.vue'
import Footer from '@/components/Footer.vue'

export default Vue.extend({
  name: 'Home',
  components: {
    Menu,
    HomeBanner,
    EventList,
    Newsletter,
    Footer
  }
})
</script>
