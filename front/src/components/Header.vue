<template>
  <b-navbar toggleable="md" class="navbar fixed-top" :class="{ 'navbar-hidden': !showNavbar }">
    <b-navbar-brand :to="{ name: 'home' }">
      <img class="menu-logo ml-0 ml-sm-5 pl-3" :src="require('@/assets/logo_gcc_text_right.svg')" alt="Logo des stages Girls Can Code" />
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav v-if="isAuthenticated" class="ml-auto">
        <b-nav-item>
          <b-dropdown no-caret toggle-class='secondary-button' variant='none'>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <b-row>
                <b-col>
                  <b-icon-person-circle aria-hidden="true" class="mr-2"/>
                    {{ getFirstName }} {{ getLastName }}
                </b-col>
                <b-col>
                  <b-icon icon='chevron-compact-down' />
                </b-col>
              </b-row>
            </template>

            <b-dropdown-header id="dropdown-header-label">
              <h2>{{ getFirstName }} {{ getLastName }}</h2>
              <h3>{{ getEmail }}</h3>
            </b-dropdown-header>
            <b-dropdown-divider/>
              <b-dropdown-item-button href="#">
                <b-icon icon="person-fill" aria-hidden="true"/>
                  Mon compte
              </b-dropdown-item-button>
              <b-dropdown-item :to="{ name: 'applications' }">
                <b-icon icon="inbox-fill"/>
                  Mes candidatures
              </b-dropdown-item>
              <b-dropdown-divider/>
                <b-dropdown-item-button @click="logout">
                  <b-icon icon="power" aria-hidden="true"/>
                    Se déconnecter
                </b-dropdown-item-button>
              </b-dropdown>
        </b-nav-item>
        <b-nav-item>
          <hr class="my-1">
        </b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav v-else class="ml-auto">
        <b-nav-item>
          <b-button :to="{ name: 'login-register' }" class="primary-button px-4">Connexion</b-button>
        </b-nav-item>
        <b-nav-item>
          <hr class="my-1">
        </b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapActions, mapGetters } from 'vuex'

export default Vue.extend({
  name: 'Header',
  data () {
    return {
      showNavbar: true,
      lastScrollPosition: 0
    }
  },
  mounted () {
    window.addEventListener('scroll', this.onScroll)
  },
  beforeDestroy () {
    window.removeEventListener('scroll', this.onScroll)
  },
  methods: {
    currentLocation: function () {
      if (window.location !== undefined) {
        return window.location.href
      }
      return 'filler'
    },
    onScroll () {
      // Based on https://medium.com/@Taha_Shashtari/hide-navbar-on-scroll-down-in-vue-fb85acbdddfe

      // Get the current scroll position
      const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop
      // Because of momentum scrolling on mobiles, we shouldn't continue if it is less than zero
      if (currentScrollPosition < 0) {
        return
      }

      // Stop executing this function if the difference between
      // current scroll position and last scroll position is less than some offset
      if (Math.abs(currentScrollPosition - this.lastScrollPosition) < 60) {
        return
      }

      // Here we determine whether we need to show or hide the navbar
      this.showNavbar = currentScrollPosition < this.lastScrollPosition
      // Set the current scroll position as the last scroll position
      this.lastScrollPosition = currentScrollPosition
    },
    async logout () {
      await this.$store.dispatch('LogOut').then(() => {
        this.$router.push({ name: 'home' })
      })
    }
  },
  computed: {
    ...mapGetters([
      'isAuthenticated',
      'getFirstName',
      'getLastName',
      'getEmail'
    ])
  }
})
</script>

<style>
.menu-logo {
  width: 6em;
}

.navbar {
  background-color: white;
  transition: top 0.5s ease;
}

.navbar.navbar-hidden {
  top: -100px;
}
</style>
