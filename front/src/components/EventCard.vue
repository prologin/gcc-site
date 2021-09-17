<template>
    <b-row class="event-card mb-4 p-3">
        <b-col class="my-auto d-none d-sm-block" md="auto">
            <b-icon :class="colorClass" icon="circle-fill" aria-hidden="true"/>
        </b-col>
        <!-- Event infos verticaly centered -->
        <b-col class="col-sm-auto">
            <h1>{{ title }}</h1>
            <h2>{{ date }}</h2>
            <h3>{{ address }}</h3>
        </b-col>
        <b-button-group vertical class="col-sm-auto ml-auto mt-4 mb-1 my-sm-auto" cols="auto">
            <b-button class="mx-auto ml-sm-auto mr-sm-5 primary-button">S'inscrire à ce stage</b-button>
            <b-button class="mx-auto ml-sm-auto mr-sm-5 secondary-button">Plus d'informations</b-button>
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
