<template>
  <div>
    <Header />
    <HomeBanner />
    <EventList />
    <FAQ />
    <Partners v-bind:isFrontPage="true"/>
    <Newsletter />
    <Footer />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Header from '@/components/Header.vue'
import HomeBanner from '@/components/HomeBanner.vue'
import EventList from '@/components/EventList.vue'
import Partners from '@/components/Partners.vue'
import FAQ from '@/components/FAQ.vue'
import Newsletter from '@/components/Newsletter.vue'
import Footer from '@/components/Footer.vue'

export default Vue.extend({
  name: 'Home',
  components: {
    Header,
    HomeBanner,
    EventList,
    Partners,
    FAQ,
    Newsletter,
    Footer
  }
})
</script>
