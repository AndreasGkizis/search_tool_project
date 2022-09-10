import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from "../views/About.vue"
import Search from "../views/Search/Search.vue"
import SearchDetail from "../views/Search/SearchDetail.vue"
import Post from "../views/Post.vue"
import PageNotFound from "../views/PageNotFound.vue"


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
    component: Search,
  },
  {
    path: '/post',
    name: 'Post',
    component: Post
  },  
  {
    path: '/search/detail/:id?/',
    name: 'SearchDetail',
    component: SearchDetail,
    props:  true 
    // This will allow to grap parameters into the props pas of each component 
  },
  {
    path: '/:catchAll(.*)',
    name: 'PageNotFound',
    component: PageNotFound
    // '/:catchAll(.*)' special Vue thing which catches any page that is not in the above 
  }
]
// allows for forward and back actions in browser history
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

