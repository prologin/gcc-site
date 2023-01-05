<template>
  <div class="main-body-style">
    <b-container fluid class="p-0">
      <!-- Header -->
      <Header />

      <div class="basic-background">
        <div class="w-75 mx-auto table-responsive">
          <AppListAdmin :event_id="eventID" />
        </div>
      </div>
      <div>
        <p>Event ID : {{ eventID }}</p>
        <p>Event Date : {{ eventDATE }}</p>
      </div>

      <!-- Footer -->
      <Footer />
    </b-container>
  </div>
</template>

<script>
import Vue from 'vue';
import Header from '@/components/Header.vue';
import AppListAdmin from "@/components/admin/ApplicationListAdmin.vue"
import Footer from '@/components/Footer.vue';
import { applicationsAPI } from '@/services/applications.api';

export default Vue.extend({
  name: 'Candidatures',
  components: {
    Header,
    AppListAdmin,
    Footer
  },
  data () {
    return {
      eventID: this.$route.params.id,
      eventDATE: this.$route.params.edition,
      applications: [],
      showError: false,
    }
  },
  beforeMount () {
    applicationsAPI.applicationsList(this.id).then(
      (response) => {
        this.showError = false;
        this.applications = response;
      },
      () => {
        this.showError = true;
      }
    );
  },
});
</script>
