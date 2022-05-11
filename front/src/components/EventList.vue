<template>
  <b-container fluid class="event-list-background pb-4">
    <section v-if="!events || events.length < 1 || showError">
      <!-- Empty list -->
      <b-row
        no-gutters
        fluid="sm"
        align-v="baseline"
        align-h="center"
        >
        <b-col md="4">
          <b-img :src="require('@/assets/no-event.svg')"/>
        </b-col>
        <b-col md="4" align="center" v-if="showError">
          <h1>Nous ne pouvons afficher les stages pour le moment.</h1>
          <h3>Une erreur technique est survenue. Veuillez nous excuser pour la gêne occasionnée. Nous vous invitons à réessayer ultérieurement et restons à votre disposition par mail à info@prologin.org</h3>
        </b-col>
        <b-col md="4" align="center" v-else>
          <h1>Malheureusement, il n'y a pas de stages pour le moment...</h1>
          <h3>Vous pouvez vous inscrire à notre newsletter afin de recevoir un mail lorsqu'un nouveau stage est disponible.</h3>
          <Newsletter />
        </b-col>
      </b-row>
    </section>
    <section v-else class="w-75 mx-auto pt-5">
      <EventCard v-for="(event, index) in events"
                 v-bind:index="index"
                 v-bind:key="event.id"
                 v-bind:title="event.title"
                 v-bind:date="event.date"
                 v-bind:address="event.address"
                 scheduleType="WEEKEND"/>
    </section>
  </b-container>
</template>

<script lang="ts">
import Vue from 'vue'
import EventCard from '@/components/EventCard.vue'
import Newsletter from '@/components/Newsletter.vue'
import { eventsAPI } from '@/services/events.api'

export default Vue.extend({
  name: 'EventList',
  props: {},
  components: {
    EventCard,
    Newsletter
  },
  data () {
    return {
      events: null,
      showError: false
    }
  },
  async created () {
    const [error, events] = await eventsAPI.getEventList()

    if (error) {
      this.showError = true
    } else {
      this.showError = false
      this.events = events
    }
  }
})
</script>

<style scoped>
.event-list-background {
  background-color: #efefef;
  background-image: url('~@/assets/event_list_bg.svg');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: top 0 right 0;
}

.event-card {
  background-color: #FFFFFF;
  border-radius: 12px;
}

.btn-group-vertical > button {
  margin-bottom:5px;
  border-radius:12px !important;
}
</style>
