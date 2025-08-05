
const grid = document.getElementById("products-grid");

fetch("http://127.0.0.1:8000/api/products/")    //@todo quemado
    .then(res => {
        if (!res.ok) throw new Error("Failed to fetch products");
        return res.json();
    })
    .then(products => {
        grid.innerHTML = products.map(product => `
            <div class="card">
                <img src="../book_image.jpg" alt="Product Image">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <strong>${product.price}$</strong>
            </div>
        `).join("");
    })
    .catch(err => {
        alert(err.message);
    });
