
document.getElementById("purchase-form").addEventListener("submit", async function(e) {
    e.preventDefault();
    const payload = {
        idProduct: parseInt(document.getElementById("idProduct").value),
        idUser: parseInt(document.getElementById("idUser").value),
        quantity: parseInt(document.getElementById("quantity").value)
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/api/purchase/", { //@todo quemado
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error(await response.text());
        alert("Purchase successful!");
    } catch (err) {
        alert(err.message);
    }
});
