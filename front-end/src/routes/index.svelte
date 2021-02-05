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
		width: calc(30% + 20px);
		float: left;
	}

	.spacing {
		padding: 2%;
		display: flex;
        justify-content: center;
        align-items: center;
	}

	.about {
		position: relative;
		width: 65%;
		float: right;
	}

	.header-height, .img, .about {
		height: 45vh;
	}

	.projects {
		display: block;
		width: 100%;
		padding-top: 20% !important;
	}

	p, h2 {
		padding: 1%;
	}

	.projects > h2 {
		margin-top: 25vh;
	}

	.profile-img {
		height: 60%;
	}

	@media (max-width: 800px) {
		.profile-img {
			display: none;
		}

		.projects, .about, .img {
			display: block;
			position: relative;
			width: 100%;
			float: none;
			margin-top: 5%;
		}

		.header-height {
			height: auto;
		}
	}
</style>

<svelte:head>
	<title>Lukas portfolio</title>
	<meta name="title" content="Lukas portfolio">
	<meta name="description" content="Lukas van den Berk a developer his portfolio site">
	<meta property="og:type" content="website">
	<meta property="og:url" content="https://lukas.sh">
	<meta property="og:title" content="Lukas portfolio">
	<meta property="og:description" content="Lukas van den Berk a developer his portfolio site">
	<meta property="og:image" content="/favicon.png">
	<meta property="twitter:card" content="summary_large_image">
	<meta property="twitter:url" content="https://lukas.sh">
	<meta property="twitter:title" content="Lukas portfolio">
	<meta property="twitter:description" content="Lukas van den Berk a developer his portfolio site">
	<meta property="twitter:image" content="/favicon.png">
</svelte:head>

<Container>
	<section class="img">
		<Card>
			<div class="header-height">
				<div class="profile-img">
					<Img src="favicon.png" alt="my-head" />
				</div>
				<ContactManager />
			</div>
		</Card>
	</section>
	<section class="about">
		<Card>
			<div class="header-height">
				<h2>Hello, I am Lukas van den Berk</h2>
				<h2>And I am a:</h2>
				<div class="spacing">
					<AboutMeManager />
				</div>
				<h2>About me</h2>
				<p>
					Hi there my name is Lukas van den Berk a {age} year old software engineer from the Netherlands.
					I Am currently following a eduction in Software Development at Hogeschool Leiden (will be done in 2023).
					Below you will find some projects that I have done (in my freetime) to give you a idea of what I am capable of and what my interests are.
					<br>For exact skills check my Linkedin in on the left.
				</p>
				<p>
					The source code of this project is available on <a href="https://github.com/lukasvdberk/portfolio-site">github</a>
				</p>
			</div>
		</Card>
	</section>
	<section class="projects">
		<h2>Projects</h2>
		<ProjectManager />
	</section>
</Container>

