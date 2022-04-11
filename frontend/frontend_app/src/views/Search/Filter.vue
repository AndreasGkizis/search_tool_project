<template>
 <div class="container">
    <div class="filters">
      <h2>Filters</h2>
      <div>{{filtered_data}}</div>
      <div class="title">
          <input type="text" v-model="filtered_data.title">
      </div>
      <div class="tags">
        <h3>Tags</h3>
        <div v-for="i in initial_data.tag" :key="i.id">
          <input
            type="checkbox"
            :id="i.tag"
            :value="i.id"
            v-model="filtered_data.tag"
          />
          <label :for="i.tag"> {{ i.tag }}</label>
        </div>
      </div>

      <div class="type">
        <h3>Types</h3>
        <div v-for="i in initial_data.type" :key="i.id">
          <input
            type="checkbox"
            :id="i.type"
            :value="i.id"
            v-model="filtered_data.type"
          />
          <label :for="i.type"> {{ i.type }}</label>
        </div>
      </div>

      <div class="year">
        <h3>Years</h3>
        <div v-for="i in initial_data.year" :key="i.id">
          <input
            type="checkbox"
            :id="i.year_published"
            :value="i.id"
            v-model="filtered_data.year"
          />
          <label :for="i.year_published"> {{ i.year_published }}</label>
        </div>
      </div>

      <div class="author">
        <h3>Author</h3>
        <div v-for="i in initial_data.author" :key="i.id">
          <input
            type="checkbox"
            :id="i.name"
            :value="i.id"
            v-model="filtered_data.author"
          />
          <label :for="i.name"> {{ i.name }}</label>
        </div>
      </div>
    </div>
    <div class="results">
        <Results
        :filter_data="filtered_data"
        />
    </div>
</div>
</template>

<script>
import Results from "./Results.vue"
import { getAPI } from "../..//axios-api";

export default {
    components: {
        Results,
    },
  data() {
    return {
      initial_data: {
        year: [],
        type: [],
        language: [],
        author: [],
        tag: [],
        material: [],
      },
      filtered_data: {
        title: "",
        year: [],
        type: [],
        language: [],
        author: [],
        tag: [],
        material: [],
      },
    };
  },
  mounted() {
    getAPI
      .get("/year/")
      .then((response) => {
        console.log("year api data recieved ");
        this.initial_data.year = response.data;
      })
      .catch((err) => {
        console.log(err);
      });

    getAPI
      .get("/type/")
      .then((response) => {
        console.log("type api data recieved ");
        this.initial_data.type = response.data;
      })
      .catch((err) => {
        console.log(err);
      });

    getAPI
      .get("/language/")
      .then((response) => {
        console.log("language api data recieved ");
        this.initial_data.language = response.data;
      })
      .catch((err) => {
        console.log(err);
      });

    getAPI
      .get("/author/")
      .then((response) => {
        console.log("author api data recieved ");
        this.initial_data.author = response.data;
      })
      .catch((err) => {
        console.log(err);
      });

    getAPI
      .get("/tag/")
      .then((response) => {
        console.log("Tag api data recieved ");
        this.initial_data.tag = response.data;
      })
      .catch((err) => {
        console.log(err);
      });

    getAPI
      .get("/material/")
      .then((response) => {
        console.log("material api data recieved ");
        this.initial_data.material = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    // updateNav() {
    //     this.$router.push({query: {title: this.title.toLowerCase() }})
    //     getAPI.get('/paper/' + '?'+ this.$route.href.split("?")[1])
    //     .then(response => {
    //     console.log('updateNav ' + this.$route.href.split("?")[1])
    //     this.APIpaperData = response.data
    // })
    // },
    // addToQuery() {
    //     this.$router.push({query: {title: this.textSearched.toLowerCase() }})
    // },
  },
};
</script>

<style>
.filters{
    width: 25%;
}

.results{
    width: 50%;
    padding-left: 30px;
}
</style>