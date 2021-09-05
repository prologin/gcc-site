<template>
    <div class="background-style pb-4">
        <section class="w-75 mx-auto pt-5">
            <EventCard v-for="post in posts"
                       v-bind:key="post.id"
                       v-bind:title="post.title"
                       v-bind:date="post.date"
                       v-bind:adress="post.adress"/>
        </section>
    </div>
</template>

<script lang="ts">
import Vue from 'vue'
import EventCard from './EventCard.vue'

export default Vue.extend({
  name: 'EventList',
  props: {},
  components: {
    EventCard
  },
  data () {
    return {
      posts: [
        { id: 1, title: 'Stage long à EPITA Paris', date: '12 janvier au 15 décembre 1245', adress: 'EPITA Paris, 14-16 rue Voltaire, 94270 Le Kremlin-Bicêtre' },
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

.btn-group-vertical > button{
    margin-bottom:5px;
    border-radius:12px !important;
}
</style>
