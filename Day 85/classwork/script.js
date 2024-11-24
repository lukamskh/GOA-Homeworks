function func1(event) {
    alert("div1");
    if (document.getElementById("check").checked) {
      event.stopPropagation();
    }
  }
  
  function func2() {
    alert("div2");
  }