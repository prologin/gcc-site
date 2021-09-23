<template>
  <b-container fluid>
    <b-row align-h="center">
      <b-img class="sponsors-logo-style m-5"
        v-for="(sponsor, index) in sponsorsSortedByOrder"
        v-show="displayLogo(sponsor)"
        :src="require(`@/assets/${sponsor.imgName}`)"
        :key="index"
        width="200"
        height="100" />
    </b-row>
    <b-row align-h="center" class="mb-3">
      <b-button v-if="isFrontPage" :to="{ name: 'partners' }" class="secondary-button">Voir tous nos partenaires</b-button>
    </b-row>
  </b-container>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'Partners',
  props: ['isFrontPage'],
  data () {
    return {
      sponsors: [
        {
          imgName: 'epita-logo.png',
          order: 3,
          isInFrontPage: true
        },
        {
          imgName: 'ministere-logo.png',
          order: 4,
          isInFrontPage: false
        },
        {
          imgName: 'strasbourg-logo.png',
          order: 1,
          isInFrontPage: false
        },
        {
          imgName: 'kb-logo.png',
          order: 2,
          isInFrontPage: true
        }
      ]
    }
  },
  computed: {
    sponsorsSortedByOrder: function () {
      return this.sponsors.slice().sort((a, b) => a.order - b.order)
    }
  },
  methods: {
    displayLogo: function (partner) {
      return (this.isFrontPage && partner.isInFrontPage) || !this.isFrontPage
    }
  }
})
</script>

<style>
.sponsors-logo-style {
  object-fit: contain;
}

</style>
