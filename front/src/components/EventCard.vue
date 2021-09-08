<template>
    <b-row class="event-card mb-4 p-3">
        <b-col class="my-auto" md="auto">
            <b-icon v-bind:class="colorClass" icon="circle-fill" aria-hidden="true"/>
        </b-col>
        <!-- Event infos verticaly centered -->
        <b-col cols="auto" class="my-auto">
            <h1>{{ title }}</h1>
            <h2>{{ date }}</h2>
            <h3>{{ address }}</h3>
        </b-col>
        <b-button-group vertical class="my-auto ml-auto m-5" cols="auto">
            <b-button class="mx-4 primary-button">S'inscrire à ce stage</b-button>
            <b-button class="mx-4 secondary-button">Plus d'informations</b-button>
        </b-button-group>
    </b-row>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'EventCard',
  props: ['title', 'date', 'address', 'index'],
  computed: {
    colorClass: function () {
      var colors = ['gcc-pink', 'gcc-green', 'gcc-blue']
      return colors[this.index % colors.length]
    }
  }
})
</script>

<style>
.event-card {
    background-color: #FFFFFF;
    border-radius: 12px;
}

.btn-group-vertical > button{
    margin-bottom:5px;
    border-radius:12px !important;
}
</style>
