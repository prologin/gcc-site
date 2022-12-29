export default {
  server: {
    host: "0.0.0.0",
    port: 3000,
  },

  /*
   ** Headers of the page
   ** Doc: https://vue-meta.nuxtjs.org/api/#metainfo-properties
   */
  head: {
    title: "Girls Can Code!",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "description",
        name: "description",
        content: "description",
      },
    ],
  },

  build: {
    transpile: ['defu'],
  },
  buildModules: ["@nuxt/typescript-build"],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  /*
   ** Nuxt.js modules
   ** Doc: https://modules.nuxtjs.org
   */
  modules: ["bootstrap-vue/nuxt", "@nuxtjs/axios", "@nuxtjs/auth-next"],

  bootstrapVue: {
    icons: true,
  },

  router: {
    extendRoutes(routes, resolve) {
      routes.push({
        name: "PageNotFound",
        path: "*",
        component: resolve(__dirname, "pages/404.vue"),
      });
    }
  },

  auth: {
    strategies: {
      prologin: {
        provider: "~/schemes/prologin",
        clientId:
          "tVOgJ4hxT8uV0bjMIjT4psPARaR1XgxhIYoXcqnGIFZVmCpMTrhDKEK2qy6TT9VO",
        clientSecret:
          "t9pvgKnwB37CeutWpPOEKMDv3gmp9kjUtQ5ifDzF9gBPMGO4yhHLdUNnh7AjRuWH",
        endpoints: {
          configuration:
            "https://auth.prologin.org/application/o/prologin-public-test-client/.well-known/openid-configuration",
        },
      }
    },
    redirect: {
      login: "/LoginRegisterView",
      callback: "/callback",
      home: "/",
    }
  },

  axios: {
    baseURL:
      process.env.BACKEND_URL == undefined
        ? 'http://backend_dev:8000'
        : process.env.BACKEND_URL,
    browserBaseURL:
      process.env.BROWSER_BACKEND_URL == undefined
        ? 'http://localhost:8000'
        : process.env.BROWSER_BACKEND_URL,
    proxy: true,
    proxyHeaders: true,
  },

  /*
   ** Global CSS
   ** Doc: https://nuxtjs.org/docs/2.x/configuration-glossary/configuration-css
   */
  css: [
    "./assets/css/main.css",
    "@fortawesome/fontawesome-svg-core/styles.css",
  ],

  /*
   ** Plugins to load before mounting the App
   ** Doc: https://nuxtjs.org/docs/2.x/directory-structure/plugins
   */
  plugins: ["~/plugins/scrollto.ts", "~/plugins/fontawesome.js"],
};
