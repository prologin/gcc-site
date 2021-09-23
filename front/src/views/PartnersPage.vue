<template>
  <div>
    <Header/>
      <b-container fluid class="basic-background">
        <b-container class="content-background m-0 m-sm-5 p-3">
          <h1>Nos partenaires</h1>
          <p>Merci à tous nos partenaires qui nous permettent d'organiser les stages.</p>
          <hr>
          <Partners v-bind:isFrontPage="false"/>
          <hr>
          <h4>Si vous souhaitez nous soutenir, vous pouvez nous envoyer un mail à info@prologin.org</h4>
        </b-container>
      </b-container>
      <Footer/>
  </div>
</template>

<script>
import Vue from 'vue'
import Partners from '@/components/Partners.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default Vue.extend({
  name: 'PartnersPage',
  components: {
    Partners,
    Header,
    Footer
  }
})

</script>

<style>
</style>
