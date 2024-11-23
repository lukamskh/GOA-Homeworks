function changeColor() {
    const button = document.getElementById('btn1');
    button.classList.toggle('active');
    if (button.classList.contains('active')) {
        button.style.opacity = 0.5;
    } else {
        button.style.opacity = 1;
    }
}