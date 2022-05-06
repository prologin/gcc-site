// Ensure CORS response header values are valid while dev
//
// https://gist.github.com/brenopolanski/7f084f2ab8f817f6160deae1be629520
// https://cli.vuejs.org/config/#devserver-proxy
// https://stackoverflow.com/questions/40315451/proxy-requests-to-a-separate-backend-server-with-vue-cli?answertab=active#tab-top

module.exports = {
  devServer: {
    proxy: {
      "/api": {
        target: process.env.BACKEND_URL == undefined ? 'http://localhost:8000' : process.env.BACKEND_URL,
        changeOrigin: true,
        secure: false
      }
    },
    watchOptions: {
      poll: true,
    },
  }
}
