function info() {
    let cookies = document.getElementById("cookies");
    let email = document.getElementById("email").value;
    let name = document.getElementById("name").value;
    let password = document.getElementById("password").value;
    let gender = document.getElementById("gender").value;
    if (!cookies.checked) {
        alert("don't you want cookies?");
        return;
    }
    if (email === "" || name === "" || password === "") {
        alert("enter all the info");
        return;
    }
    if (password.length < 8) {
        alert("password is not long enough");
        return;
    }
    console.log(email + " " + name + " " + password + " " + gender);
}