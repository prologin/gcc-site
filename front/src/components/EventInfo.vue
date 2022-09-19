<template>
  <b-container fluid style="margin-bottom: 5%;">
    <div slot="modal-header" style="position: relative; text-align: center; margin-bottom: 20px;">
      <img class="menu-logo" :src="require('@/assets/logo_gcc.svg')"
        alt="Logo des stages Girls Can Code" />
    </div>
    <b-row class="p-3 d-flex" style="flex-direction: column;">
      <hr class="eventInfo-line" :class="colorClass + '-back'" md="auto" />
      <b-tbody class="mb-4">
        <h1 >Stage : {{ this.info.name }}</h1>
        <b-row align-h="around" class="m-3">
          <b-row class="m-3">
            <b-img :src="require('@/assets/logo-calendar.svg')" class="eventInfo-icon" />
            <ul style="list-style: none; margin: 0; padding: 0px;">
                <li><h2>{{ startdate }}</h2></li>
                <li><h2>{{ enddate }}</h2></li>
            </ul>
          </b-row>
          <b-row class="m-3">
            <b-img :src="require('@/assets/logo-localisation.svg')" class="eventInfo-icon" />
            <ul style="list-style: none; margin: 0; padding: 0px;">
              <li><h2>{{ this.info.center.address.street }} {{ this.info.center.address.complement }}</h2></li>
              <li><h2>{{ this.info.center.address.city}} ({{ this.info.center.address.zip_code }})</h2></li>
            </ul>
          </b-row>
        </b-row>
        <h2>{{ this.info.description }}</h2>
      </b-tbody>
      <b-button-group class="mx-auto m-5 mb-1 my-lg-auto">
        <b-button class="mx-auto ml-lg-auto mr-lg-4 primary-button">S'inscrire à ce stage</b-button>
        <b-button v-b-modal="'modal'"
                  class="mx-auto ml-lg-auto mr-lg-4 secondary-button">
          Calendrier du stage
        </b-button>
      </b-button-group>
      <b-modal :id="'modal'"
                size="xl"
                centered
                hide-footer
                headerClass='p-2 border-bottom-0'
                ok-variant="secondary-button">
        <Schedules v-bind:scheduleType="scheduleType"/>
      </b-modal>
    </b-row>

  </b-container>
</template>

<script>
import Vue from 'vue'
import { eventsAPI } from '@/services/events.api'
import Schedules from '@/components/Schedules.vue'
import { formatDate } from '@/services/date'

export default Vue.extend({
  name: 'EventInfo',
  props: ['id', 'colorClass', 'scheduleType'],
  data () {
    return {
      info: {
        center: {
          address: {
            city: '',
            complement: '',
            country: '',
            id: '',
            lat: '',
            lng: '',
            street: '',
            zip_code: ''
          },
          id: '',
          name: ''
        },
        description: '',
        end_date: '',
        form_id: '',
        id: '',
        name: '',
        notes: '',
        signup_end_date: '',
        signup_start_date: '',
        start_date: ''
      }
    }
  },
  computed: {
    startdate: function () {
      return 'Début : ' + formatDate(this.info.start_date)
    },
    enddate: function () {
      return 'Fin : ' + formatDate(this.info.end_date)
    }
  },
  async created () {
    await eventsAPI.eventsRead(this.id).then(
      (response) => {
        this.info = response
      },
      () => {
        this.showError = true
      }
    )
  },
  components: {
    Schedules
  }

})
</script>

<style>
.modal-header {
  border: none;
}

.eventInfo-line {
  margin: 0;
  height: 3px;
  width: 100%;
  margin-bottom: 2%;
  border-radius: 40%;
}
.gcc-pink-back {
  background-color: var(--gcc-pink-color);
}
.gcc-green-back {
  background-color: var(--gcc-green-color);
}
.gcc-blue-back {
  background-color: var(--gcc-blue-color);
}
.eventInfo-icon {
  min-width: 60px;
  max-width: 60px;
  padding-right: 25px;
}
</style>
