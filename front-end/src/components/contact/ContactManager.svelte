<script>
    import Contact from "./Contact.svelte"

    import getContactsInfo from "./contact.js"

    const contactsInfo = getContactsInfo()
</script>

<style>
    div {
        display: block;
        width: 100%;
        position: relative;
        margin-top: 2.5%;
    }

    h1 {
        text-align: left;
    }

    @media (max-width: 1000px) {
        h1 {
            text-align: center;
        }
    }
</style>

<h1>Contact me at</h1>
{#each contactsInfo as contact}
    <div>
        <Contact {contact} />
    </div>
{/each}
