<template>
<div class="search">

    <h1>Search page</h1>
    <div v-for="i in APIdata" :key="i.id">
        <router-link :to="{ name: 'SearchDetail', params: {id:i.id }}">
            {{i.title}}
        </router-link>
    </div>
</div>
</template>

<script>
import{getAPI} from '../..//axios-api'
export default {
    data() {
        return {
            APIdata: []
        }
            
        },
    mounted() {
        getAPI.get('/paper/',)
        .then(response => {
            console.log('Paper api data recieved ')
            this.APIdata = response.data
        })
        .catch(err => {
            console.log(err)
        })
    }
}
</script>