import fetch from 'isomorphic-fetch';

    const apiurl = 'http://localhost:5000/api/'
    const origin = "http:/WritersWorkshop/testApi.html"

    export const fetchGroups = async(setGroups, setLoading) => {
        const api = apiurl + 'group/all'
        const response = await fetch(api,{
            method: 'GET',
            headers: {
                'Content-Type': 'text/html',
                'Origin': origin
            },
        })
        const answer = await response.json()
        console.log(answer);
        const groups = await buildGroups(answer)
        setGroups(groups) 
        setLoading(false)
    }
    export const buildGroups = async(answer) => {
        var groups = []
        for (let k=0; k <= answer.count-1; k++) {
            groups[k] = answer.groups[k] // build array
        }
        return groups
    }

    export const fetchGenres = async(setGenres, setLoading) =>{
        const api = apiurl + 'genre/all'
        const response = await fetch(api,{
            method: 'GET',
            headers: {
                'Content-Type': 'text/html',
                'Origin': origin
            },
        })
        const answer = await response.json()
        console.log(answer);
        const genres = await buildGenres(answer)
        setGenres(genres)
        setLoading(false)
    }
    export const buildGenres = async(answer) => {
        var genres = []
        for (let k=0; k <= answer.count-1; k++) {
            genres[k] = answer.genres[k] // build array
        }
        return genres
    }
