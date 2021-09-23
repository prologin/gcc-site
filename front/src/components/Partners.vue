<template>
  <b-container fluid>
    <b-row align-h="center">
      <b-link v-b-modal="'modal-' + sponsor.name" v-for="(sponsor, index) in sponsorsSortedByOrder" :key="index">
        <b-img class="sponsors-logo-style m-5"
          v-show="displayLogo(sponsor)"
          :src="require(`@/assets/${sponsor.imgName}`)"
          width="200"
          height="100" />
          <b-modal :id="'modal-' + sponsor.name"
            size="lg"
            centered
            ok-only
            hide-header
            ok-title="Fermer"
            ok-variant="secondary-button">
            <b-card
              :img-src="require(`@/assets/${sponsor.imgName}`)"
              img-alt="Logo de notre partenaire"
              img-width=250
              img-left
              class="px-3"
              :title="sponsor.name"
              title-tag="h1">

              <b-card-text>
                <p>{{ sponsor.description }}</p>
              </b-card-text>
              <b-card-text>
                <a :href="sponsor.link">Voir leur site</a>
              </b-card-text>
            </b-card>
          </b-modal>
      </b-link>
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
          name: 'Epita',
          link: 'https://epita.fr',
          imgName: 'epita-logo.png',
          order: 3,
          isInFrontPage: true,
          description: 'lalalalalalala aaaaaaaaaaaaaaa zzzzzzzzzzz eeeeeeeeeeeeeeeee rrrrrrrrrrrrrrrr tttttttt'
        },
        {
          name: 'Ministere',
          link: 'https://epita.fr',
          imgName: 'ministere-logo.png',
          order: 4,
          isInFrontPage: false,
          description: 'lalalalalalala aaaaaaaaaaaaaaa zzzzzzzzzzz eeeeeeeeeeeeeeeee rrrrrrrrrrrrrrrr tttttttt'

        },
        {
          name: 'Strasbourg',
          link: 'https://epita.fr',
          imgName: 'strasbourg-logo.png',
          order: 1,
          isInFrontPage: false,
          description: 'lalalalalalala aaaaaaaaaaaaaaa zzzzzzzzzzz eeeeeeeeeeeeeeeee rrrrrrrrrrrrrrrr tttttttt'

        },
        {
          name: 'KB',
          link: 'https://epita.fr',
          imgName: 'kb-logo.png',
          order: 2,
          isInFrontPage: true,
          description: 'lalalalalalala aaaaaaaaaaaaaaa zzzzzzzzzzz eeeeeeeeeeeeeeeee rrrrrrrrrrrrrrrr tttttttt'

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
.sponsors-logo-style, .card > img {
  object-fit: contain;
}

.card, .modal-footer {
  border: none !important;
}

</style>
