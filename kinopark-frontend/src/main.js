import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import Home from './components/Home.vue'

createApp(App).mount('#app')
App.components(Home)
