<template>
  <Schedules v-bind:scheduleType="scheduleType"/>
</template>

<script>
import Vue from 'vue'
import Schedules from '@/components/Schedules.vue'

export default Vue.extend({
  name: 'EventInfo',
  props: ['scheduleType'],
  components: {
    Schedules
  }
})
</script>

<style>
</style>
