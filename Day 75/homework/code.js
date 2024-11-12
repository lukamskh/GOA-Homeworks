const form = document.querySelector("form");
const ul = document.querySelector("ul");

form.addEventListener("submit", function(e) {
    e.preventDefault();
    
    const firstnm = form.name.value;
    const li = document.createElement("li");
    li.textContent = firstnm;
    ul.appendChild(li);

    form.name.value = "";
});