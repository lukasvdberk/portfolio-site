<script>
    export let src;
    export let alt;
</script>

<style>
    img {
        object-fit: scale-down;
        width: 100%;
        height: 100%;
        border-radius: 5px;
    }
</style>

<img src={src} alt={alt} />