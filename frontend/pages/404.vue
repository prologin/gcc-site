<template>
  <div class="main-body-style">
    <b-container class="content" fluid>
      <Header />
      <b-row class="page-not-found-background">
        <b-col class="my-auto content-background" md="auto" offset-md="6">
          <p class="text-center">
            <span class="error-code">404</span><br />
            <span class="error-message">Page introuvable</span><br />
          </p>
          <NuxtLink to="/" class="primary-button" block
            >Retour a l'accueil</NuxtLink
          >
          <span class="light-text"
            >Si vous pensez que ceci est une erreur, envoyez un mail à
            {{ Constants.CONTACT_EMAIL }}</span
          >
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Vue from "vue";
import Header from "@/components/Header.vue";

import * as Constants from "@/constants";

export default Vue.extend({
  props: ["error"],
  name: "error",
  components: {
    Header,
  },
  created() {
    this.Constants = Constants;
  },
});
</script>

<style scoped>
.page-not-found-background {
  min-height: 90vh;
  background-color: white;
  background-image: url("~@/assets/page_not_found_bg.svg");
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
  color: #37474f;
  font-weight: 400;
  font-size: 80%;
}
</style>