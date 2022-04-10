<template>
<div class="container">
    <div class="filter">
        <Filter 
        />
    </div>
</div>

</template>

<script>
import Filter from './Filter.vue'

export default {
    components: {
        Filter,
        
    },
}
</script>

<style>
.container {
    display: flex;
    margin: 20px;
    align-content: center;
    width: 100%;
    padding: auto;
}


</style>