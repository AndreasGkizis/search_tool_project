<template>
  <div class="container">
    <div class="filters">
      <h2>Filters</h2>
      <div class="title">
        <label for="title">Title:</label>
        <input id="title" type="text" v-model="filters_selected.title" />
      </div>

      <div class="tags">
        <h3>Tags</h3>
        <div v-for="i in initial_filter_data.tag" :key="i.id">
          
            <ul>
                  <input
                type="checkbox"
                :id="i.tag"
                :value="i.id"
                v-model="filters_selected.tag"
              />
              <label :for="i.tag"> {{ i.tag }}</label>
            </ul>
          
          
        </div>
      </div>

      <div class="type">
        <h3>Types</h3>
        <div v-for="i in initial_filter_data.type" :key="i.id">
          <input
            type="checkbox"
            :id="i.type"
            :value="i.id"
            v-model="filters_selected.type"
          />
          <label :for="i.type"> {{ i.type }}</label>
        </div>
      </div>

      <div class="year">
        <h3>Years</h3>
        <div v-for="i in initial_filter_data.year" :key="i.id">
          <input
            type="checkbox"
            :id="i.year_published"
            :value="i.id"
            v-model="filters_selected.year"
          />
          <label :for="i.year_published"> {{ i.year_published }}</label>
        </div>
      </div>

      <div class="author">
        <h3>Author</h3>
        <div v-for="i in initial_filter_data.author" :key="i.id">
          <input
            type="checkbox"
            :id="i.name"
            :value="i.id"
            v-model="filters_selected.author"
          />
          <label :for="i.name"> {{ i.name }}</label>
        </div>
      </div>

      <div class="material">
        <h3>Material</h3>
        <div v-for="i in initial_filter_data.material" :key="i.id">
          <input
            type="checkbox"
            :id="i.material"
            :value="i.id"
            v-model="filters_selected.material"
          />
          <label :for="i.material">{{ i.material }}</label>
        </div>
      </div>
      <!-- last div closes Filters -->
    </div>

    <div class="results">
      <div v-for="i in results_data" :key="i.id">
        <div class="card">
          <div class="card-header">
            <h3>Title: {{ i.title }}</h3>
          </div>
          <div class="card-body">
            <p>Abstract: {{ i.abstract }}</p>
            Authors:
            <div v-for="p in i.author.length" :key="p.id" id="authors">
              <p>{{ i.author[p - 1].name }}</p>
            </div>
            Tags: 
            <div v-for="p in i.tag.length" :key="p.id" id="tags">
              <p>{{ i.tag[ p - 1] }}</p>
            </div>
          </div>
        </div>

        <p></p>
        <p></p>
        <p></p>
      </div>
    </div>
  </div>
</template>

<script>
import { getAPI } from "../..//axios-api";

export default {
  data() {
    return {
      initial_filter_data: {
        year: [],
        type: [],
        language: [],
        author: [],
        tag: [],
        material: [],
      },
      filters_selected: {
        title: "",
        year: [],
        type: [],
        language: [],
        author: [],
        tag: [],
        material: [],
      },
      results_data: [],
    };
  },
  mounted() {
    // FILTER FIELDS DATA
    getAPI
      .get("/year/")
      .then((response) => {
        console.log("year api data recieved ");
        this.initial_filter_data.year = response.data;
      })
      .catch((err) => {
        console.log(err);
      });

    getAPI
      .get("/type/")
      .then((response) => {
        console.log("type api data recieved ");
        this.initial_filter_data.type = response.data;
      })
      .catch((err) => {
        console.log(err);
      });

    getAPI
      .get("/language/")
      .then((response) => {
        console.log("language api data recieved ");
        this.initial_filter_data.language = response.data;
      })
      .catch((err) => {
        console.log(err);
      });

    getAPI
      .get("/author/")
      .then((response) => {
        console.log("author api data recieved ");
        this.initial_filter_data.author = response.data;
      })
      .catch((err) => {
        console.log(err);
      });

    getAPI
      .get("/tag/")
      .then((response) => {
        console.log("Tag api data recieved ");
        this.initial_filter_data.tag = response.data;
      })
      .catch((err) => {
        console.log(err);
      });

    getAPI
      .get("/material/")
      .then((response) => {
        console.log("material api data recieved ");
        this.initial_filter_data.material = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
    //  RESULTS INITIAL DATA
    getAPI
      .get("/paper/")
      .then((response) => {
        this.results_data = response.data;
        console.log("Paper api data recieved and logged , no error!");
      })
      .catch((err) => {
        console.log(err);
      });
  },
  watch: {
    filters_selected: {
      handler() {
        console.log("filters_selected watcher");
        this.$router.push({
          path: "/search",
          query: {
            title: this.filters_selected.title,
            year: this.filters_selected.year,
            type: this.filters_selected.type,
            language: this.filters_selected.language,
            author: this.filters_selected.author,
            tag: this.filters_selected.tag,
            material: this.filters_selected.material,
          },
        });

        getAPI
          .get("/paper", {
            params: {
              title: this.filters_selected.title,
              year: this.filters_selected.year,
              type: this.filters_selected.type,
              language: this.filters_selected.language,
              author: this.filters_selected.author,
              tag: this.filters_selected.tag,
              material: this.filters_selected.material,
            },
          })
          .then((response) => {
            console.log("getapi filteredPapers hit");
            console.log(response.data);
            this.results_data = response.data;
          })
          .catch((err) => {
            console.log(err);
          });
      },
      deep: true,
    },
  },
};
</script>

<style>
.filters {
  width: 25%;
  background-color: lightgray;
  padding: 5px;
}

.results {
  width: 50%;
  padding-left: 30px;
}

.card {
  background: lightgrey;
  border-radius: 10px;
  padding: 5px;
  width: 100%;
}

.ul {
  margin: 0%;

}
</style>