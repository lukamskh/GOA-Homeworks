function test() {
    let cookies = document.getElementById("cookies");
    let email = document.getElementById("email").value;
    let name = document.getElementById("name").value;
    let password = document.getElementById("password").value;
    if (!cookies.checked) {
        alert("Don't you want cookies?");
        return;
    }
    if (email === "" || name === "" || password === "") {
        alert("Please enter all the information.");
        return;
    }

    // Check password length
    if (password.length < 8) {
        alert("Password must be at least 8 characters long");
        return;
    }
    console.log("email: " + email);
    console.log("name: " + name);
    console.log("password: " + password);
}