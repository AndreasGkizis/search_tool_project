<template>
<div>
  <div id="nav">
    <router-link :to= "{ name: 'Home' }">Home</router-link> 
    <router-link :to= "{ name: 'About' }">About</router-link> 
    <router-link :to= "{ name: 'Search'}">Search</router-link> 
    <router-link :to= "{ name: 'Post'}"> Post </router-link>
  </div>
  <router-view/>
  <!-- all components (pages..) are injected into the router-view component . all else stays the same FOR EVERY PAGE  -->
</div>
</template>

<style>
#app {
  font-family: Avenir;
}

#nav {
  padding: 10px;
  background: #666;
}

#nav a {
  font-weight: bold;
  color: lightgray;
  text-decoration: none;
  width: 100%;
  padding: 10px;
  border-radius: 4px;
  margin: 10px;
}

#nav a.router-link-exact-active {
  color: #ffffff;
  background: #369;
  border-radius: 20;
}
</style>
