<template>
  <div class="main-body-style">
    <Header/>
      <b-container fluid class="basic-background content">
        <b-container fluid class="content-background">
          <div class="m-5">
            <h1>Nos partenaires</h1>
            <p>Merci à tous nos partenaires qui nous permettent d'organiser les stages.</p>
            <hr>
            <Partners v-bind:isFrontPage="false"/>
            <hr>
            <h4>Si vous souhaitez nous soutenir, vous pouvez nous envoyer un mail à info@prologin.org</h4>
          </div>
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
