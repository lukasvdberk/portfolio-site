<script>
	import Img from "../components/common/StandardImage.svelte"
	import AboutMeManager from "../components/about-me-tags/AboutMeManager.svelte"
	import ContactManager from "../components/contact/ContactManager.svelte"
	import ProjectManager from "../components/projects/ProjectManager.svelte"
	import Container from "../components/common/Container.svelte";

	 function calculateAge(birthday) { // birthday is a date
	   let ageDifMs = Date.now() - birthday;
	   let ageDate = new Date(ageDifMs); // miliseconds from epoch
	   return Math.abs(ageDate.getUTCFullYear() - 1970);
	 }

	 // So the age is always up to date
	 const age = calculateAge(new Date(2000, 12, 22));
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
	<!--  Meta tags	-->
	<meta name="title" content="Lukas portfolio">
	<meta name="description" content="Lukas van den Berk a developer his portfolio site">
	<meta property="og:type" content="website">
	<!--  TODO update to lukas.sh	-->
	<meta property="og:url" content="https://lukashisprojects.rocks">
	<meta property="og:title" content="Lukas portfolio">
	<meta property="og:description" content="Lukas van den Berk a developer his portfolio site">
	<meta property="og:image" content="/favicon.png">
	<meta property="twitter:card" content="summary_large_image">
	<!--  TODO update to lukas.sh	-->
	<meta property="twitter:url" content="https://lukashisprojects.rocks">
	<meta property="twitter:title" content="Lukas portfolio">
	<meta property="twitter:description" content="Lukas van den Berk a developer his portfolio site">
	<meta property="twitter:image" content="/favicon.png">
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
			Hi there my name is Lukas van den Berk a {age} year old software engineer from the Netherlands. Currently following a eduction in Software Development at Hogeschool leiden (will be done in 2023). I like to write scripts create websites/apps and work with new technologies in general. Below you will find some projects that I have done (in my freetime) to give you a idea of what I am capable of and what my interests are. But the TLDR version is:
		</p>
		<ul>
			<li>Backend development</li>
			<li>Sys-admin</li>
			<li>Mobile app development</li>
			<li>Front-end development</li>
		</ul>
		<p>
			The source code of this project is available on <a href="https://github.com/lukasvdberk/portfolio-site">github</a>
		</p>

		<h2>Projects</h2>
		<ProjectManager />
	</section>
</Container>

