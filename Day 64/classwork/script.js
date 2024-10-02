
function filter(numberArr){
    evenNumbers = []
    oddNumbers = []
    for (let num in numberArr){
        if (num % 2 == 0){
            evenNumbers += num
        } else {
            oddNumbers += num
        }
    }
    console.log(evenNumbers)
    console.log(oddNumbers)
}

filter([1,2,3,4,5,6,7,8,9,10])