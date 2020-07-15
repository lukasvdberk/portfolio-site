<script>
    export let contact
</script>

<style>
    a {
        position: relative;
        display: inline-block;
        height: 5%;
        margin-left: 5%;
        text-decoration: none;
    }

    a > * {
        text-align: center;
        height: 2.5%;
        padding: 0;
        margin: 0;
    }

    img {
        border-radius: 10%;
    }

    .img-with-text {
        text-align: justify;
    }
</style>
<a class="img-with-text" href={contact.link}>
    <img src={contact.img} alt={contact.name} />
    <p>{contact.name}</p>
</a>
