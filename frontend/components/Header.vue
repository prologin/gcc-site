<template>
  <b-navbar
    toggleable="md"
    class="navbar fixed-top"
    :class="{ 'navbar-hidden': !showNavbar }"
  >
    <NuxtLink to="/">
      <img
        class="menu-logo ml-0 ml-sm-5 pl-3"
        :src="require('../assets/logo_gcc_text_right.svg')"
        alt="Logo des stages Girls Can Code"
      >
    </NuxtLink>
    <b-navbar-toggle target="nav-collapse" />
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav v-if="loggedIn" class="ml-auto">
        <b-nav-item v-if="this.user.is_staff && this.user['user_permissions'].includes(89)">
          <b-dropdown
            right
            no-caret
            toggle-class="secondary-button"
            variant="none"
          >
            <template #button-content>
              <b-row>
                <b-col>
                  <font-awesome-icon
                    icon="fa-solid fa-star"
                    style="color: black"
                  />
                </b-col>
                <b-col> Admin </b-col>
              </b-row>
            </template>

            <b-dropdown-header id="dropdown-header-label">
              Panel Admin
            </b-dropdown-header>
            <b-dropdown-divider />
            <b-dropdown-item>
              <NuxtLink style="color: black" to="/admin">
                Administration Django
              </NuxtLink>
            </b-dropdown-item>
            <b-dropdown-item>
              <NuxtLink style="color: black" to="/stages">
                Liste des stages
              </NuxtLink>
            </b-dropdown-item>
          </b-dropdown>
        </b-nav-item>

        <b-nav-item v-if="loggedIn">
          <b-dropdown
            right
            no-caret
            toggle-class="secondary-button"
            variant="none"
          >
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <b-row>
                <b-col>
                  <b-icon-person-circle aria-hidden="true" class="mr-2" />
                  {{ user.first_name }} {{ user.last_name }}
                </b-col>
                <b-col>
                  <b-icon icon="chevron-compact-down" />
                </b-col>
              </b-row>
            </template>

            <b-dropdown-header id="dropdown-header-label">
              <h2>{{ user.first_name }} {{ user.lastname }}</h2>
              <h3>{{ user.email }}</h3>
            </b-dropdown-header>
            <b-dropdown-divider />
            <b-dropdown-item>
              <font-awesome-icon icon="fa-solid fa-user" />
              <NuxtLink style="color: black" to="/AccountInformationsView">
                Mon compte
              </NuxtLink>
            </b-dropdown-item>
            <b-dropdown-item>
              <font-awesome-icon icon="fa-solid fa-inbox" />
              <NuxtLink style="color: black" to="/ApplicationsView">
                Mes candidatures
              </NuxtLink>
            </b-dropdown-item>
            <b-dropdown-divider />
            <b-dropdown-item-button @click="logout()">
              <b-icon icon="power" aria-hidden="true" />
              Se déconnecter
            </b-dropdown-item-button>
          </b-dropdown>
        </b-nav-item>
        <b-nav-item>
          <hr class="my-1" >
        </b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav v-else class="ml-auto">
        <b-nav-item>
          <ClientOnly>
            <NuxtLink
              to="/LoginRegisterView"
              class="primary-button py-2 px-4"
              style="color: white"
            >
              Connexion
            </NuxtLink>
          </ClientOnly>
        </b-nav-item>
        <b-nav-item>
          <hr class="my-1" >
        </b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script lang="ts">
import Vue from "vue";
import { usersAPI } from "@/services/users.api";

export default Vue.extend({
  name: "Header",
  data() {
    return {
      user: "",
      loggedIn: this.$auth.loggedIn,
      showNavbar: true,
      lastScrollPosition: 0,
    };
  },
  created() {
    //Trouver le moyen de remettre /users/me/ because pipline failed
    this.$axios.get("rest/auth/user").then((response) => {
      this.user = response.data;
    })
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.onScroll);
  },
  methods: {
    currentLocation: function () {
      if (window.location !== undefined) {
        return window.location.href;
      }
      return "filler";
    },
    onScroll() {
      // Based on https://medium.com/@Taha_Shashtari/hide-navbar-on-scroll-down-in-vue-fb85acbdddfe

      // Get the current scroll position
      const currentScrollPosition =
        window.pageYOffset || document.documentElement.scrollTop;
      // Because of momentum scrolling on mobiles, we shouldn't continue if it is less than zero
      if (currentScrollPosition < 0) {
        return;
      }

      // Stop executing this function if the difference between
      // current scroll position and last scroll position is less than some offset
      if (Math.abs(currentScrollPosition - this.lastScrollPosition) < 60) {
        return;
      }

      // Here we determine whether we need to show or hide the navbar
      this.showNavbar = currentScrollPosition < this.lastScrollPosition;
      // Set the current scroll position as the last scroll position
      this.lastScrollPosition = currentScrollPosition;
    },
    async logout() {
      // this as any: bypasses typescript checks
      await this.$auth.logout().then(() => {
        (this as any).$router.push("/");
      });
    },
  },
});
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

button.dropdown-item {
  z-index: 10;
}
</style>
