<template>
  <b-container fluid>
    <b-row v-if="isFeaturedSpace" align-h="center" class="pt-3">
      <h1>Ils nous soutiennent</h1>
    </b-row>

    <vue-horizontal align-h="center" ref="horizontal" @scroll-debounce="onScrollDebounce" :displacement="displacement">
      <b-link
        v-b-modal="'modal-' + partner.name"
        v-for="(partner, index) in partnersSortedByOrder"
        :key="index" class="m-5">
        <b-img
          class="partners-logo-style"
          :src="partner.logo"
          width="200"
          height="100"/>
          <b-modal
            :id="'modal-' + partner.name"
            size="lg"
            centered
            ok-only
            hide-header
            ok-title="Fermer"
            ok-variant="secondary-button">
            <b-card
              :img-src="partner.logo"
              :img-alt="`Logo de notre partenaire ${partner.name}`"
              img-width="250"
              img-left
              class="px-3"
              :title="partner.name"
              title-tag="h1">
              <b-card-text>
                <p>{{ partner.description }}</p>
              </b-card-text>
              <b-card-text>
                <a :href="partner.website_url">Voir leur site</a>
              </b-card-text>
            </b-card>
          </b-modal>
        </b-link>
      </vue-horizontal>
    <b-row v-if="isFrontPage && !isFeaturedSpace" align-h="center" class="mb-3">
      <NuxtLink
        to="/PartnersPage"
        class="secondary-button">
        Voir tous nos partenaires
      </NuxtLink>
    </b-row>

  </b-container>
</template>

<script>
import Vue from "vue";
import VueHorizontal from 'vue-horizontal';
import { partnersAPI } from "../services/partners.api.ts";

export default Vue.extend({
  name: "Partners",
  props: ["isFrontPage", "isFeaturedSpace"],
  components: {
    VueHorizontal
  },
  data() {
    return {
      partners: [],
      hasPrev: false,
      hasNext: false,
      interval: null,
      // relative width to move when next/prev is clicked.
      displacement: 1.0,
    };
  },
  beforeMount() {
    partnersAPI
    .partnersList(this.isFrontPage || undefined, this.isFeaturedSpace)
    .then((res) => {
        this.partners = res
    })
  },
  mounted() {
    // Custom observe visibility is below
    // Much easier way: https://www.npmjs.com/package/vue-observe-visibility
    observeVisibility(this.$refs.horizontal.$el, (visible) => {
      if (visible) {
        this.interval = setInterval(this.play, 4000)
      } else {
        clearInterval(this.interval)
      }
    })
  },
  destroyed() {
    clearInterval(this.interval)
  },
  methods: {
    onScrollDebounce({hasNext, hasPrev}) {
      this.hasPrev = hasPrev
      this.hasNext = hasNext
    },
    play() {
      if (!this.hasNext && this.hasPrev) {
        this.$refs.horizontal.scrollToIndex(0)
        this.displacement = 1.0
        return
      }

      if (this.hasNext) {
        this.$refs.horizontal.next()

        // After first nav, change displacement window to just 60%
        this.displacement = 0.6
      }
    }
  },
  computed: {
    partnersSortedByOrder() {
      return this.partners.slice().sort((a, b) => a.order - b.order);
    },
  },
});


/**
 * Custom function, much easier way: https://www.npmjs.com/package/vue-observe-visibility
 *
 * @param element to track visibility
 * @param callback: function(boolean) when visibility change
 */
function observeVisibility(element, callback) {
  const observer = new IntersectionObserver((records) => {
    callback(records.find(record => record.isIntersecting))
  }, {rootMargin: '10% 0% 10% 0%', threshold: 1.0});
  observer.observe(element);
}

</script>

<style>
.partners-logo-style,
.card > img {
  object-fit: contain;
}

.card,
.modal-footer {
  border: none !important;
}

.horizontal >>> .v-hl-btn svg {
  border-radius: 0;
  margin: 0;
  padding: 8px;
  height: 100%;
  box-shadow: none;
  background: none;
}

.horizontal >>> .v-hl-btn-prev {
  background: linear-gradient(to left, #ffffff00 0, #fff 66%, #fff);
  padding-right: 24px;
}

.horizontal >>> .v-hl-btn-next {
  background: linear-gradient(to right, #ffffff00 0, #fff 66%, #fff);
  padding-left: 24px;
}

.horizontal >>> .v-hl-btn {
  top: 0;
  bottom: 0;
  transform: translateX(0);
}
</style>
