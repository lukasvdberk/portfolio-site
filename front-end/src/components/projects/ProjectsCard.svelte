<script>
    import Img from "../common/StandardImage.svelte"
    import Tag from "../common/Tag.svelte"

    export let images
    export let title
    export let shortDescription
    export let slug;
    export let tags = undefined;
</script>

<style>
    article {
        position: relative;
        box-shadow: 0 1px 1px 0 rgba(0,0,0,0.07),0 3px 1px -2px rgba(0,0,0,0.6),0 1px 5px 0 rgba(0,0,0,0.2);
        border-radius: 5px;
        text-align: left;
        padding: 5px;
    }

    div.img {
        position: relative;
        height: 350px;
        width: 98%;
        margin: 0;
        padding: 0;
    }

    h1, p {
        text-align: center;
    }

    div.tag-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
    }

    div.tag {
        display: inline-block;
        width: 100px;
        margin: 1px;
    }

    div.no-image {
        opacity: 0.4;
        width: 100%;
    }

    a, a::after {
        position: relative;
        display: block;
        width: 60%;
        color: white;
        padding: 2%;
        border-radius: 5px;
        background-color: #001021;
        text-decoration: none;
        margin: 0 auto;
        text-align: center;
        transition: 1s;
        align-content: center;
    }

    a:hover {
        background-color: lightblue;
    }

    p {
      display: -webkit-box;
      -webkit-line-clamp: 1;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
</style>
<article>
    <div class="img">
        {#if images.length > 0}
            <Img src={images[0]["image"]} alt={title} />
        {:else}
            <div class="no-image">
                <Img src="no-image-available.png" alt={title} />
            </div>
        {/if}
    </div>
    <h1>{title}</h1>
    <div class="tag-container">
        {#each tags as tag}
            <div class="tag">
                <Tag txt={tag.name} icon="{tag.icon}" timing="0" />
            </div>
        {/each}
    </div>
    <p>{shortDescription}</p>
    <a href="/projects/{slug}">Learn more</a>
</article>