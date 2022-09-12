<template>
  <div class="searchdetail">
      <div class="card">
        <div class="card-header">
          <h1 class="display-6 my-0">Title : {{ results_detail.title }}</h1>
        </div>
        <div class="card-body text-start p-0">
          <ul class="list-group-flush border-0 my-1">
            <li class="list-group-item">
              <div class="fw-bold list-inline-item">Authors :</div>
              <div class="list-inline-item badge bg-light text-dark fw-normal fs-6" v-for="p in results_detail.author"
                :key="p.id" id="material">
                {{ p.name }}
              </div>
            </li>

            <li class="list-group-item">
              <div class="fw-bold list-inline-item">Year :</div>
              <div class="list-inline-item badge bg-light text-dark fw-normal fs-6">
                {{ results_detail.year_id }}
              </div>
            </li>

            <li class="list-group-item">
              <div class="fw-bold list-inline-item">Type :</div>
              <div class="list-inline-item badge bg-light text-dark fw-normal fs-6">
                {{ results_detail.type_id }}
              </div>
            </li>

            <li class="list-group-item">
              <div class="fw-bold list-inline-item">Materials :</div>
              <div class="list-inline-item badge bg-light text-dark fw-normal fs-6" v-for="p in results_detail.material"
                :key="p.id" id="material">
                {{ p }}
              </div>
            </li>
            <li class="list-group-item">
              <div class="fw-bold list-inline-item">Language :</div>
              <div class="list-inline-item badge bg-light text-dark fw-normal fs-6" v-for="p in results_detail.language"
                :key="p.id" id="material">
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
          <div class="list-inline-item badge rounded-pill bg-secondary fw-normal fs-6" v-for="p in results_detail.tag"
            :key="p.id" id="material">
            {{ p }}
          </div>
        </div>
      </div>

    <div class="card-body text-center">
      <div class="btn-group-lg gap mx-auto">
        <button class="btn btn-primary" type="button" :href="results_detail.pdf" target="_blank">Open PDF</button>
        <button class="btn btn-primary" type="button" @click="this.$router.back()">Back</button>
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
        this.results_detail = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
