<script>
	import NavIcon from "./NavIcon.svelte"
</script>

<style>
	* {
		color: white;
		background-color: #001021;
	}

	nav {
		position: fixed;
		z-index: 2;
		height: 60px;
		width: 100vw;
	}

	div {
		position: relative;
		height: 100%;
		width: 100%;
	}
</style>

<nav>
	<div>
		<NavIcon />
	</div>
</nav>
