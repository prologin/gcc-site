<template>
  <b-card no-body border-variant="light" header-border-variant="light">
    <b-card-header header-tag="header" role="tab">
      <b-row v-b-toggle="'accordion-' + index" class="secondary-button pr-4">
        <b-row class="pl-3">
          <b-icon
            :class="colorClass"
            class="mr-1 mr-sm-2 my-auto"
            icon="circle-fill"
            aria-hidden="true"
          />
          <p class="my-auto">
            {{ title }}
          </p>
        </b-row>
        <span class="when-closed ml-auto">
          <b-icon icon="chevron-compact-down" />
        </span>
        <span class="when-open ml-auto">
          <b-icon icon="chevron-compact-up" />
        </span>
      </b-row>
    </b-card-header>
    <b-collapse
      :id="'accordion-' + index"
      role="tabpanel"
      accordion="my-accordion"
    >
      <b-card-body>
        <ClientOnly>
          <b-card-text v-html="content" />
        </ClientOnly>
      </b-card-body>
    </b-collapse>
  </b-card>
</template>

<script>
import Vue from 'vue';

export default Vue.extend({
  name: 'Accordion',
  props: ['index', 'title', 'content'],
  computed: {
    colorClass: function () {
      const colors = ["gcc-pink", "gcc-green", "gcc-blue"];
      return colors[this.index % colors.length]
    },
  },
})
</script>

<style scoped>
.card,
.card-header {
  background-color: white !important;
  border-radius: var(--global-border-radius) !important;
  border: none;
}

.collapsed > .when-open,
.not-collapsed > .when-closed {
  display: none;
}
</style>
