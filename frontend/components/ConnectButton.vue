<template>
    <b-button block class="login-button">
        <b-row align-v="center">
            <b-col cols="2">
              <font-awesome-icon :icon=logo class="icon alt" size="2x"/>
            </b-col>
            <b-col cols="10">
                {{ name }}
            </b-col>
        </b-row>
    </b-button>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: 'ConnectButton',
  props: ['logo','name'],
})

</script>

<style scoped>
.login-button {
  border-radius: var(--global-border-radius) !important;
}

.login-button {
  background:
    linear-gradient(white, white) padding-box,
    linear-gradient(to right, #00AED3, #E4006D, #A6C613) border-box;
  border: 2px solid transparent !important;
  color: var(--main-dark-color) !important;
}

.login-button:hover {
  background: var(--light-text-color) !important;
  color: white !important;
}
</style>
