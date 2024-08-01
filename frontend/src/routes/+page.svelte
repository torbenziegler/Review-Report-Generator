<script>
	import { Button, Label, Input, Select } from 'flowbite-svelte';
	import { DownloadOutline } from 'flowbite-svelte-icons';

	let selected;
	let packageName = '';
	let countries = [
		{ value: 'us', name: 'English' },
		{ value: 'de', name: 'German' }
	];

	async function getReport() {
		if (packageName) {
			try {
				const response = await fetch(`localhost:5000/`); // await fetch(`localhost:5000/pdf/${packageName}`);
				if (!response.ok) {
					throw new Error('API response was not ok');
				}
				const data = await response.json();
				console.log('Report data:', data);
				// Handle the response data as needed
			} catch (error) {
				console.error('Fetch error:', error);
				// Handle the error as needed
			}
		} else {
			alert('Please enter a valid package name.');
		}
	}
</script>

<div>
	<h1 class="text-xl dark:text-white">Welcome to App Report Generator</h1>
	<p class="dark:text-white">Enter a valid package name to generate a report.</p>
	<div class="mt-8 flex space-x-4">
		<div>
			<Label for="language-select">
				Select a language
				<Select id="language-select" class="mt-2" items={countries} bind:value={selected} />
			</Label>
		</div>
		<div>
			<Label for="package-name-input" class="mb-2 block">App package name</Label>
			<Input id="package-name-input" placeholder="App package name" bind:value={packageName} />
		</div>
		<div>
			<Label for="download-btn" class="mb-2 block">Download now</Label>
			<Button id="download-btn" on:click={getReport}>
				<DownloadOutline class="me-2 h-5 w-5" /> Get Report
			</Button>
		</div>
	</div>
</div>
