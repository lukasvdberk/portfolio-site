<style>
	.container {
		position: relative;
		padding-top: 20px;
		height: 100vh;
		margin: auto;
		width: 60%;
		background-color: white;
	}

	@media (max-width: 1450px) {
		main {
			background-color: transparent;
		}
	}

	@media (min-width: 800px) and (max-width: 1250px) {
		.container {
			width: 90%;
			margin: auto;
		}
	}


	@media (max-width: 800px) {
		.container {
			width: 95%;
			margin: auto;
		}
	}
</style>
<main>
	<div class="container">
        <slot></slot>
    </div>
</main>