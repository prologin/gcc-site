<template>
  <div class="main-body-style">
    <b-container fluid class="p-0">
      <!-- Header -->
      <Header />
      <div class="basic-background">
        <div class="w-75 mx-auto table-responsive">
          <table class="table table-borderless">
            <thead>
              <tr>
                <th scope="col" />
                <th scope="col">Nom</th>
                <th scope="col">Durée</th>
                <th scope="col">Date</th>
                <th scope="col" />
              </tr>
            </thead>
            <EventCardAdmin
              v-for="(event, index) in eventsSortedByDate"
              :id="event.id"
              :key="event.id"
              :index="index"
              :title="event.name"
              :camps_type="event.camps_type"
              :start_date="event.start_date"
              :end_date="event.end_date"
            />
          </table>
        </div>
      </div>
      <!-- Footer -->
      <Footer />
    </b-container>
  </div>
</template>

<script>
import Vue from "vue";
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import EventCardAdmin from "../components/admin/EventCardAdmin.vue";
import { eventsAPI } from "../services/events.api";

export default Vue.extend({
  name: "Stages",
  components: {
    Header,
    EventCardAdmin,
    Footer,
  },
  data() {
    return {
      events: [],
      showError: false
    }
  },
  computed: {
    eventsSortedByDate () {
      return this.events
        .slice()
        .sort((a, b) => new Date(b.start_date) - new Date(a.start_date));
    },
  },
  beforeMount () {
    eventsAPI.eventsList(false).then(
      (response) => {
        this.showError = false
        this.events = response;
      },
      () => {
        this.showError = true
      }
    )
  },
})
</script>
