<template>
  <div v-if="isFrontPage">
    <b-row class="event-card mb-4 p-3">
      <b-col class="my-auto d-none d-sm-block" md="auto">
        <b-icon :class="colorClass" icon="circle-fill" aria-hidden="true" />
      </b-col>
      <!-- Event infos verticaly centered -->
      <b-col class="col-lg-auto">
        <h1>{{ title }}</h1>
        <h2>{{ date }}</h2>
        <h3>{{ address }}</h3>
      </b-col>

      <b-button-group vertical class="col-lg-auto ml-auto mt-4 mb-1 my-lg-auto">
        <b-button class="mx-auto ml-lg-auto mr-lg-4 primary-button"
          >S'inscrire à ce stage</b-button
        >
        <b-button
          v-b-modal="'modal-' + index"
          class="mx-auto ml-lg-auto mr-lg-4 secondary-button"
        >
          Plus d'informations
        </b-button>

        <!--
          TODO: Add "S'inscrire à ce stage" button in the following modal
          component.
        -->
        <b-modal
          :id="'modal-' + index"
          size="xl"
          centered
          hide-footer
          headerClass="p-2 border-bottom-0"
          ok-variant="secondary-button"
        >
          <EventInfo
            v-bind:id="id"
            v-bind:colorClass="colorClass"
            v-bind:scheduleType="scheduleType"
          />
        </b-modal>
      </b-button-group>
    </b-row>
  </div>

  <div v-else>
    <b-row class="event-card mb-4 p-3">
      <b-col class="my-auto d-none d-sm-block" md="auto">
        <b-icon :class="colorClass" icon="circle-fill" aria-hidden="true" />
      </b-col>
      <!-- Event infos verticaly centered -->
      <b-col class="d-none d-sm-block" md="2">
        {{ title }}
      </b-col>
      <!-- type -->
      <b-col>
        {{ CampsType[camps_type] }}
      </b-col>
      <b-col>
        {{ date }}
      </b-col>
      <b-col>
        {{ address }}
      </b-col>
      <b-col>
        <NuxtLink to="/review">
          Review
        </NuxtLink>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import Vue from "vue";
import EventInfo from "@/components/EventInfo.vue";
import ScheduleTypeEnum from "@/enums/ScheduleTypeEnum.js";
import { formatDate } from "@/services/date";

const CampsType = {
  short: "Stage Court",
  long: "Stage Long"
};

export default Vue.extend({
  name: "EventCard",
  components: {
    EventInfo
  },
  mixins: [ScheduleTypeEnum.Mixin],
  props: [
    "isFrontPage",
    "title",
    "camps_type",
    "id",
    "start_date",
    "end_date",
    "address",
    "index",
    "scheduleType",
  ],
  computed: {
    colorClass: function () {
      const colors = ['gcc-pink', 'gcc-green', 'gcc-blue'];
      return colors[this.index % colors.length];
    },
    date: function () {
      return (
        "Du " + formatDate(this.start_date) + " au " + formatDate(this.end_date)
      );
    },
  },
  data() {
    return {
      CampsType
    }
  }
});
</script>

<style>
.event-card {
  background-color: #ffffff;
  border-radius: 12px;
}

.btn-group-vertical > button {
  margin-bottom: 5px;
  border-radius: 12px !important;
}
</style>
