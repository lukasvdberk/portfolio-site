<script>
    import getAboutMeTags from "./about-me.js" 
    import Tag from "../common/Tag.svelte"
    import { fade } from 'svelte/transition';
    import {onDestroy, onMount} from 'svelte';

    let allAboutMeTags = []

    // In seconds
    const timing = 4
    let currentTxt = "";

    function setRandomTag() {        
        let newText = allAboutMeTags[Math.floor(Math.random() * allAboutMeTags.length)]

        if(newText !== currentTxt) {
            currentTxt = newText
        }
    }

    const interval = setInterval(setRandomTag, timing * 1000)

    onMount(() => {
        getAboutMeTags().then((result) => {
            allAboutMeTags = result
            setRandomTag()
        })
    })

    onDestroy(() => {
		clearInterval(interval);
	});
</script>

<style>
    div, div::after {
        width: 200px;
        margin: 0 auto;
    }
</style>
<div>
    {#if currentTxt}
        <Tag txt={currentTxt} {timing} />
    {/if}
</div>