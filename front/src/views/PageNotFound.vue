<template>
    <b-container fluid>
      <Menu />
      <b-row class="background-image">
        <b-col class="my-auto content-background" md="auto" offset-md="6">
          <p class="text-center">
          <span class="error-code">404</span><br>
          <span class="error-message">Page introuvable</span><br>
          </p>
          <b-button :to="{ name: 'home' }" class="primary-button" block>Retour a l'accueil</b-button>
          <span class="light-text">Si vous pensez que ceci est une erreur, envoyez un mail à info@prologin.org</span>
        </b-col>
      </b-row>
    </b-container>
</template>

<script>
import Vue from 'vue'
import Menu from '@/components/Menu.vue'

export default Vue.extend({
  name: 'PageNotFound',
  components: {
    Menu
  }
})
</script>

<style>
.background-image {
  min-height: 90vh;
  background-color: white;
  background-image: url('~@/assets/page_not_found_bg.svg');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
}

.error-code {
  font-size: 1000%;
  font-weight: bold;
}

.error-message {
  font-size: 300%;
}

.light-text {
  color: #37474F;
  font-weight: 400;
  font-size: 80%;
}
</style>
