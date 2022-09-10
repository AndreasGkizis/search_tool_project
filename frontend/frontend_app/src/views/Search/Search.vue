<template>
  <div class="container-xxl">
    <div class="row mx-auto">
      <!-- All filters under this div -->
      <div class="filters col-3">
        <h2>Filters</h2>

        <div class="title">
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label"></label>
            <h4>Title</h4>
            <input type="text" class="form-control" id="title" placeholder="Enter here to search by title "
              v-model="filters_selected.title" />
          </div>
        </div>

        <div class="tags">
          <h4>Tags</h4>

          <input type="text" class="form-control" v-model="tagQuery" placeholder="filter tags " />
          <div v-for="i in computedTags" :key="i.id">
            <div class="form-check form-switch">
              <input class="form-check-input" type="checkbox" role="switch" :id="i.tag" :value="i.id"
                v-model="filters_selected.tag" />
              <label class="form-check-label" :for="i.tag">
                {{ i.tag }}</label>
            </div>
          </div>

        </div>

        <div class="type">
          <h3>Types</h3>
          <input type="text" class="form-control" v-model="typeQuery" placeholder="filter types" />
          <div v-for="i in computedTypes" :key="i.id">
            <div class="form-check form-switch">
              <input class="form-check-input" type="checkbox" role="switch" :id="i.type" :value="i.id"
                v-model="filters_selected.type" />
              <label class="form-check-label" :for="i.type">
                {{ i.type }}
              </label>
            </div>
          </div>
          {{ filters_selected.type }}
          {{ Array.isArray(filters_selected.type) }}

        </div>

        <div class="year">
          <h3>Years</h3>
          <div v-for="i in initial_filter_data.year" :key="i.id">
            <div class="form-check form-switch">
              <input class="form-check-input" type="checkbox" role="switch" :id="i.year_published" :value="i.id"
                v-model="filters_selected.year" />
              <label class="form-check-label" :for="i.year_published">
                {{ i.year_published }}</label>
            </div>
          </div>
        </div>

        <div class="author">
          <h3>Author</h3>
          <input type="text" class="form-control" v-model="authorQuery" placeholder="filter types" />

          <div v-for="i in computedAuthor" :key="i.id">
            <div class="form-check form-switch">
              <input class="form-check-input" type="checkbox" role="switch" :id="i.name" :value="i.id"
                v-model="filters_selected.author" />
              <label class="form-check-label" :for="i.name">
                {{ i.name }}</label>
            </div>
          </div>
        </div>

        <div class="material">
          <h3>Material</h3>

          <input type="text" class="form-control" v-model="materialQuery" placeholder="filter types" />

          <div v-for="i in computedMaterial" :key="i.id">
            <div class="form-check form-switch">
              <input class="form-check-input" type="checkbox" role="switch" :id="i.material" :value="i.id"
                v-model="filters_selected.material" />
              <label class="form-check-label" :for="i.material">
                {{ i.material }}</label>
            </div>
          </div>
        </div>
        <!-- last div closes Filters -->
      </div>
      <!-- All results under this div  -->
      <div class="results col-9">
        <div class="pb-1 m-0" v-for="i in results_data.results" :key="i.id">
          <div class="card">
            <div class="col">
              <div class="card-header">
                <h1 class="display-6 my-0">Title : {{ i.title }}</h1>
              </div>
              <div class="container-xxl">
                <div class="row align-items-center">
                  <div class="card-body text-start p-0 col-md-8">
                    <ul class="list-group-flush my-1">
                      <li class="list-group-item">
                        <ul class="
                            list-group list-group-horizontal
                            border-0
                            m-0
                            p-0
                          ">
                          <li class="list-group-item border-0 p-0 mx-auto">
                            <strong>Type: </strong>
                            <div class="list-inline-item" id="type_id">
                              {{ i.type_id }}
                            </div>
                          </li>
                          <li class="
                              list-group-item
                              border-0
                              align-end
                              m-0
                              p-0
                              mx-auto
                            ">
                            <strong>Year: </strong>
                            <div class="list-inline-item" id="year">
                              {{ i.year_id }}
                            </div>
                          </li>
                        </ul>
                      </li>

                      <li class="list-group-item">
                        <div class="fw-bold">Materials :</div>
                        <div class="
                            list-inline-item
                            badge
                            bg-light
                            text-dark
                            fw-normal
                            fs-6
                          " v-for="p in i.material.length" :key="p.id" id="material">
                          {{ i.material[p - 1] }}
                        </div>
                      </li>
                      <li class="list-group-item">
                        <div class="fw-bold">Author(s) :</div>
                        <div id="author" class="list-inline-item" v-for="p in i.author.length" :key="p.id">
                          {{ i.author[p - 1].name }}
                        </div>
                      </li>

                      <li class="list-group-item">
                        <div class="fw-bold">Tags :</div>
                        <div class="list-inline-item" v-for="p in i.tag.length" :key="p.id" id="tags">
                          {{ i.tag[p - 1] }}
                        </div>
                      </li>

                      <li class="list-group-item">
                        <details>
                          <summary>Abstract</summary>
                          {{ i.abstract }}
                        </details>
                      </li>
                    </ul>
                  </div>
                  <div class="
                      card-body
                      col-md-3
                      text-center
                    ">
                    <div class="btn-group-vertical gap-3 mx-auto">
                      <button class="btn btn-primary" type="button" :href="i.pdf" target="_blank">Open PDF</button>
                      <!-- Open pdf stopped working... no idea why -->
                      <button class="btn btn-primary" type="button" @click="
                        this.$router.push({
                          name: 'SearchDetail',
                          params: { id: i.id },
                        }) // -> /search/detail/i.id/
                      ">Details</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <nav aria-label="Page navigation" v-if="results_data.total_pages > 1">
          <ul class="pagination justify-content-center-bottom">
            <li class="page-item" :class="{ disabled: hidePreviousButton }">
              <a class="page-link" @click="loadPrev()">Previous</a>
            </li>
            <div v-for="i in results_data.total_pages" :key="i.id">
              <li class="page-item" :class="{ active: currentPage == i }">
                <a class="page-link" @click="goToPage(i)"> {{ i }} </a>
              </li>
            </div>
            <li class="page-item" :class="{ disabled: hideNextButton }">
              <a class="page-link" @click="loadNext()">Next</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
import { getAPI, getPage } from "../..//axios-api";

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
      typeQuery: [],
      authorQuery: [],
      materialQuery: [],
      // computedtags: [],
      // computedTypes: [],
      // computedAuthor:[],
      total_pages: 0,
      hideNextButton: true,
      hidePreviousButton: false,
      currentPage: 1,
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

    //  RESULTS INITIAL DATA, All Paper object results paginated 
    getAPI
      .get("/paper/")
      .then((response) => {
        this.results_data = response.data;
        this.hideNextButton = false;
        this.hidePreviousButton = true;

        console.log("Paper api data recieved and logged , no error!");
      })
      .catch((err) => {
        console.log(err);
      });
  },
  watch: {
    // watches for the filter fields, 
    // when anything changes it makes the correct API call with the filters
    // and adds to url 
    filters_selected: {
      handler() {
        this.currentPage = 1;
        this.hideNextButton = false;
        this.hidePreviousButton = true;
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
    computedTypes(typeQuery) {
      return this.initial_filter_data.type.filter((x) =>
        x.type.toLowerCase().includes(this.typeQuery)
      );
    },
    computedAuthor(authorQuery) {
      return this.initial_filter_data.author.filter((x) =>
        x.name.toLowerCase().includes(this.authorQuery)
      );
    },
    computedMaterial(materialQuery) {
      return this.initial_filter_data.material.filter((x) =>
        x.material.toLowerCase().includes(this.materialQuery)
      );
    },
    displayPages() {
      const totalPages = this.total_pages;
      let currentPage = this.currentPage;

      if (totalPages > 3) {
        if ([1, 2].includes(currentPage)) currentPage = 3;
        else if ([totalPages - 1, totalPages].includes(currentPage)) currentPage = totalPages - Math.trunc(5 / 2);
        return [...Array(5).keys()].map(i => i - Math.trunc(5 / 2) + currentPage)
      } else {
        return totalPages
      }
    }


  },
  methods: {
    sayHi() {
      console.log("hi, this test funtion has activated")
      // dummy testing function
    },

    loadNext() {
      this.currentPage += 1;

      getAPI
        .get(`/paper/?page=${this.currentPage}`, {
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
          console.log(response.data);

          this.results_data = response.data;

          this.hideNextButton = true;
          if (this.results_data.next) {
            this.hideNextButton = false;
          }
          this.hidePreviousButton = true;
          if (this.results_data.previous) {
            this.hidePreviousButton = false;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    loadPrev() {
      this.currentPage -= 1;

      getAPI
        .get(`/paper/?page=${this.currentPage}`, {
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
          console.log(response.data);
          this.results_data = response.data;

          this.hideNextButton = true;
          if (this.results_data.next) {
            this.hideNextButton = false;
          }
          this.hidePreviousButton = true;
          if (this.results_data.previous) {
            this.hidePreviousButton = false;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },

    goToPage(i) {
      this.currentPage = i;
      getAPI
        .get(`/paper/?page=${this.currentPage}`, {
          params: {
            title: this.filters_selected.title,
            year: this.filters_selected.year,
            type: this.filters_selected.type,
            language: this.filters_selected.language,
            author: this.filters_selected.author,
            tag: this.filters_selected.tag,
            material: this.filters_selected.material,
            page: this.currentPage,
          },
        })
        .then((response) => {
          console.log(response.data);
          this.results_data = response.data;

          this.hideNextButton = true;
          if (this.results_data.next) {
            this.hideNextButton = false;
          }
          this.hidePreviousButton = true;
          if (this.results_data.previous) {
            this.hidePreviousButton = false;
          }
        })
        .catch((err) => {
          console.log(err);
        });
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
