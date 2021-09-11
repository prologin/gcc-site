<template>
    <div id="event-list" class="background-style pb-4">
        <section class="w-75 mx-auto pt-5">
            <EventCard v-for="(event, index) in events"
                       v-bind:index="index"
                       v-bind:key="event.id"
                       v-bind:title="event.title"
                       v-bind:date="event.date"
                       v-bind:address="event.address"/>
        </section>
    </div>
</template>

<script lang="ts">
import Vue from 'vue'
import EventCard from '@/components/EventCard.vue'

export default Vue.extend({
  name: 'EventList',
  props: {},
  components: {
    EventCard
  },
  data () {
    return {
      events: [
        { id: 1, title: 'Stage long à EPITA Paris', date: '12 janvier au 15 décembre 1245', address: 'EPITA Paris, 14-16 rue Voltaire, 94270 Le Kremlin-Bicêtre' },
        { id: 2, title: 'Stage court à EPITA Paris' },
        { id: 3, title: 'Stage long à EPITA Lyon' }
      ]
    }
  }
})
</script>

<style scoped>
.background-style {
    background-color: #efefef;
    background-image: url('../assets/event_list_bg.svg');
    background-repeat: no-repeat;
    background-size: cover;
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
