<script>
    let file;
    let prediction = null;
    let loading = false;
    let error = null;
  
    async function handleSubmit() {
      loading = true;
      error = null;
      const formData = new FormData();
      formData.append('file', file);
  
      try {
        const response = await fetch('http://localhost:5000/predict', {
          method: 'POST',
          body: formData
        });
        const data = await response.json();
        if (response.ok) {
          prediction = data.prediction;
        } else {
          error = data.error || 'An error occurred';
        }
      } catch (err) {
        error = 'Failed to connect to the server';
      } finally {
        loading = false;
      }
    }
  </script>
  
  <div class="mt-8">
    <h2 class="text-xl font-semibold mb-4">Upload CSV for Price Prediction</h2>
    <form on:submit|preventDefault={handleSubmit} class="space-y-4">
      <div>
        <label for="file" class="block mb-2">Select CSV file:</label>
        <input type="file" id="file" accept=".csv" bind:files={file} required class="border p-2">
      </div>
      <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded" disabled={loading}>
        {loading ? 'Predicting...' : 'Predict'}
      </button>
    </form>
  
    {#if prediction !== null}
      <div class="mt-4 p-4 bg-green-100 rounded">
        <p>Predicted Price: ${prediction.toFixed(2)}</p>
      </div>
    {/if}
  
    {#if error}
      <div class="mt-4 p-4 bg-red-100 rounded">
        <p>{error}</p>
      </div>
    {/if}
  </div>