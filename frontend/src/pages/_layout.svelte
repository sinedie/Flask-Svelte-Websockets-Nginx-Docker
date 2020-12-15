<!-- routify:options preload="proximity" -->
<script>
    import { goto } from '@roxi/routify'


    async function checkTokenValidation() {

        if (!localStorage.getItem('authToken')) {
            $goto('/login')
            return false
        }

        const response = await fetch(
            '/api/auth/validate-token', {
            method: "GET",
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('authToken')}`
            }
        });

        if (response.status == 200) {
            return true
        }

        localStorage.setItem('authToken', null)

        return await refreshToken()
    }
    

    async function refreshToken() {

        if (!localStorage.getItem('refreshToken')) {
            $goto('./login', {}, true)
            return false
        }

        const response = await fetch(
            '/api/auth/refresh', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('refreshToken')}`,
            }
        });

        const responseJSON = await response.json()

        if (response.status == 200) {
            const accessToken = responseJSON.access_token;
            localStorage.setItem('authToken', accessToken)
            return true
        }

        localStorage.setItem('refreshToken', null)

        $goto('./login', {}, true)
        return false
    }


</script>


{#await checkTokenValidation()}
    Revisando credenciales...
{:then response} 
    {#if response}
        <slot />
    {:else}
        Something happened... You should've been redirected to Login page
    {/if}
{/await}