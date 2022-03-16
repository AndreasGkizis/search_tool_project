<template>
<div class="search">

    <h1>Search page</h1>
    <p>what the hell...</p>
    <button >
        <router-link :to="{ name: 'SearchDetail'}"> Details </router-link>
    </button>

    <div v-for="paper in papers" :key="paper.id">
        <p>looped</p>
        {{ paper.title }}
    </div>
</div>
</template>

<script>
export default {
    data() {
        return 
            papers: []
        },
    mounted() {
        fetch('http://127.0.0.1:8000/paper/') 
            // .then(res => res.json())
            .then(data => this.papers = data)
            .catch(err => console.log(err.message))
        console.log("fetched papers")
    }
}
</script>