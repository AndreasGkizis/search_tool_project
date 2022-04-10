<template>
<div>
  <div id="nav">
    <router-link :to= "{ name: 'Home' }">Home</router-link> |
    <router-link :to= "{ name: 'About' }">About</router-link> |
    <router-link :to= "{ name: 'Search'}">Search</router-link> |
    <router-link :to= "{ name: 'Post'}"> Post </router-link>
  </div>
  <router-view/>
  <!-- all components (pages..) are injected into the router-view component . all else stays the same FOR EVERY PAGE  -->
</div>
  
</template>

<style>
#app {
  font-family: Avenir
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  padding: 10px;
  border-radius: 4px;
}

#nav a.router-link-exact-active {
  color: #ffffff;
  background: #2c3e50;
}
</style>
