document.getElementById("register-form").addEventListener("submit", async function(e) {
    e.preventDefault();
    const payload = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value,
        email: document.getElementById("email").value,
        direction: document.getElementById("direction").value,
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/api/users/register", {    //@todo quemado
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error(await response.text());
        alert("Registration successful!");
    } catch (err) {
        alert(err.message);
    }
});
