<template>
    <div class="searchdetail">
        <h1>search detail</h1>
        <p>The Id is {{$route.params.id}} ( via $route thing) </p>
        <p>The Id is {{id}} ( via prop thing) </p>
        <p>{{APIdata}}</p>
    </div>
</template>

<script>
import{getAPI} from '../..//axios-api'

export default {
    data(){
        return{
            APIdata: null
        }
    },
    props: ['id',],
    mounted(){
        getAPI.get('/paper/' + this.id ,)
        .then(response => {
            console.log('Paper api data with id = ' +this.id +' recieved ')
            this.APIdata = response.data
        })
        .catch(err => {
            console.log(err)
        })
    }
}
</script>