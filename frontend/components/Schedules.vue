<template>
  <b-container fluid>
    <h1>Emploi du temps type :</h1>
    <!-- This is ugly but it works ¯\_(ツ)_/¯ -->
    <b-table-simple
      small
      caption-top
      bordered
      responsive
      style="background-color: var(--main-light-color)"
    >
      <b-thead head-variant="dark">
        <b-tr>
          <b-th />
          <b-th v-for="(schedule, index) in schedules" :key="index">
            {{ schedule.day }}
          </b-th>
        </b-tr>
      </b-thead>
      <b-tbody>
        <b-tr v-for="index in 11" :key="index">
          <b-th class="text-nowrap" variant="dark">
            {{ globalStartHour - 1 + index }} h 00
          </b-th>
          <b-th
            v-for="(activity, key) in activitiesAtHour(
              globalStartHour - 1 + index
            )"
            :key="key"
            :rowspan="activity.duration"
            class="content-background"
          >
            <h3>
              <strong>{{ activity.title }}</strong>
            </h3>
            <h4 style="color: var(--light-text-color)">
              <em>{{ globalStartHour - 1 + index }} h 00 -
                {{ globalStartHour - 1 + index + activity.duration }} h 00</em>
            </h4>
          </b-th>
        </b-tr>
      </b-tbody>
    </b-table-simple>
  </b-container>
</template>

<script>
import Vue from 'vue';
import ScheduleTypeEnum from '@/enums/ScheduleTypeEnum.js';
import { scheduleAPI } from '@/services/schedule.api';

export default Vue.extend({
  name: 'Schedules',
  mixins: [ScheduleTypeEnum.Mixin],
  props: ['scheduleType'],
  data () {
    return {
      globalStartHour: 8,
      schedules: null
    };
  },
  created () {
    if (this.scheduleType === ScheduleTypeEnum.WEEKEND) {
      this.schedules = scheduleAPI.getWeekEndSchedule()
    } else if (this.scheduleType === ScheduleTypeEnum.WEEK) {
      this.schedules = scheduleAPI.getWeekSchedule()
    }
  },
  methods: {
    activitiesAtHour (hour) {
      const activities = [];
      for (const day in this.schedules) {
        const dayActivities = this.schedules[day].activities;
        for (const activity in dayActivities) {
          if (dayActivities[activity].start === hour) {
            activities.push(dayActivities[activity])
          }
        }
      }
      return activities
    },
  }
});
</script>

<style></style>
