<template>
  <div class="main-body-style">
    <b-container class="p-0 content" fluid>
      <Header />
      <div class="candidatures-background">
        <div class="mr-5">
          <div class="col-9 offset-3">
            <b-row class="mt-5">
              <!--
                  TODO: Create a pluralize function.
                -->
              <h1>Candidature(s)</h1>
              <b-button class="primary-button ml-auto">
                S'inscrire à un stage
              </b-button>
            </b-row>
            <b-row class="mt-3">
              <ApplicationsList />
            </b-row>
          </div>
        </div>
      </div>
      <Footer />
    </b-container>
  </div>
</template>

<script>
import Vue from "vue";
import ApplicationsList from "@/components/ApplicationsListComponent.vue";
import Footer from "@/components/Footer.vue";
import Header from "@/components/Header.vue";

export default Vue.extend({
  name: 'Candidatures',
  middleware: 'auth',
  components: {
    Header,
    ApplicationsList,
    Footer
  },
})
</script>

<style scoped>
.candidatures-background {
  height: 100%;
  background-attachment: fixed;
  background-image: url("~@/assets/candidatures_bg.svg");
  background-position: top left;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
