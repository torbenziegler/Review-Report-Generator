<script>
	import { Button, Label, Input, Select } from 'flowbite-svelte';
	import { DownloadOutline } from 'flowbite-svelte-icons';

	let selected = 'us';
	let packageName = '';
	let countries = [
		{ value: 'us', name: 'English' },
		{ value: 'de', name: 'German' }
	];

	async function getReport() {
		if (packageName) {
			try {
				const response = await fetch(`http://localhost:5000/pdf/${packageName}`, {
					headers: {
						'Content-Language': selected
					}
				});
				if (!response.ok) {
					throw new Error('API response was not ok');
				}
				const blob = await response.blob();
				const url = window.URL.createObjectURL(blob);
				const a = document.createElement('a');
				a.href = url;
				a.download = `${packageName}-report.pdf`;
				document.body.appendChild(a);
				a.click();
				a.remove();
				window.URL.revokeObjectURL(url);
			} catch (error) {
				console.error('Fetch error:', error);
				alert('An error occurred while fetching the report. Please try again later.');
			}
		} else {
			alert('Please enter a valid package name.');
		}
	}
</script>

<div>
	<h1 class="text-xl dark:text-white">Welcome to App Report Generator</h1>
	<p class="dark:text-white">Enter a valid package name to generate a report.</p>
	<form class="mt-8 flex space-x-4">
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
			<Button id="download-btn" on:click={getReport} type="submit">
				<DownloadOutline class="me-2 h-5 w-5" /> Get Report
			</Button>
		</div>
	</form>
</div>
