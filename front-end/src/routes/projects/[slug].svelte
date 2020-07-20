<script context="module">
	import {fetchProject} from '../../components/projects/projects';
	import Container from "../../components/common/Container.svelte";


	import marked from 'marked';
	let projectData = undefined;
	let dataLoaded = false;
	let projectImages = [];

	// This will be parsed from markdown from the serveer.
	let mainTextHtml = undefined;


	export async function preload({ params, query }) {
		dataLoaded = true;
		projectData = await fetchProject(params.slug, this);

		if(projectData) {
			mainTextHtml = marked(projectData.long_description);
			projectImages = projectData.images.map((imageMap) => imageMap.image)
		}
	}


</script>
<script>
	import SlideShow from "../../components/img-slideshow/SlideShow.svelte";
</script>

<style>
	h1.title {
		font-weight: bold;
	}
</style>

<svelte:head>
	<!--  Another check here since you can not put svelte:head in a if block	-->
	{#if projectData !== undefined}
		<title>{projectData.name}</title>
	{/if}}
</svelte:head>

{#if projectData === undefined && dataLoaded}
	<p>Project not found</p>
{:else if projectData && dataLoaded}
	<Container>
		<!--	TODO image slide show	-->
		<!--	TODO add project styling and links at bottom and project size	-->
		<h1 class="title">{projectData.name}</h1>
		<SlideShow images={projectImages} />
		<p>Started project around: {projectData.date}</p>

		{@html mainTextHtml}
	</Container>
{/if}