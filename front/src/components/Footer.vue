<template>
  <b-container fluid class="footer-bg py-2 w-100">
    <b-row class="mx-5">
      <b-col class="col-12 col-lg-auto mb-3 mb-lg-0 text-center text-lg-left">
        <b-link :to='{ name: "home" }'>
          <img class="picture-size" :src="require('@/assets/logo_gcc.svg')" alt="Logo des stages Girls Can Code!" />
        </b-link>
      </b-col>
      <b-col class="col-12 col-lg-auto text-center text-lg-left">
        <b-link :to="{ name: 'privacy' }" class="secondary-button footer-link-style my-auto">Politique de
          confidentialité
        </b-link>
      </b-col>
      <b-col class="col-12 col-lg-auto text-center text-lg-left">
        <b-link :to="{ name: 'legal' }" class="secondary-button footer-link-style my-auto">Mentions légales</b-link>
      </b-col>
      <b-row class="col-12 col-lg-auto mx-auto ml-lg-auto mr-lg-0 p-0">
        <h3 class="light-text my-auto col-lg-auto order-12 order-lg-1 text-center">{{ Constants.CONTACT_EMAIL }}</h3>
        <b-row class="col-12 col-lg-auto order-1 order-lg-12 my-3 my-lg-0 mx-auto mr-lg-0" align-h="center">
          <SocialNetwork v-for="(sn, index) in Constants.SOCIAL_NETWORKS" v-bind:link="sn.link"
            v-bind:imgName="sn.imgName" v-bind:alt="sn.alt" v-bind:key="index" />
        </b-row>
      </b-row>
      <b-col class="col-12 col-lg-auto text-center text-lg-left">
        Illustrations made with <b-link href="https://storyset.com" class="secondary-button footer-link-style my-auto">
          Storyset</b-link>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Vue from 'vue'
import SocialNetwork from '@/components/SocialNetwork.vue'

import * as Constants from '@/constants'

export default Vue.extend({
  name: 'Footer',
  components: {
    SocialNetwork
  },
  created () {
    this.Constants = Constants
  }
}
)
</script>

<style>
.footer-bg {
  flex-shrink: 0;
  background-color: white;
}

.picture-size {
  max-height: 30px;
}

.footer-link-style {
  font-size: 80%;
}
</style>
