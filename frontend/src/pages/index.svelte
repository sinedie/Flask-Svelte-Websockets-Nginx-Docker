<script>
    import { metatags } from '@roxi/routify'

    metatags.title = 'My Routify app'
    metatags.description = 'Description coming soon...'


    async function REST_healtcheck() {
        try {
            const fetching = await fetch(
                '/api/', {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }
            });

            const response = await fetching.json()

            console.log(response)
        } catch {
            console.log('Some error happened while sending the request')
        }
    }


    async function protected_endpoint() {
        try {
            const response = await fetch(
                '/api/protected', {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('authToken')}`
                }
            });

            const responseJSON = await response.json()

            console.log(responseJSON)
        } catch {
            console.log('Some error happened while sending the request')
        }
    }


    async function fresh_protected_endpoint() {
        try {
            const fetching = await fetch(
                '/api/protected-fresh', {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('authToken')}`
                }
            });

            const response = await fetching.json()

            console.log(response)
        } catch {
            console.log('Some error happened while sending the request')
        }
    }


    async function fresh_long_task() {
        try {
            const fetching = await fetch(
                '/api/async_task', {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('authToken')}`
                }
            });

            const response = await fetching.json()

            console.log(response)
        } catch {
            console.log('Some error happened while sending the request')
        }
    }

</script>


<button on:click={REST_healtcheck}>
	REST API Healtcheck
</button>

<button on:click={protected_endpoint}>
	Fetch proteted endpoint
</button>

<button on:click={fresh_protected_endpoint}>
	Fetch proteted endpoint with fresh token
</button>

<button on:click={fresh_long_task}>
	Fetch proteted long_task
</button>