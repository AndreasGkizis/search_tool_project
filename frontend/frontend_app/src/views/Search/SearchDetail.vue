<template>
  <div class="searchdetail">
    <h1>search detail</h1>
    <p>The Id is {{ $route.params.id }} ( via $route thing)</p>
    <p>The Id is {{ $route.params }} ( via $route thing)</p>
    <p>The Id is {{ id }} ( via prop thing)</p>
    <p>{{ results_detail }}</p>

    <div class="results">
      <div class="card">
        <div class="card-header">
          <h1 class="display-6 my-0">Title : {{ results_detail.title }}</h1>
        </div>
        <div class="card-body text-start p-0">
          <ul class="list-group-flush border-0 my-1">
            <li class="list-group-item">
              <div class="fw-bold list-inline-item">Authors :</div>
              <div
                class="list-inline-item badge bg-light text-dark fw-normal fs-6"
                v-for="p in results_detail.author"
                :key="p.id"
                id="material"
              >
                {{ p.name }}
              </div>
            </li>

            <li class="list-group-item">
              <div class="fw-bold list-inline-item">Year :</div>
              <div
                class="list-inline-item badge bg-light text-dark fw-normal fs-6"
              >
                {{ results_detail.year_id }}
              </div>
            </li>

            <li class="list-group-item">
              <div class="fw-bold list-inline-item">Type :</div>
              <div
                class="list-inline-item badge bg-light text-dark fw-normal fs-6"
              >
                {{ results_detail.type_id }}
              </div>
            </li>

            <li class="list-group-item">
              <div class="fw-bold list-inline-item">Materials :</div>
              <div
                class="list-inline-item badge bg-light text-dark fw-normal fs-6"
                v-for="p in results_detail.material"
                :key="p.id"
                id="material"
              >
                {{ p }}
              </div>
            </li>
            <li class="list-group-item">
              <div class="fw-bold list-inline-item">Language :</div>
              <div
                class="list-inline-item badge bg-light text-dark fw-normal fs-6"
                v-for="p in results_detail.language"
                :key="p.id"
                id="material"
              >
                {{ p }}
              </div>
            </li>

            <li class="list-group-item">
              <div class="fw-bold list-inline-item">Abstract</div>
              <div class="card-text">
                {{ results_detail.abstract }}
              </div>
            </li>
          </ul>
        </div>
        <div class="card-footer">
            <div class="fw-bold list-inline-item">Tags :</div>
            <div
              class="list-inline-item badge rounded-pill bg-secondary fw-normal fs-6"
              v-for="p in results_detail.tag"
              :key="p.id"
              id="material"
            >
              {{ p }}
            </div>
        </div>
      </div>
    </div>
    <button type="button"
          class="btn btn-primary" 
          @click="this.$router.back()">
    Go back </button>
    <div class="popuppdf">
      <div class="container p-5">
        <!-- Button trigger modal -->
        <button
          type="button"
          class="btn btn-primary"
          data-bs-toggle="modal"
          data-bs-target="#exampleModal"
        >
          Open PDF
        </button>
        <!-- Modal -->
        <div
          class="modal fade"
          id="exampleModal"
          tabindex="-1"
          aria-labelledby="exampleModalLabel"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-fullscreen modal-dialog-scrollable">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title text-danger" id="exampleModalLabel">
                  PDF
                </h5>
                <button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></button>
              </div>
              <div class="modal-body">
                <iframe
                  src="https://therichpost.com/sample.pdf#toolbar=0&navpanes=0&scrollbar=0"
                  frameBorder="0"
                  scrolling="auto"
                  height="500%"
                  width="100%"
                >
                </iframe>
              </div>
              <div class="modal-footer">
                <button
                  type="button"
                  class="btn btn-warning"
                  data-bs-dismiss="modal"
                >
                  Close
                </button>
              </div>
            </div>
          </div>
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
      results_detail: [],
    };
  },
  props: ["id"],
  mounted() {
    getAPI
      .get("/paper/" + this.id)
      .then((response) => {
        console.log("Paper api data with id = " + this.id + " received ");
        this.results_detail = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>