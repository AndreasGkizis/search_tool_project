<template>
  <div class="row cols-2 mx-auto">
    <div class="filters col-3">
      <h2>Filters</h2>

      <div class="title">
        <div class="mb-3 dark">
          <label for="exampleInputEmail1" class="form-label"
            ><h4>Title</h4></label
          >
          <input
            type="text"
            class="form-control"
            id="title"
            placeholder="Enter here to search by title "
            v-model="filters_selected.title"
          />
        </div>
      </div>

      <!-- <label for="title">Title:</label>
        <input id="title" type="text" v-model="filters_selected.title" />
      </div> -->

      <div class="tags">
        <h4>Tags</h4>
        <button
          class="btn pt-0"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#collapsetags"
          aria-expanded="false"
          aria-controls="collapsetags"
        >
          Show tags
        </button>

        <div class="collapse" id="collapsetags">
          <input
            type="text"
            class="form-control"
            v-model="tagQuery"
            placeholder="filter tags "
          />
          <br />
          <div v-for="i in computedTags" :key="i.id">
            <div class="form-check form-switch">
              <input
                class="form-check-input"
                type="checkbox"
                role="switch"
                :id="i.tag"
                :value="i.id"
                v-model="filters_selected.tag"
              />
              <label class="form-check-label" :for="i.tag"> {{ i.tag }}</label>
            </div>
          </div>
          <br />

          <!-- <div v-for="i in initial_filter_data.tag" :key="i.id">
            <div class="form-check form-switch">
              <input
                class="form-check-input"
                type="checkbox"
                role="switch"
                :id="i.tag"
                :value="i.id"
                v-model="filters_selected.tag"
              />
              <label class="form-check-label" :for="i.tag"> {{ i.tag }}</label>
            </div>
          </div> -->
        </div>
      </div>

      <div class="type">
        <h3>Types</h3>
        <div v-for="i in initial_filter_data.type" :key="i.id">
          <div class="form-check form-switch">
            <input
              class="form-check-input"
              type="checkbox"
              role="switch"
              :id="i.type"
              :value="i.id"
              v-model="filters_selected.type"
            />
            <label class="form-check-label" :for="i.type">
              {{ i.type }}
            </label>
          </div>
        </div>
      </div>

      <div class="year">
        <h3>Years</h3>
        <div v-for="i in initial_filter_data.year" :key="i.id">
          <div class="form-check form-switch">
            <input
              class="form-check-input"
              type="checkbox"
              role="switch"
              :id="i.year_published"
              :value="i.id"
              v-model="filters_selected.year"
            />
            <label class="form-check-label" :for="i.year_published">
              {{ i.year_published }}</label
            >
          </div>
          <!-- 
          <input
            type="checkbox"
            :id="i.year_published"
            :value="i.id"
            v-model="filters_selected.year"
          />
          <label :for="i.year_published"> {{ i.year_published }}</label> -->
        </div>
      </div>

      <div class="author">
        <h3>Author</h3>
        <div v-for="i in initial_filter_data.author" :key="i.id">
          <div class="form-check form-switch">
            <input
              class="form-check-input"
              type="checkbox"
              role="switch"
              :id="i.name"
              :value="i.id"
              v-model="filters_selected.author"
            />
            <label class="form-check-label" :for="i.name"> {{ i.name }}</label>
          </div>
        </div>
      </div>

      <div class="material">
        <h3>Material</h3>
        <div v-for="i in initial_filter_data.material" :key="i.id">
          <div class="form-check form-switch">
            <input
              class="form-check-input"
              type="checkbox"
              role="switch"
              :id="i.material"
              :value="i.id"
              v-model="filters_selected.material"
            />
            <label class="form-check-label" :for="i.material">
              {{ i.material }}</label
            >
          </div>
        </div>
      </div>
      <!-- last div closes Filters -->
    </div>

    <div class="results col">
      <div v-for="i in results_data" :key="i.id">
        <div class="card">
          <div class="card-header">
            <h4>{{ i.title }}</h4>
            <h4 class="display-6">{{ i.title }}</h4>
            <!-- change all to disply, they do look nicer -->
          </div>
          <div class="card-body row">
            <dl class="row">
              <dt class="col">Tags:</dt>
              <dd class="col-sm-11">
                <div
                  class="list-inline-item"
                  v-for="p in i.tag.length"
                  :key="p.id"
                  id="tags"
                >
                  {{ i.tag[p - 1] }}
                </div>
              </dd>

              <dt class="col">Type:</dt>
              <dd class="col-11">
                <div class="list-inline-item" id="type_id">
                  {{ i.type_id }}
                </div>
              </dd>

              <dt class="col">Year:</dt>
              <dd class="col-sm-11">
                <div id="year">
                  {{ i.year_id }}
                </div>
              </dd>

              <dt class="col">Materials:</dt>
              <dd class="col-sm-11">
                <div
                  class="list-inline-item"
                  v-for="p in i.material.length"
                  :key="p.id"
                  id="material"
                >
                  {{ i.material[p - 1] }}
                </div>
              </dd>

              <dt class="col">Author:</dt>
              <dd class="col-sm-11">
                <div
                  id="author"
                  class="list-inline-item"
                  v-for="p in i.author.length"
                  :key="p.id"
                >
                  {{ i.author[p - 1].name }}
                </div>
              </dd>
            </dl>
            <details>
              <summary>Abstract</summary>
                {{i.abstract}}
            </details>
          </div>
          <br />
        </div>
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
      tagQuery: [],
      computedtags: [],
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
        this.computedtags = response.data;
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
          path: "/search/",
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
          .get("/paper/", {
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
            console.log(this.$router.params);
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
  computed: {
    computedTags(tagQuery) {
      return this.initial_filter_data.tag.filter((x) =>
        x.tag.toLowerCase().includes(this.tagQuery)
      );
    },
  },
};
</script>

<style>
.filters {
  padding: 5px;
}

.results {
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
