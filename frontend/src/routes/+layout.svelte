<script>
	import '../app.css';
	import { DarkMode } from 'flowbite-svelte';
</script>

<div class="flex h-screen flex-col items-center justify-center">
	<DarkMode class="text-primary-500 dark:text-primary-600 m-8 border dark:border-gray-800" />

	<div class="main flex h-full w-full items-center justify-center">
		<slot></slot>
	</div>
</div>
