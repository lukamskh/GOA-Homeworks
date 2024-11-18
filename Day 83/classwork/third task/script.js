
function last_amount(){
    const payed = document.getElementById("payed").value;
    const tip = document.getElementById("tip").value;
    if (payed == Math.sign(1) || tip == Math.sign(1)){
        let ans = payed * (tip / 100);
        let ans1 = Number(payed) + Number(ans);
        alert(`${ans}$ is your tip and ${ans1}$ is total amount`);
    } else {
        alert("negative number really?")
    }
}