<template>
  <b-container fluid class="event-list-background pb-4">
    <section v-if="!events || events.length < 1 || showError">
      <!-- Empty list -->
      <b-row no-gutters fluid="sm" align-v="baseline" align-h="center">
        <b-col md="4">
          <b-img :src="require('@/assets/no-event.svg')" />
        </b-col>
        <b-col v-if="showError" md="4" align="center">
          <h1>Nous ne pouvons pas afficher les stages pour le moment.</h1>
          <h3>
            Une erreur technique est survenue. Veuillez nous excuser pour la
            gêne occasionnée. Nous vous invitons à réessayer ultérieurement et
            restons à votre disposition par mail à {{ Constants.CONTACT_EMAIL }}
          </h3>
        </b-col>
        <b-col v-else md="4" align="center">
          <h1>Malheureusement, il n'y a pas de stages pour le moment...</h1>
          <h3>
            Vous pouvez vous inscrire à notre newsletter afin de recevoir un
            mail lorsqu'un nouveau stage est disponible.
          </h3>
          <Newsletter />
        </b-col>
      </b-row>
    </section>
    <section v-else class="w-75 mx-auto pt-5">
      <EventCard
        v-for="(event, index) in events"
        :id="event.id"
        :key="event.id"
        :index="index"
        :title="event.name"
        :start_date="event.start_date"
        :end_date="event.end_date"
        :signup_start_date="event.singup_start_date"
        :signup_end_date="event.singup_end_date"
        :address="event.center.name"
        schedule-type="WEEKEND"
      />
    </section>
  </b-container>
</template>

<script>
import Vue from 'vue';
import { eventsAPI } from "../services/events.api";
import * as Constants from '../constants';
import EventCard from './EventCard.vue';
import Newsletter from './Newsletter.vue';

export default Vue.extend({
  name: "EventList",
  components: {
    EventCard,
    Newsletter
  },
  props: {},
  data() {
    return {
      events: null,
      showError: false,
      Constants
    };
  },
  async created() {
    await eventsAPI.eventsList(true).then(
      (response) => {
        this.showError = false;
        this.events = response;
      },
      () => {
        this.showError = true;
      }
    );
  },
});
</script>

<style scoped>
.event-list-background {
  background-color: #efefef;
  background-image: url("~@/assets/event_list_bg.svg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: top 0 right 0;
}

.event-card {
  background-color: #ffffff;
  border-radius: 12px;
}

.btn-group-vertical > button {
  margin-bottom: 5px;
  border-radius: 12px !important;
}
</style>
