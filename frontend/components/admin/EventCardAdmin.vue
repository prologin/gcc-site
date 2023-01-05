<template>
  <tbody>
    <tr>
      <th scope="row">
        <b-icon :class="colorClass" icon="circle-fill" aria-hidden="true" />
      </th>
      <td>{{ title }}</td>
      <td>{{ CampsType[camps_type] }}</td>
      <td>{{ date }}</td>
      <td>
        <NuxtLink
          class="primary-button px-2 py-2"
          style="color: white"
          :to="path"
        >
          Review
        </NuxtLink>
      </td>
    </tr>
  </tbody>
</template>

<script>
import Vue from "vue";
import { formatDate } from "@/services/date";

const CampsType = {
  short: "Stage Court",
  long: "Stage Long",
};

export default Vue.extend({
  name: "EventCardAdmin",
  props: [
    "title",
    "index",
    "camps_type",
    "id",
    "start_date",
    "end_date"
  ],
  data () {
    return {
      path:
        "/candidatures/" + new Date(this.start_date).getFullYear() + '/' + this.id,
      CampsType,
    };
  },
  computed: {
    colorClass: function () {
      const colors = ["gcc-pink", "gcc-green", "gcc-blue"];
      return colors[this.index % colors.length]
    },
    date: function () {
      return (
        'Du ' + formatDate(this.start_date) + ' au ' + formatDate(this.end_date)
      )
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