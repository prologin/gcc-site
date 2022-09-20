<template>
  <b-container fluid>
    <b-row align-h="center" class="pt-3">
      <h1 v-if="isFeaturedSpace">Ils nous soutiennent</h1>
    </b-row>
    <b-row align-h="center">
      <b-link v-b-modal="'modal-' + partner.name" v-for="(partner, index) in partnersSortedByOrder" :key="index">
        <b-img class="partners-logo-style m-5" :src=partner.logo width="200" height="100" />
        <b-modal :id="'modal-' + partner.name" size="lg" centered ok-only hide-header ok-title="Fermer"
          ok-variant="secondary-button">
          <b-card :img-src=partner.logo :img-alt="`Logo de notre partenaire ${partner.name}`" img-width=250 img-left
            class="px-3" :title="partner.name" title-tag="h1">

            <b-card-text>
              <p>{{ partner.description }}</p>
            </b-card-text>
            <b-card-text>
              <a :href="partner.website_url">Voir leur site</a>
            </b-card-text>
          </b-card>
        </b-modal>
      </b-link>
    </b-row>
    <b-row align-h="center" class="mb-3">
      <b-button v-if="isFrontPage && !isFeaturedSpace" :to="{ name: 'partners' }" class="secondary-button">Voir tous nos
        partenaires
      </b-button>
    </b-row>
  </b-container>
</template>

<script>
import Vue from 'vue'

import { partnersAPI } from '@/services/partners.api'

export default Vue.extend({
  name: 'Partners',
  props: [
    'isFrontPage',
    'isFeaturedSpace'
  ],
  data () {
    return {
      partners: []
    }
  },
  async created () {
    await partnersAPI.partnersList(this.isFrontPage || undefined, this.isFeaturedSpace).then(
      (response) => {
        console.log(response)
        this.partners = response
      }
    )
  },
  computed: {
    partnersSortedByOrder () {
      return this.partners.slice().sort((a, b) => a.order - b.order)
    }
  }
})
</script>

<style>
.partners-logo-style,
.card>img {
  object-fit: contain;
}

.card,
.modal-footer {
  border: none !important;
}
</style>
