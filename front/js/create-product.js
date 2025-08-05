document.getElementById("create-product-form").addEventListener("submit", async function(e) {
    e.preventDefault();
    const payload = {
        name: document.getElementById("name").value,
        price: parseFloat(document.getElementById("price").value),
        description: document.getElementById("description").value
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/api/products", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error(await response.text());
        alert("Product created!");
    } catch (err) {
        alert(err.message);
    }
});
