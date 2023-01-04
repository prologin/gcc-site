<template>
  <div>
    <table class="table table-borderless">
      <thead>
        <tr>
          <th scope="col">Nom</th>
          <th scope="col">Status</th>
          <th scope="col">Infos</th>
          <th scope="col" />
        </tr>
      </thead>
      <AppCardAdmin
        v-for="(app, index) in applications"
        :key="index"
        :app_id="app.id"
      />
    </table>

    <b-button variant="primary"> Sauvegarder </b-button>
  </div>
</template>
<script>
import Vue from "vue";
import { applicationsAPI } from "../services/applications.api";
import AppCardAdmin from './ApplicationCardAdmin.vue';

export default Vue.extend({
  name: "ApplicationListAdmin",
  components: {
    AppCardAdmin,
  },
  props: ["event_id"],
  data() {
    return { applications: [] };
  },
  created () {
    applicationsAPI.applicationsList(null, this.event_id).then((res) => {
      this.applications = res
    });
  }
});
</script>

<style></style>
