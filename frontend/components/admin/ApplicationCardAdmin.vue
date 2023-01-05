<template>
  <!--faire le modal ici-->
  <b-modal> TODO </b-modal>
</template>
<script>
import Vue from "vue";
import { applicationsAPI } from "../../services/applications.api";

export default Vue.extend({
  name: "ApplicationCardAdmin",
  props: ["app_id"],
  data() {
    return { app: [] };
  },
  created() {
    applicationsAPI.applicationsRead(this.app_id).then((res) => {
      this.app = res;
    })
  },
  methods: {
    rejectApp () {
      console.log('Application Rejete');
    },
  }
});
</script>

<style></style>
