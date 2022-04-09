<template>
  <div>
    <ContactInformationComponent />
    <ParticipantInformationComponent />
    <QuestionsComponent />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import ContactInformationComponent from '@/components/ContactInformationComponent.vue'
import ParticipantInformationComponent from '@/components/ParticipantInformationComponent.vue'
import QuestionsComponent from '@/components/QuestionsComponent.vue'

export default Vue.extend({
  name: 'Inscription',
  components: {
    ContactInformationComponent,
    ParticipantInformationComponent,
    QuestionsComponent
  }
})
</script>
