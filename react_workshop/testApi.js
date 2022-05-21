import {fetch} from 'node-fetch'
const api = 'http://localhost:5000/api/group/all'
const request = fetch.fetch(api)
    .then(response => response.text())
    .then(data => console.log(data))
