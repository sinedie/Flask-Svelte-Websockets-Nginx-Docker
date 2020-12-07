<script>
    import { metatags } from '@roxi/routify'

    import io from 'socket.io-client';

    metatags.title = 'My Routify app'
    metatags.description = 'Description coming soon...'


    const socket = io();


    async function say_hi() {
        try {
            const fetching = await fetch(
                '/api/say_hi', {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
            });

            const response = await fetching.json()

            console.log(response)
        } catch {
            console.log('Some error happened while sending the request')
        }
    }


    function say_hi_websockets() {
        socket.emit('say_hi');
    }


    function start_task() {
		socket.emit('simple_start_task');
    }


    socket.on('greetings', (data) => {
		console.log(data);
    });
    

    socket.on('task_finished', (data) => {
        console.log('Long task as finished with result: ')
		console.log(data);
	});

</script>


<button on:click={say_hi}>
	Say hi from a normal request
</button>


<button on:click={say_hi_websockets}>
	Say hi from websockets
</button>


<button on:click={start_task}>
	Start long task on celery
</button>
