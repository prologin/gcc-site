<template>
  <b-container class="p-0" fluid>
    <FormPage />
  </b-container>
</template>

<script lang="ts">
import Vue from 'vue'
import FormPage from '@/components/FormPage.vue'

export default Vue.extend({
  name: 'Inscription',
  components: {
    FormPage
  }
})
</script>

<style scoped>
</style>
