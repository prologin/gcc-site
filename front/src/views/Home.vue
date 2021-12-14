<template>
  <b-container fluid class="p-0">
    <Header />
      <b-container fluid class="home-banner">
      <b-row class="h-100" align-v="center" align-h="center">
        <b-col class="text-center text-md-left col-md-5 col-lg-4 content-background">
          <h1> Stage d'initiation à l'informatique pour collégiennes et lycéennes. </h1>
          <b-button @click="scrollTo('event-list')" class="primary-button subtitleSize mt-4" block> Voir les stages </b-button>
          <b-button @click="scrollTo('faq')" class="secondary-button subtitleSize" block>Plus d'informations</b-button>
        </b-col>
      </b-row>
    </b-container>
    <EventList id="event-list" />
    <FAQ id="faq" />
    <Partners v-bind:isFrontPage="true"/>
    <Newsletter />
    <Footer />
  </b-container>
</template>

<script>
import Vue from 'vue'
import Header from '@/components/Header.vue'
import EventList from '@/components/EventList.vue'
import Partners from '@/components/Partners.vue'
import FAQ from '@/components/FAQ.vue'
import Newsletter from '@/components/Newsletter.vue'
import Footer from '@/components/Footer.vue'

export default Vue.extend({
  name: 'Home',
  components: {
    Header,
    EventList,
    Partners,
    FAQ,
    Newsletter,
    Footer
  },
  methods: {
    scrollTo (index) {
      document.getElementById(index).scrollIntoView({ behavior: 'smooth' })
    }
  }

})
</script>

<style>
.home-banner {
  height: 70vh;
  background-image: url('~@/assets/girl-class-v2.svg'), url('~@/assets/code-background-v2.svg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
</style>
