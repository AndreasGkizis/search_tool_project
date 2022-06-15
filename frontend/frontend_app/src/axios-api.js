import axios from "axios";


// this will be used by axios as a base to add other stings to make api calls
const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 5000, 
})

export {getAPI, }