<template>
  <div>
    <ContactInformationComponent />
    <ParticipantInformationComponent />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import ContactInformationComponent from '@/components/ContactInformationComponent.vue'
import ParticipantInformationComponent from '@/components/ParticipantInformationComponent.vue'

export default Vue.extend({
  name: 'Inscription',
  components: {
    ContactInformationComponent,
    ParticipantInformationComponent
  }
})
</script>
