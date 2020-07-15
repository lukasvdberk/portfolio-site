<script>
    export let txt = undefined;
    export let timing = 2;
    // Source of the icon (url)
    export let icon = undefined
</script>

<style>
    div {
		color: white;
        background-color: #001021;
        border: solid lightblue 5px;
        border-radius: 150px;
        text-align: center;
    }

    h3 {
        /*margin: 2%;*/
        /*padding: 2%;*/
        font-size: 20px;
        padding-top: 10px;
    }

    img {
        width: 30px;
        height: 30px;
    }

    h3, img {
        display: inline-block !important;
        vertical-align: middle;
    }

    .animate {
        animation-name: trans;
        animation-iteration-count: infinite;
    }

    @keyframes trans {
        0% {opacity: 0.0}
        25% {opacity: 1}
        75% {opacity: 1}
        100% {opacity: 0.0}
    }

</style>

<div class="animate" style="animation-duration: {timing}s">
    {#if icon}
        <img src={icon} alt="txt" />
    {/if}
    <h3>{txt}</h3>
</div>