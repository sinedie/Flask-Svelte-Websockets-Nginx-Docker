<script>
    import { url, goto } from '@roxi/routify'
    import { fade } from 'svelte/transition';

    import { valid_email, valid_password, valid_username } from '../../utils/validators'

    let username
    let email
    let password
    let password_verification
    let error


    async function register() {

        if (password !== password_verification) {
            error = 'Contraseñas no coinciden'
            return
        }

        const response = await fetch(
            '/api/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                username,
                email,
                password
            })
        });

        const responseJSON = await response.json();

        if (response.status == 200) {
            localStorage.setItem('authToken', responseJSON.access_token)
            localStorage.setItem('refreshToken', responseJSON.refresh_token)
            $goto('/');
        } else {
            error = responseJSON.msg;
        }
    }

</script>


<style>
    .parent {
        width: 100%;
        display: grid;
        place-items: center;
    }
    .container {
        min-width: 25vw;
        display: grid;
        grid-template-rows: 12vh 1fr;
    }
    .error {
        text-align: center;
        color: red;
    }
    .wrong-validation {
        border-color: red;
    }
    form {
        padding: 3vh 5vw 5vh 5vw;
    }
    h1 {
        margin: 0;
        padding: 0;
        background-color: rgba(31, 45, 51, 0.5);
        padding: 4vh 0 0 5vw;
    }
    label {
        display: flex;
        flex-direction: column;
        margin-top: 2vh;
    }
    span {
        margin-bottom: 1vh;
    }
    button {
        margin-top: 3vh;
        width: 100%;
    }
    button:hover {
        cursor: pointer;
    }
</style>


<div class='parent'>

    <div class='container'>

        <h1> Login </h1>

        <form>
            <label>
                <span> Username </span>
                <input
                    type='text'
                    placeholder='eg. user123'
                    bind:value={username}
                    class:wrong-validation={() => !valid_username(username)}
                    />
                     
            </label>

            <label>
                <span> Email </span>
                <input
                    type='email'
                    placeholder='eg. user@example.com'
                    bind:value={email}
                    class:wrong-validation={() => !valid_email(email)}
                    />
                     
            </label>
            
            <label>
                <span> Contraseña </span>
                <span> Mínimo 8 letras (1 mayuscula, 1 minuscula, 1 numero y 1 letra especial) </span>
                <input
                    type='password'
                    placeholder='************'
                    bind:value={password}
                    class:wrong-validation={() => !valid_password(password)}
                    />
            </label>

            <label>
                <span> Verificar contraseña </span>
                <span> 
                    {#if password !== password_verification}
                        No coinciden
                    {/if}
                </span>
                <input
                    type='password'
                    placeholder='************'
                    bind:value={password_verification}
                    class:wrong-validation={() => !valid_password(password)}
                    />
            </label>

            {#if error}
                <!-- svelte-ignore a11y-label-has-associated-control -->
                <label>
                    <span class='error' transition:fade>
                        {error}
                    </span>
                </label>
            {/if}

            <button on:click|preventDefault={register}>
                Registarse
            </button>

        </form>

        <a href={$url('/login')}>Iniciar sesion</a>
        
    </div>
</div>
