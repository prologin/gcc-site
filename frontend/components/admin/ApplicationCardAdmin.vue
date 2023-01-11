<template>
  <!--faire le modal ici-->
  <b-modal
    :id="'modal-' + app.user"
    centered
    ok-title="Fermer"
    ok-variant="secondary-button"
    size="xl"
  >
    <span :id="app.user"> {{ user.particaptions_count }} </span>
  </b-modal>
</template>
<script>
import Vue from "vue";
import { applicationsAPI } from "../../services/applications.api";
import { eventsAPI } from "../../services/events.api";
import { usersAPI } from "../../services/users.api";

export default Vue.extend({
  name: "ApplicationCardAdmin",
  props: ["app_id", "event_id"],
  data() {
    return { app: [], form: {}, user: [] }
  },
  created() {
    applicationsAPI.applicationsRead(this.app_id).then((res) => {
      this.app = res;
    })
    eventsAPI.eventsForm(this.event_id).then((res) => {
      this.form = res;
    })
    usersAPI.usersMeRead(this.app.user).then((res) => {
      this.user = res;
    })
  },
})
</script>

<style></style>
