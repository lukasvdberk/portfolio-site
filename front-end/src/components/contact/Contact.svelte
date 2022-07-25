<script>
    export let contact
</script>

<style>
    div.container {
        display: block;
        height: 30px;
        width: 100%;
    }

    a {
        display: inline-block;
        position: relative;
        margin-left: 2.5%;
        font-size: 15px;
        float: left;
    }

    img {
        display: inline-block;
        float:left;
        height: 30px;
        width: 30px;
        border-radius: 10%;
    }

    @media (max-width: 1000px) {
        .container {
            margin: 0 auto;
        }

        a {
            vertical-align: top;
        }

        a, img {
            text-align: center;
            float: none;
        }
    }
</style>
<div class="container">
    <img src="{contact.img}" alt={contact.name} />
    <a href="{contact.link}">Contact me at {contact.name}</a>
</div>
