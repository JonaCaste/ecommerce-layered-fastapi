document.getElementById("update-inventory-form").addEventListener("submit", async function(e) {
    e.preventDefault();
    const payload = {
        idProduct: parseInt(document.getElementById("idProduct").value),
        quantity: parseInt(document.getElementById("quantity").value)
    };

    try {
        console.log(payload)
        const response = await fetch("http://127.0.0.1:8000/api/inventory/update", {  //@todo quemado
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error(await response.text());
        alert("Inventory updated!");
    } catch (err) {
        alert(err.message);
    }
});
