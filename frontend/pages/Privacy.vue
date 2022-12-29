<template>
  <div class="main-body-style">
    <b-container class="p-0 content" fluid>
      <div class="basic-background">
        <Header />
        <h1 class="text-center m-3">
          Girls Can Code! (GCC!) et vos données personnelles
        </h1>
        <b-container class="accordion mb-1" role="tablist">
          <AccordionCard
            v-for="(privacy_element, index) in Constants.PRIVACY_LIST"
            :key="index"
            :index="index"
            :title="privacy_element.title"
            :content="privacy_element.content"
          />
        </b-container>
      </div>
    </b-container>
    <Footer />
  </div>
</template>

<script>
import Vue from 'vue';
import AccordionCard from '@/components/AccordionCard.vue';
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';

import * as Constants from '@/constants';

export default Vue.extend({
  name: 'Privacy',
  components: {
    AccordionCard,
    Footer,
    Header
  },
  created () {
    this.Constants = Constants
  }
})
</script>
