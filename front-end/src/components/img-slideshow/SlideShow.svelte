<script>
    import Img from "../common/StandardImage.svelte";
    import {onDestroy} from 'svelte';

    // Should be a list of links
    export let images = [];

    // in seconds
    const switchTimer = 4;

    let currentImage = undefined
    if(images.length > 1) {

        currentImage = images[0];
        const interval = setInterval(() => {
             let newImageIndex= images.indexOf(currentImage) + 1;

             if(images.length === newImageIndex) {
                 newImageIndex = 0;
             }

             currentImage = images[newImageIndex];
        }, switchTimer * 1000);

        onDestroy(() => {
		    clearInterval(interval);
	    });
    } else {
        currentImage = images[0];
    }

    function setImage(image) {
        currentImage = image;
    }
</script>

<style>
    div.center {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    img {
        width: 100%;
        height: 60vh;
        object-fit: scale-down;
    }

    .img-animation {
        animation-name: trans;
        animation-iteration-count: infinite;
        animation-duration: 4s;
    }

    @keyframes trans {
        0% {opacity: 0.0}
        25% {opacity: 1}
        75% {opacity: 1}
        100% {opacity: 0.0}
    }

    span {
        height: 25px;
        width: 25px;
        border: solid black 2px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 5px;
    }

    span:hover {
        cursor: pointer;
    }

    .current-image {
        background-color: #001021;
    }

    .not-current-image {
        background-color: white;
        border-color: #001021;
    }
</style>

<div class="center">
    {#if images.length === 1}
        <img src="{currentImage}" alt="project-image" />
    {:else}
        <img class="img-animation" src="{currentImage}" alt="project-image" />
    {/if}

</div>

{#if images.length > 1}
    <div class="center">
        <!--  Shows the little dots for the available images  -->
        {#each images as image }
            {#if image === currentImage}
                <span class="current-image" on:click={() => setImage(image)}></span>
            {:else}
                <span class="not-current-image" on:click={() => setImage(image)}></span>
            {/if}
        {/each}
    </div>
{/if}