export default {

    server: {
        port: 8080,
        host: '0.0.0.0'
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
                content: "description"
            }
        ],

    },
    buildModules: [
        '@nuxt/typescript-build',
    ],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    /*
     ** Nuxt.js modules
     ** Doc: https://modules.nuxtjs.org
     */
    modules: [
        'bootstrap-vue/nuxt',
        '@nuxtjs/axios'
    ],

    bootstrapVue: {
        icons: true,
    },


    router: {
        extendRoutes(routes, resolve) {
        routes.push({
            name: 'PageNotFound',
            path: '*',
            component: resolve(__dirname, 'pages/404.vue')
        })
        }
    },

    axios: {
        proxy: true,
    },

    proxy: {
        '/api/': {
            target : process.env.BACKEND_URL == undefined ? 'http://localhost:8000' : process.env.BACKEND_URL
        }
    },

    /*
     ** Global CSS
     ** Doc: https://nuxtjs.org/docs/2.x/configuration-glossary/configuration-css
     */
    css: [
        './assets/css/main.css',
        '@fortawesome/fontawesome-svg-core/styles.css',
    ],

    /*
     ** Plugins to load before mounting the App
     ** Doc: https://nuxtjs.org/docs/2.x/directory-structure/plugins
     */
    plugins: [
        '~/plugins/scrollto.ts',
        '~/plugins/fontawesome.js',
    ]
};
