<template>
  <div class="main-body-style">
    <b-container fluid class="p-0">
      <!-- Header -->
      <Header />

      <!-- Home illustration -->
      <client-only>
        <b-container fluid class="home-banner">
          <b-row class="h-100" align-v="center" align-h="center">
            <b-col
              class="text-center text-md-left col-md-5 col-lg-4 content-background home-title"
            >
              <span>
                <h1>
                  Stage d'initiation à l'informatique pour collégiennes et
                  lycéennes.
                </h1>
              </span>
              <span>
                <b-button
                  class="primary-button subtitleSize mt-4"
                  block
                  @click="scrollTo('event-list')"
                >
                  Voir les stages
                </b-button>
              </span>
              <span>
                <b-button
                  class="secondary-button subtitleSize"
                  block
                  @click="scrollTo('faq')"
                >
                  Plus d'informations
                </b-button>
              </span>
            </b-col>
          </b-row>
        </b-container>
      </client-only>

      <!-- Featured partners -->
      <!-- TODO change style -->
      <!--<Partners :is-front-page="true" :is-featured-space="true" />-->

      <!-- Event list -->
      <EventList id="event-list" />

      <!-- FAQ -->
      <FAQ id="faq" />

      <!-- Partners -->
      <!--<Partners :is-front-page="true" :is-featured-space="false" />-->

      <!-- Newsletter -->
      <b-container fluid class="newsletter-background text-center">
        <b-row align-h="center">
          <b-col md="8" class="mt-5">
            <h1>S'inscrire à la newsletter</h1>
            <h3>Pour être tenu au courant de nos prochains évènements.</h3>
            <Newsletter />
          </b-col>
        </b-row>
      </b-container>

      <!-- Footer -->
      <Footer />
    </b-container>
  </div>
</template>

<script>
import Vue from "vue";
import Header from "../components/Header.vue";
import EventList from "../components/EventList.vue";
import Partners from "../components/Partners.vue";
import FAQ from "../components/FAQ.vue";
import Newsletter from "../components/Newsletter.vue";
import Footer from "../components/Footer.vue";

export default Vue.extend({
  name: "Home",
  components: {
    Header,
    EventList,
    Partners,
    FAQ,
    Newsletter,
    Footer,
  }
});
</script>

<style>
.home-banner {
  height: 70vh;
  background-image: url("../assets/girl-class-v2.svg"),
    url("../assets/code-background-v2.svg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}

/* title animation */
.home-title span {
  position: relative;
  overflow: hidden;
  display: block;
  border-radius: var(--global-border-radius);
}

.home-title span::after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
  background: var(--main-dark-color);
  animation: a-ltr-after 0.7s cubic-bezier(0.5, 0.5, 0.5, 0.5) forwards;
  transform: translateX(-101%);
}

.home-title span::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
  background: white;
  animation: a-ltr-before 1s cubic-bezier(0.5, 0.5, 0.5, 0.5) forwards;
  transform: translateX(0);
}

.home-title span:nth-of-type(1)::before,
.home-title span:nth-of-type(1)::after {
  animation-delay: 0.5s;
}

.home-title span:nth-of-type(2)::before,
.home-title span:nth-of-type(2)::after {
  animation-delay: 0.7s;
}

.home-title span:nth-of-type(3)::before,
.home-title span:nth-of-type(3)::after {
  animation-delay: 1s;
}

@keyframes a-ltr-after {
  0% {
    transform: translateX(-100%);
  }

  100% {
    transform: translateX(101%);
  }
}

@keyframes a-ltr-before {
  0% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(200%);
  }
}

.newsletter-background {
  background-color: #efefef;
  background-image: url("../assets/newsletter_bg.svg");
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
