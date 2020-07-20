<script>
	import Img from "../components/standard/StandardImage.svelte"
	import AboutMeManager from "../components/about-me-tags/AboutMeManager.svelte"
	import ContactManager from "../components/contact/ContactManager.svelte"
	import ProjectManager from "../components/projects/ProjectManager.svelte"
	import {onMount} from "svelte";
	import Container from "../components/common/Container.svelte";

	let projects = undefined

	// TODO refactor to separate file.
	onMount(async () => {
		// Fetching the projects
		const res = await fetch(
				'/api/projects', {
					headers: {
						'Content-Type': 'application/json'
					},
					credentials: 'same-origin'
				}
		);
		projects = await res.json();
	})

</script>

<style>
	div.img {
		width: 25%;
		margin: auto;
		float: left;
	}

	article {
		text-align: center;
		display: inline-block;
		vertical-align: center;
		position: relative;
		padding: 2%;
	}

	section {
		text-align: center;
	}

	.spacing {
		padding: 2%;
	}

	.about {
		display: block;
		margin-top: 80px;
	}

	a {
		color: darkblue;
		text-decoration: none;
	}

	@media (max-width: 1450px) {
		main {
			background-color: transparent;
		}
	}

	@media (min-width: 800px) and (max-width: 1250px) {
		div.img {
			width: 30%;
			margin: auto;
		}

		article {
			width: 55%;
			margin: auto;
		}
	}


	@media (max-width: 800px) {
		div.img {
			height: 40%;
			width: 80%;
			margin: auto;
			float: none;
		}
	}
</style>

<svelte:head>
	<title>Lukas portfolio</title>
</svelte:head>
<Container>
	<section>
		<div class="img">
			<Img src="lukas.jpg" alt="my-head" />
		</div>
		<article>
			<h2>Hello there, I am Lukas van den Berk</h2>
			<h2>I am a developer but also a........</h2>
			<div class="spacing">
				<AboutMeManager />
			</div>
			<div class="spacing">
				<ContactManager />
			</div>
		</article>
	</section>
	<section class="about">
		<h2>About me</h2>
		<p>
			"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
		</p>
		<h2>Projects</h2>
		<a href="/api/projects">The endpoint for the projects</a>
		<ProjectManager />
	</section>
</Container>

