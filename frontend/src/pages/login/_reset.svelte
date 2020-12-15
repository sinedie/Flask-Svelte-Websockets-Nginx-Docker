<script>
    import { goto } from '@roxi/routify'

    if (localStorage.getItem('authToken')) {
        $goto('/')
    }
</script>

{#if !localStorage.getItem('authToken')}
    <slot/>
{/if}