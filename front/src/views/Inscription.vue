<template>
  <ContactInformationComponent />
</template>

<script lang="ts">
import Vue from 'vue'
import ContactInformationComponent from '@/components/ContactInformationComponent.vue'

export default Vue.extend({
  name: 'Inscription',
  components: {
    ContactInformationComponent
  }
})
</script>
