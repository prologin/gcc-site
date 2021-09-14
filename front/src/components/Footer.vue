<template>
    <b-row align-v="center" class="m-2 mx-5">
        <b-col md="auto">
            <img class="picture-size"
                 :src="require('@/assets/logo_gcc.svg')"
                 alt="Logo des stages Girls Can Code!" />
        </b-col>
        <b-col md="auto">
            <h4 class="my-auto">Politique de confidentialité</h4>
        </b-col>
        <b-col md="auto">
            <h4 class="my-auto">Mentions légales</h4>
        </b-col>
        <b-row class="ml-auto">
            <h3 class="light-text my-auto mr-4">info@prologin.org</h3>
            <b-row cols="5">
                <SocialNetwork v-for="(sn, index) in socialNetworks"
                               v-bind:link="sn.link"
                               v-bind:imgName="sn.imgName"
                               v-bind:alt="sn.alt"
                               v-bind:key="index" />
            </b-row>
        </b-row>
    </b-row>
</template>

<script>
import Vue from 'vue'
import SocialNetwork from '@/components/SocialNetwork.vue'

export default Vue.extend({
  name: 'Footer',
  components: {
    SocialNetwork
  },
  data () {
    return {
      socialNetworks: [
        {
          link: 'https://www.facebook.com/stagegirlscancode/',
          imgName: 'facebook-logo.svg',
          alt: 'Page facebook des stages Girls Can Code!'
        },
        {
          link: 'https://www.flickr.com/photos/prologin/',
          imgName: 'flickr-logo.svg',
          alt: 'Album photos de l\'association Prologin'
        },
        {
          link: 'https://www.instagram.com/association_prologin/',
          imgName: 'instagram-logo.svg',
          alt: 'Page instagram de l\'association Prologin'
        },
        {
          link: 'https://fr.linkedin.com/company/prologin',
          imgName: 'linkedin-logo.svg',
          alt: 'Page linkedin de l\'association Prologin'
        },
        {
          link: 'https://twitter.com/prologin',
          imgName: 'twitter-logo.svg',
          alt: 'Page twitter de l\'association Prologin'
        }
      ]
    }
  }
})
</script>

<style>
.picture-size {
  max-height: 30px;
}

.light-text {
  color: #37474F;
  font-weight: 400;
}
</style>
