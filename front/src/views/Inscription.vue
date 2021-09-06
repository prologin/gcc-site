<template>
  <b-container class="p-0" fluid>
    <div class="form-page-image-background" />
    <div class="form-page-below-background" />
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
.form-page-image-background {
  background-color: black;
  width: 100%;
  height: 30%;
  min-height: 15em;
  margin: 0;
}

.form-page-below-background {
  background-color: #F9F9F9;
  width: 100%;
  height: 70%;
  min-height: 70em;
}
</style>
