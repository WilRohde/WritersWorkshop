function getGroups() {
    const api = 'http://localhost:5000/api/group/all'
    const request = fetch(api,{
        method: 'GET',
        headers: {
            'Content-Type': 'text/html',
            'Origin': "http:/WritersWorkshop/testApi.html"
        },
    })
        .then(response => response.json())
        .then(data => {
            console.log("calling callback function")
            buildGroups(data)})
        .catch(error => console.log(error))
}

function buildGroups(answer) {
    console.log(answer)
    var groups = []
    for (k=0; k <= answer.count-1; k++) {
        groups[k] = answer.groups[k] // build array
    }
    return groups
}
