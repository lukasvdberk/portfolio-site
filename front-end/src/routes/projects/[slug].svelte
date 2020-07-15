<script context="module">
	import {fetchProject} from '../../components/projects/projects';
	import marked from 'marked';
	let projectData = undefined;
	let projectLoaded = false;

	// This will be parsed from markdown from the serveer.
	let mainTextHtml = undefined;


	export async function preload({ params, query }) {
		projectLoaded = true;
		projectData = await fetchProject(params.slug, this);
		mainTextHtml = marked(projectData.long_description);
	}


</script>

{#if projectData === undefined && projectLoaded}
	<p>Project not found</p>
{:else if projectData}
	<h1>{projectData.name}</h1>
	{@html mainTextHtml}
{/if}