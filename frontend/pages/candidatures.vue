<template>
  <div class="main-body-style">
    <b-container fluid class="p-0">
      <!-- Header -->
      <Header />


      <!-- Footer -->
      <Footer />
    </b-container>
  </div>
</template>

<script>
import Vue from "vue";
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import { applicationsAPI } from "../services/applications.api"

export default Vue.extend({
  name: "Candidatures",
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      applications: [],
      showError: false
    }
  },
  beforeMount() {
    applicationsAPI
    .applicationsList(this.id)
    .then((response) => {
      this.showError = false;
      this.applications = response;
    },
    () => {
      this.showError = true;
    })
  }
});
</script>