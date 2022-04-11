<template>
  <div>
    <div>
      <div>
        Filters passed down to child <br />
        {{ filter_data }}
      </div>
      <br />
      <div>Data filtered_data: <br />{{ filteredPapers }}</div>
    </div>
    <h1>RESULTS</h1>
    <div v-for="i in filtered_data" :key="i.id">
      <h3>{{ i.title }}</h3>
      <p>{{ i.abstract }}</p>
    </div>
  </div>
</template>

<script>
import { getAPI } from "../..//axios-api";

export default {
  props: {
    filter_data: Object,
  },
  data() {
    return {
      initial_data: [],
      filtered_data: [],
    };
  },
  // watch : {
  //   filter_data: function(value) {
  //     console.log(value)
  //   }
  // },
  computed: {
    filteredPapers() {
      console.log("filteredPapers run ");

      this.$router.push({
        path: "/search",
        query: {
          title: this.filter_data.title,
            year: this.filter_data.year,
            type: this.filter_data.type,
            language: this.filter_data.language,
            author: this.filter_data.author,
            tag: this.filter_data.tag,
            material: this.filter_data.material,
        },
      });

      getAPI
        .get("/paper", {
          params: {
            title: this.filter_data.title,
            year: this.filter_data.year,
            type: this.filter_data.type,
            language: this.filter_data.language,
            author: this.filter_data.author,
            tag: this.filter_data.tag,
            material: this.filter_data.material,
          },
        })
        .then((response) => {
          console.log("getapi filteredPapers hit");
          console.log();
          this.filtered_data = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mounted() {
    getAPI
      .get("/paper/")
      .then((response) => {
        this.initial_data = response.data;
        console.log("Paper api data recieved and logged results.vue, no error");
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    // updateNav() {
    //   // console.log('updateNav ' + this.$route.href.split("?")[1])
    //   // { title: ..., tags: [..]}
    //   // this.$router.push({query: this.fields})
    //   // this.$router.push({path: this.$route.path, query:  this.fields})
    //   // this.$router.push({path: 'about', query: {title: this.title}})

    //   this.$router.push({
    //     path: "/search",
    //     query: {
    //       title: this.selected_fields.title,
    //       tag: this.selected_fields.tags,
    //       author: this.selected_fields.author,
    //     },
    //     // prepei na prosthesw ola ta filtra  ayto fainete na douleuei kai me adeia pedia, alla DEN me fernei sthn selida an to balw sto url bar kateytheian
    //   });

    //   // console.log('this.selected_fields.tag = ' + this.selected_fields.tags)
    //   // console.log('this.selected_fields.title = ' + this.selected_fields.title)
    //   // console.log('href = ' + this.$route.href)
    //   // console.log('query = ' + this.$route.params)

    //   console.log("this.$route.href = " + this.$route.href);

    //   getAPI
    //     .get("/paper", {
    //       params: {
    //         title: this.selected_fields.title,
    //         tag: this.selected_fields.tags,
    //         author: this.selected_fields.author,
    //       },
    //     })
    //     .then((response) => {
    //       this.APIpaperData = response.data;
    //     })
    //     .catch((err) => {
    //       console.log(err);

    //       // hard coded sinithos to ?title=kati

    //       // this.$router.push({path: this.$route.path, query: {title: this.title}})

    //       console.log("===== after 2 =====");
    //       console.log("title = " + this.title);
    //       console.log(
    //         "this.$route.query = " + JSON.stringify(this.$route.query)
    //       );
    //       console.log("this.$route.href = " + this.$route.href);
    //       console.log(response.data);
    //     });
    // },
    sayhi() {
      console.log("hi hi hi");
    },
  },
  // computed: {
  //     urlUpdate() {

  //         return this.$router.push({query: {title: this.title }})
  //     }
  // }
};

//  console.log(this.$route.query)
//         getAPI.get('/paper/'+ this.$route.href.split('?')[1] )
//         .then(response => {
//             console.log('Paper api data recieved ')
//             this.APIpaperData = response.data
//         })
//         .catch(err => {
//             console.log(err)
//         })
</script>