const form = document.querySelector("form");
const tbody = document.querySelector("tbody");

form.addEventListener("submit", function(e) {
    e.preventDefault();

    const firstnm = form.firstname.value;
    const email = form.email.value;
    const password = form.password.value;

    const info = [firstnm, email, password];
    const tr = document.createElement("tr");

    for(let i = 0; i < info.length; i++){
        const td = document.createElement("td");
        td.textContent = info[i];
        tr.appendChild(td);
    }
    form.firstnm = "";
    form.email = "";
    form.password = "";

    tbody.appendChild("tr");
})