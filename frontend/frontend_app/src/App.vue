<template>
  <div>
    <div id="nav">
      <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
          <a class="navbar-brand"> Search Tool Project </a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
           <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <router-link :to="{ name: 'Home' }" class="nav-link"
                  >Home</router-link
                >
              </li>

              <li class="nav-item">
                <router-link :to="{ name: 'Post' }" class="nav-link"
                  >Post</router-link
                >
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'Search' }" class="nav-link"
                  >Search</router-link
                >
              </li>
              <li class="nav-item align-right">
                <router-link :to="{ name: 'About' }" class="nav-link"
                  >About</router-link
                >
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
    <router-view />
    <!-- all components (pages..) are injected into the router-view component . all else stays the same FOR EVERY PAGE  -->
  </div>
</template>

<style>
#app {
  /* font-family: Avenir; */
}

#nav {
  background: #666;
}

#nav a.router-link-exact-active {
  color: #ffffff;
  background: #369;
  padding-inline: 30px;
  border-radius: 4px;
}

#nav a.nav-link {
  padding-inline: 30px;
}
</style>
