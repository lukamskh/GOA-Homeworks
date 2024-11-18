const timer = setTimeout(hello, 3000);
function hello() {
    const paragraphs = document.getElementsByTagName("p");
    paragraphs[0].textContent = "hi";
}
const time = setInterval(time1, 1000);
function time1() {
    let d = new Date();
    let n = d.toLocaleTimeString();
    const timers = document.getElementById("timers");
    timers.textContent = n;
}