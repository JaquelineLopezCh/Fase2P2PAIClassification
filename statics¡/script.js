async function predictInvoice() {
    const text = document.getElementById('invoiceText').value;
    const result = document.getElementById('result');
    result.textContent = 'Procesando...';

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        if (!response.ok) {
            result.textContent = `Error: ${data.error}`;
            return;
        }

        result.textContent = `Clasificación: ${data.prediction}`;
    } catch (error) {
        result.textContent = `Error de conexión: ${error}`;
    }
}
