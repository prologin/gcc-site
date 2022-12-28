<template>
  <b-container fluid class="faq-background p-2 p-sm-0">
    <b-row class="w-100">
      <b-col class="col-12 col-sm-8">
        <b-img
          :src="require('@/assets/photo_1.png')"
          alt="Photo des stages Girls Can Code!"
          fluid
        />
        <b-col class="content-background ml-1 ml-sm-5 mr-1 p-3">
          <h1>Foire Aux Questions</h1>
          <div class="accordion p-1" role="tablist">
            <AccordionCard
              v-for="(faq_elt, index) in Constants.FAQ_ENTRIES"
              :key="index"
              :index="index"
              :title="faq_elt.question"
              :content="faq_elt.answer"
            />
          </div>
        </b-col>
      </b-col>
      <b-col class="d-none d-sm-block">
        <b-img
          :src="require('@/assets/photo_2.png')"
          alt="Photo des stages Girls Can Code!"
          fluid
        />
      </b-col>
    </b-row>
    <b-row class="w-100">
      <b-col class="d-none d-sm-block">
        <b-img
          :src="require('@/assets/photo_3.png')"
          alt="Photo des stages Girls Can Code!"
          fluid
        />
      </b-col>
      <b-col>
        <b-img
          :src="require('@/assets/photo_4.png')"
          alt="Photo des stages Girls Can Code!"
          fluid
        />
        <b-col class="content-background mt-5 p-4 mx-auto back-mode">
          <h1>Une question ?</h1>
          <p>
            Si vous avez une question qui ne figure pas dans la FAQ, vous pouvez
            nous envoyer un mail à l'adresse suivante :
          </p>
          <h3>{{ Constants.CONTACT_EMAIL }}</h3>
        </b-col>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Vue from 'vue';
import AccordionCard from '@/components/AccordionCard.vue';

import * as Constants from '@/constants';

export default Vue.extend({
  name: 'FAQ',
  components: {
    AccordionCard
  },
  created () {
    this.Constants = Constants
  },
})
</script>

<style scoped>
.faq-background {
  background-color: #efefef;
  background-image: url(~@/assets/faq_bg.svg);
  background-size: contain;
  background-repeat: no-repeat;
  background-position: bottom 0 right 0;
}
</style>
