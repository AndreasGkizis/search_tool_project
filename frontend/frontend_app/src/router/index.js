import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from "../views/About.vue"
import Search from "../views/Search/Search.vue"
import SearchDetail from "../views/Search/SearchDetail"
import Post from "../views/Post.vue"


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/search/detail',
    name: 'SearchDetail',
    component: SearchDetail
  },  
  {
    path: '/post',
    name: 'Post',
    component: Post
  },  
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
