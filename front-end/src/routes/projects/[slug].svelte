<script>
	import {fetchProject} from '../../components/projects/projects';
	import Container from "../../components/common/Container.svelte";
	import SlideShow from "../../components/img-slideshow/SlideShow.svelte";
	import {stores} from "@sapper/app";
	import marked from 'marked';
	import {onMount} from "svelte";
	import Tag from "../../components/common/Tag.svelte";

	const {page} = stores();
	const {slug} = $page.params;


	let projectData = undefined;
	let dataLoaded = false;
	let projectImages = [];

	// This will be parsed from markdown from the serveer.
	let mainTextHtml = undefined;

	onMount(async () => {
		projectData = await fetchProject(slug)
		dataLoaded = true;

		if (projectData) {
			mainTextHtml = marked(projectData.long_description);
			projectImages = projectData.images.map((imageMap) => imageMap.image)
		}
	})

</script>

<style>
	h1.title {
		font-weight: bold;
	}
	div.tag {
        display: inline-block;
        width: 150px;
		margin-right: 5px;
    }
</style>

<svelte:head>
	<!--  Another check here since you can not put svelte:head in a if block	-->
	{#if projectData !== undefined}
		<title>{projectData.name}</title>
	{/if}
</svelte:head>

{#if projectData === undefined && dataLoaded}
	<p>Project not found</p>
{:else if projectData && dataLoaded}
	<Container>
		<h1 class="title">{projectData.name}</h1>
		{#each projectData.tags as tag}
			<div class="tag">
				<Tag timing="0" txt="{tag.name}" icon="{tag.icon}" />
			</div>
		{/each}
		<SlideShow images={projectImages} />
		<a href="{projectData.link}">Site link</a>
		<br>
		<a href="{projectData.github_link}">Github link</a>
		<p>Started project around: {projectData.date}</p>


		{@html mainTextHtml}
	</Container>
{/if}