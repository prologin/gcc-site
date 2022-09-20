<template>
  <div class="main-body-style">
    <b-container fluid class="p-0">
      <Header />
      <b-container fluid class="basic-background content">
        <b-container fluid class="content-background">
          <div class="m-5">
            <h1>Nos partenaires</h1>
            <p>Merci à tous nos partenaires qui nous permettent d'organiser les stages.</p>
            <hr>
            <Partners />
            <hr>
            <h4>Si vous souhaitez nous soutenir, vous pouvez nous envoyer un mail à <a
                :href="`mailto:${Constants.PARTNERS_EMAIL}`">
                {{ Constants.PARTNERS_EMAIL }}
              </a></h4>
          </div>
        </b-container>
      </b-container>
      <Footer />
    </b-container>
  </div>
</template>

<script>
import Vue from 'vue'
import Partners from '@/components/Partners.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

import * as Constants from '@/constants'

export default Vue.extend({
  name: 'PartnersPage',
  components: {
    Partners,
    Header,
    Footer
  },
  created () {
    this.Constants = Constants
  }
})

</script>
