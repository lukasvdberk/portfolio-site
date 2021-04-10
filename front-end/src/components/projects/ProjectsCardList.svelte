<script>
    import ProjectCard from "./ProjectsCard.svelte";

    export let projects;
</script>

<style>
    div {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-gap: 25px;
        justify-content: space-evenly;
    }

    @media only screen and (max-width: 1200px) {
        div {
            grid-template-columns: 1fr 1fr;
        }
    }
    @media only screen and (max-width: 800px) {
        div {
            grid-template-columns: 1fr;
        }
    }
</style>

<div>
    {#each projects as project}
        <ProjectCard
            title={project.name}
            shortDescription={project.short_description}
            images={project.images}
            slug={project.slug}
            tags={project.tags}
        />
    {/each}
</div>
