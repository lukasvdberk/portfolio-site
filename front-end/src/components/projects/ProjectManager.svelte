<script>
	import ProjectCardList from "./ProjectsCardList.svelte"
    import {fetchProjects, getSize} from "./projects.js"
	import {onMount} from "svelte";

	const projectSizeOptions = getSize()
	let projects = undefined
	let projectFilterSize = "ALL";

	onMount(async () => {
		projects = await fetchProjects()
	})


	function setSize(newSize) {
		if(projects) {
			// Fetch new projects by size
			fetchProjects(newSize)
					.then((newProjects) => {projects=newProjects})
					.catch((err) => console.log(err))
		}
	}

	$: setSize(projectFilterSize)
</script>

{#if projects !== undefined}
	<form on:submit|preventDefault={setSize}>
		<label>
			Filter by project size:
			<select bind:value={projectFilterSize}>
				{#each projectSizeOptions as optionSize}
					<option value={optionSize.value}>{optionSize.name}</option>
				{/each}
			</select>
		</label>
	</form>
	<ProjectCardList {projects} />
{:else}
    <p>Please stand by, projects loading......</p>
{/if}