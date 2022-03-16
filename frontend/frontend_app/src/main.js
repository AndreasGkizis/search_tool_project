import { createApp } from 'vue'
import App from './App.vue'
import router from './router' 
// no need for './router/index.js' everytime there is an index.js it picks it up 

createApp(App).use(router).mount('#app')
