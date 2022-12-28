<template>
  <b-row class="code-background">
    <b-col class="p-0">
      <!-- TODO: add optimized images -->
      <img
        class="w-100"
        :src="require('@/assets/gcc-affiche-2022.jpg')"
        alt="Affiche GCC decoration"
      />
    </b-col>
    <b-col md="8" class="white-background">
      <b-form @submit="submitAnswers">
        <ContactInformationComponent />
        <ParticipantInformationComponent />
        <QuestionsComponent />

        <b-row align-h="end">
          <b-col cols="4">
            <b-button type="submit" class="primary-button" block>
              Continuer
            </b-button>
          </b-col>
        </b-row>
      </b-form>
    </b-col>
  </b-row>
</template>

<script>
import Vue from 'vue';
import ContactInformationComponent from '@/components/ContactInformationComponent.vue';
import ParticipantInformationComponent from '@/components/ParticipantInformationComponent.vue';
import QuestionsComponent from '@/components/QuestionsComponent.vue';

export default Vue.extend({
  name: 'Inscription',
  components: {
    ContactInformationComponent,
    ParticipantInformationComponent,
    QuestionsComponent
  },
  methods: {
    submitAnswers: function (event) {
      event.preventDefault()
      console.log('TOTO');
    }
  },
})
</script>

<style scoped>
.white-background {
  background-color: white;
}

.code-background {
  height: 100%;
  background-attachment: fixed;
  background-color: var(--main-light-color);
  background-image: url("~@/assets/faq_bg.svg");
  background-repeat: no-repeat;
  background-size: 70%;
  background-position: left bottom;
}
</style>
