function genPassword() {
    const length = document.getElementById("length").value;
    const upper = document.getElementById("uppercase").checked;
    // const lower = document.getElementById("lowercase").checked;
    const numbers = document.getElementById("numbers").checked;
    const symbols = document.getElementById("symbols").checked;

    let chars = "abcdefghijklmnopqrstuvwxyz";
    if (upper) chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    // if (lower) chars += "abcdefghijklmnopqrstuvwxyz";
    if (numbers) chars += "0123456789";
    if (symbols) chars += "!@#$%^&*()_+[]{}|;:',.<>?/";

    let password = "";

    for (let i=0; i<length; i++){
        password += chars.charAt(Math.floor(Math.random() * chars.length))
    }

    document.getElementById("password").textContent = password;
    document.getElementById("copy-btn").classList.remove("hidden");
}

function copyPassword() {
    const password = document.getElementById("password").textContent.trim();

    if (password.length === 0) return;

    navigator.clipboard.writeText(password).then(() => {
        const status = document.getElementById("copy-status");
        status.textContent = "Password copied!";
        setTimeout(() => status.textContent = "", 2000);
    }).catch(err => {
        console.error("Copy failed", err);
    });
}

