<script>
	import Img from "../components/common/StandardImage.svelte"
	import AboutMeManager from "../components/about-me-tags/AboutMeManager.svelte"
	import ContactManager from "../components/contact/ContactManager.svelte"
	import ProjectManager from "../components/projects/ProjectManager.svelte"
	import Container from "../components/common/Container.svelte";
	import Card from "../components/common/Card.svelte";

	function calculateAge(birthday) { // birthday is a date
		let ageDifMs = Date.now() - birthday;
		let ageDate = new Date(ageDifMs); // miliseconds from epoch
		return Math.abs(ageDate.getUTCFullYear() - 1970);
	}

	// So the age is always up to date
	const age = calculateAge(new Date(2000, 12, 22));
</script>

<style>
	section {
		text-align: center;
	}

	.img {
		display: block;
		position: relative;
		width: 30%;
		float: left;
	}

	.group {
		display: block;
		position: relative;
		width: 100%;
	}

	.img, .group {
		height: 550px;
	}


	.spacing {
		padding: 2%;
		display: flex;
        justify-content: center;
        align-items: center;
	}

	.about {
		display: block;
		position: relative;
		float: right;
		width: 65%;
	}

	.end{
		position: absolute;
		right:    0;
		bottom:   0;
	}

	.projects {
		display: block;
		width: 100%;
		margin-top: 5%;
	}

	.profile-img-container {
		display: block;
	}

	p, h2 {
		padding: 1%;
	}

	.profile-img-container {
		padding: 2.5%;
	}

	ul, li, p{
		text-align: left;
	}

	@media (min-width: 800px) and (max-width: 1450px) {
		.img {
			width: 40%;
		}
		.about {
			width: 55%;
		}
	}

	.profile-img {
		display: block;
	}


	@media (max-width: 800px) {
		.group {
			height: auto;
		}

		.profile-img {
			display: none;
		}

		.img {
			height: auto;
		}

		.group, .projects, .about, .img {
			display: block;
			position: relative;
			width: 100%;
			float: none;
			margin-top: 5%;
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
	<section class="group">
		<section class="img">
			<Card>
				<div class="profile-img-container">
					<div class="profile-img">
						<Img src="favicon.png" alt="my-head" />
					</div>
					<ContactManager />
				</div>
			</Card>
		</section>
		<section class="about">
			<Card>
				<h2>Hello, I am Lukas van den Berk</h2>
				<h2>I am a developer but also a...</h2>
				<div class="spacing">
					<AboutMeManager />
				</div>
			</Card>
		</section>
		<section class="about end">
			<Card>
				<h2>About me</h2>
				<p>
					Hi there my name is Lukas van den Berk a {age} year old software engineer from the Netherlands. Currently following a eduction in Software Development at Hogeschool leiden (will be done in 2023). I like to write scripts create websites/apps and work with new technologies in general. Below you will find some projects that I have done (in my freetime) to give you a idea of what I am capable of and what my interests are. <br>For exact skills check my Linkedin in on the left.
				</p>
				<p>
					The source code of this project is available on <a href="https://github.com/lukasvdberk/portfolio-site">github</a>
				</p>
			</Card>
		</section>
	</section>
	<section class="group">
		<section class="projects">
			<h2>Projects</h2>
			<ProjectManager />
		</section>
	</section>
</Container>

