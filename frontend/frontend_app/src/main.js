import { createApp } from 'vue'
import App from './App.vue'
import router from './router' 
// no need for './router/index.js' everytime there is an index.js it picks it up 
import './assets/global.css'

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

createApp(App).use(router).mount('#app')
