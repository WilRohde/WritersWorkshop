// 05/25/2022 - have to uncomment and get this working...
    const apiurl = 'http://localhost:5000/api/'
    const origin = "http:/WritersWorkshop/testApi.html"
    export const fetchGroups = () => {
        this.setState({loading: true})
        const api = apiurl + 'group/all'
        const request = fetch(api,{
            method: 'GET',
            headers: {
                'Content-Type': 'text/html',
                'Origin': origin
            },
        })
            .then(response => response.json())
            .then(data => {buildGroups(data)})
            .then(groups => 
                this.state({groups, loading: false}))
            .catch(error => console.log(error))
    }

    function buildGroups(answer) {
        console.log(answer)
        var groups = []
        for (let k=0; k <= answer.count-1; k++) {
            groups[k] = answer.groups[k] // build array
        }
        return groups
    }

    // componentDidMount() {
    //     const myGroups = 
    //     this.setState({groups: props.state.groups})
    // }

