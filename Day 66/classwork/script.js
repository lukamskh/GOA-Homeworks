let num = prompt("what is your age: ")

if (num > 17){
    alert("you are adult")
} else{
    alert("you are not an adult")
}

let i = 0
let list_ = []
do{
    i += 1
    list_.push(i)
}while(i < 30)
console.log(list_)

function filter(numberArr){
    evenNumbers = []
    oddNumbers = []
    for (let num in numberArr){
        if (num % 2 == 0){
            evenNumbers.push(num)
        } else {
            oddNumbers.push(num)
        }
    }
    console.log(evenNumbers)
    console.log(oddNumbers)
}
filter(list_)