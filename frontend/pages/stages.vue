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
                <th scope="col"> </th>
                <th scope="col">Nom</th>
                <th scope="col">Durée</th>
                <th scope="col">Date</th>
                <th scope="col"> </th>
              </tr>
            </thead>
            <EventCard
              v-for="(event, index) in eventsSortedByDate"
              v-bind:isFrontPage="false"
              v-bind:index="index"
              v-bind:key="event.id"
              v-bind:title="event.name"
              v-bind:camps_type="event.camps_type"
              v-bind:id="event.id"
              v-bind:start_date="event.start_date"
              v-bind:end_date="event.end_date"
              v-bind:address="event.center.name"/>
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
import { eventsAPI } from "../services/events.api";


export default Vue.extend({
  name: "Stages",
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      events: [],
      showError: false
    };
  },
  beforeMount() {
    eventsAPI
    .eventsList(false)
    .then((response) => {
      this.showError = false;
      this.events = response;
    },
    () => {
      this.showError = true;
    })
  },
  computed: {
    eventsSortedByDate(){
      return this.events.slice().sort((a,b) => (new Date(b.start_date)) - (new Date(a.start_date)));
    }
  },
});
</script>
