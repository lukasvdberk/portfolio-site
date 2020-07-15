<script>
    import Contact from "./Contact.svelte"

    import getContactsInfo from "./contact.js"

    const contactsInfo = getContactsInfo() 
</script>

<h1>Contact me at</h1>
{#each contactsInfo as contact}
    <Contact {contact} />
{/each}