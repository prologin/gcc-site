<template>
  <b-container fluid>
    <h1>Emploi du temps type :</h1>
    <!-- This is ugly but it works ¯\_(ツ)_/¯ -->
    <b-table-simple small caption-top bordered responsive style="background-color:var(--main-light-color)">
      <b-thead head-variant="dark">
        <b-tr>
          <b-th />
            <b-th v-for="(schedule, index) in schedules" :key="index">{{ schedule.day }}</b-th>
        </b-tr>
      </b-thead>
      <b-tbody>
        <b-tr v-for="index in 11" :key="index">
          <b-th class="text-nowrap" variant="dark">{{ globalStartHour - 1 + index }} h 00</b-th>
          <b-th v-for="(activity, key) in activitiesAtHour(globalStartHour - 1 + index)" :key="key" :rowspan="activity.duration" class="content-background">
            <h3><strong>{{ activity.title }}</strong></h3>
            <h4 style="color:var(--light-text-color)"><em>{{ globalStartHour - 1 + index }} h 00 - {{ globalStartHour - 1 + index + activity.duration }} h 00</em></h4>
          </b-th>
        </b-tr>
      </b-tbody>
    </b-table-simple>
  </b-container>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'Schedules',
  data () {
    return {
      globalStartHour: 8,
      schedules: [
        {
          day: 'Lundi',
          activities: [
            {
              title: 'Accueil et petit déjeuner',
              start: 9,
              duration: 1
            },
            {
              title: 'Introduction et présentation',
              start: 10,
              duration: 2
            },
            {
              title: 'Prise en main',
              start: 12,
              duration: 1
            },
            {
              title: 'Repas',
              start: 13,
              duration: 1
            },
            {
              title: 'Initiation au Python',
              start: 14,
              duration: 4
            }
          ]
        },
        {
          day: 'Mardi',
          activities: [
            {
              title: 'Accueil et petit déjeuner',
              start: 9,
              duration: 1
            },
            {
              title: 'Python',
              start: 10,
              duration: 2
            },
            {
              title: 'Repas',
              start: 12,
              duration: 2
            },
            {
              title: 'Python',
              start: 14,
              duration: 4
            }
          ]
        },
        {
          day: 'Mercredi',
          activities: [
            {
              title: 'Accueil et petit déjeuner',
              start: 9,
              duration: 1
            },
            {
              title: 'Découverte de la cryptologie',
              start: 10,
              duration: 2
            },
            {
              title: 'Repas',
              start: 12,
              duration: 1
            },
            {
              title: 'Activité surprise',
              start: 13,
              duration: 5
            }
          ]
        },
        {
          day: 'Jeudi',
          activities: [
            {
              title: 'Accueil et petit déjeuner',
              start: 9,
              duration: 1
            },
            {
              title: 'Découverte du web et du réseau',
              start: 10,
              duration: 2
            },
            {
              title: 'Repas',
              start: 12,
              duration: 2
            },
            {
              title: 'Projets',
              start: 14,
              duration: 4
            }
          ]
        },
        {
          day: 'Vendredi',
          activities: [
            {
              title: 'Accueil et petit déjeuner',
              start: 9,
              duration: 1
            },
            {
              title: 'Projets',
              start: 10,
              duration: 1
            },
            {
              title: 'Conférence',
              start: 11,
              duration: 1
            },
            {
              title: 'Repas',
              start: 12,
              duration: 2
            },
            {
              title: 'Projets',
              start: 14,
              duration: 4
            }
          ]
        },
        {
          day: 'Samedi',
          activities: [
            {
              title: 'Accueil et petit déjeuner',
              start: 9,
              duration: 1
            },
            {
              title: 'Conférence',
              start: 10,
              duration: 1
            },
            {
              title: 'Projets',
              start: 11,
              duration: 2
            },
            {
              title: 'Repas',
              start: 13,
              duration: 2
            }
          ]
        }
      ]
    }
  },
  methods: {
    activitiesAtHour (hour) {
      var activities = []
      for (var day in this.schedules) {
        var dayActivities = this.schedules[day].activities
        for (var activity in dayActivities) {
          if (dayActivities[activity].start === hour) {
            activities.push(dayActivities[activity])
          }
        }
      }
      return activities
    }
  }
})
</script>

<style>
</style>
