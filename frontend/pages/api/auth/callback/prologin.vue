<template>
  <div fluid class="callback-background">
    <div class="spin">
      <h1>Connexion en cours</h1>
    </div>
    <div class="dot-spin" />
  </div>
</template>

<script>
import Vue from 'vue';

export default Vue.extend({
  middleware: ["auth"],
})
</script>

<style scoped>
.callback-background {
  height: 100vh;
  background-image: url("@/assets/basic_background_v2.svg");
}

.dot-spin {
  position: absolute;
  margin: auto;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;

  width: 10px;
  height: 10px;
  border-radius: 10px;
  background-color: white;
  color: black;
  box-shadow: 0 -24px 0 0 rgba(0, 174, 211, 1),
    17px -17px 0 0 rgba(0, 174, 211, 1), 24px 0 0 0 rgba(0, 174, 211, 1),
    17px 17px 0 0 rgba(0, 174, 211, 0), 0 24px 0 0 rgba(0, 174, 211, 0),
    -17px 17px 0 0 rgba(0, 174, 211, 0), -24px 0 0 0 rgba(0, 174, 211, 0),
    -17px -17px 0 0 rgba(0, 174, 211, 0);
  animation: dot-spin 1.5s infinite linear;
}

@keyframes dot-spin {
  0%,
  100% {
    box-shadow: 0 -24px 0 0 rgba(0, 174, 211, 1),
      17px -17px 0 0 rgba(0, 174, 211, 1), 24px 0 0 0 rgba(0, 174, 211, 1),
      17px 17px 0 -5px rgba(0, 174, 211, 0), 0 24px 0 -5px rgba(0, 174, 211, 0),
      -17px 17px 0 -5px rgba(0, 174, 211, 0),
      -24px 0 0 -5px rgba(0, 174, 211, 0),
      -17px -17px 0 -5px rgba(0, 174, 211, 0);
  }

  12.5% {
    box-shadow: 0 -24px 0 -5px rgba(0, 174, 211, 0),
      17px -17px 0 0 rgba(0, 174, 211, 1), 24px 0 0 0 rgba(0, 174, 211, 1),
      17px 17px 0 0 rgba(0, 174, 211, 1), 0 24px 0 -5px rgba(0, 174, 211, 0),
      -17px 17px 0 -5px rgba(0, 174, 211, 0),
      -24px 0 0 -5px rgba(0, 174, 211, 0),
      -17px -17px 0 -5px rgba(0, 174, 211, 0);
  }

  25% {
    box-shadow: 0 -24px 0 -5px rgba(0, 174, 211, 0),
      17px -17px 0 -5px rgba(0, 174, 211, 0), 24px 0 0 0 rgba(0, 174, 211, 1),
      17px 17px 0 0 rgba(0, 174, 211, 1), 0 24px 0 0 rgba(0, 174, 211, 1),
      -17px 17px 0 -5px rgba(0, 174, 211, 0),
      -24px 0 0 -5px rgba(0, 174, 211, 0),
      -17px -17px 0 -5px rgba(0, 174, 211, 0);
  }

  37.5% {
    box-shadow: 0 -24px 0 -5px rgba(0, 174, 211, 0),
      17px -17px 0 -5px rgba(0, 174, 211, 0), 24px 0 0 -5px rgba(0, 174, 211, 0),
      17px 17px 0 0 rgba(0, 174, 211, 1), 0 24px 0 0 rgba(0, 174, 211, 1),
      -17px 17px 0 0 rgba(0, 174, 211, 1), -24px 0 0 -5px rgba(0, 174, 211, 0),
      -17px -17px 0 -5px rgba(0, 174, 211, 0);
  }

  50% {
    box-shadow: 0 -24px 0 -5px rgba(0, 174, 211, 0),
      17px -17px 0 -5px rgba(0, 174, 211, 0), 24px 0 0 -5px rgba(0, 174, 211, 0),
      17px 17px 0 -5px rgba(0, 174, 211, 0), 0 24px 0 0 rgba(0, 174, 211, 1),
      -17px 17px 0 0 rgba(0, 174, 211, 1), -24px 0 0 0 rgba(0, 174, 211, 1),
      -17px -17px 0 -5px rgba(0, 174, 211, 0);
  }

  62.5% {
    box-shadow: 0 -24px 0 -5px rgba(0, 174, 211, 0),
      17px -17px 0 -5px rgba(0, 174, 211, 0), 24px 0 0 -5px rgba(0, 174, 211, 0),
      17px 17px 0 -5px rgba(0, 174, 211, 0), 0 24px 0 -5px rgba(0, 174, 211, 0),
      -17px 17px 0 0 rgba(0, 174, 211, 1), -24px 0 0 0 rgba(0, 174, 211, 1),
      -17px -17px 0 0 rgba(0, 174, 211, 1);
  }

  75% {
    box-shadow: 0 -24px 0 0 rgba(00AED3, 1),
      17px -17px 0 -5px rgba(0, 174, 211, 0), 24px 0 0 -5px rgba(0, 174, 211, 0),
      17px 17px 0 -5px rgba(0, 174, 211, 0), 0 24px 0 -5px rgba(0, 174, 211, 0),
      -17px 17px 0 -5px rgba(0, 174, 211, 0), -24px 0 0 0 rgba(0, 174, 211, 1),
      -17px -17px 0 0 rgba(0, 174, 211, 1);
  }

  87.5% {
    box-shadow: 0 -24px 0 0 rgba(0, 174, 211, 1),
      17px -17px 0 0 rgba(0, 174, 211, 1), 24px 0 0 -5px rgba(0, 174, 211, 0),
      17px 17px 0 -5px rgba(0, 174, 211, 0), 0 24px 0 -5px rgba(0, 174, 211, 0),
      -17px 17px 0 -5px rgba(0, 174, 211, 0),
      -24px 0 0 -5px rgba(0, 174, 211, 0), -17px -17px 0 0 rgba(0, 174, 211, 1);
  }
}

.spin {
  display: flex;
  justify-content: center;
  align-items: center;
}
.spin h1 {
  margin: 0;
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -90%);
}
</style>
