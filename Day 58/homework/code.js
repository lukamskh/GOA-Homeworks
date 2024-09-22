const car = {
    brand: "BMW",
    model: "M3 GTR GT E46",
    // 2002 incorect
    year: 2002,
}

console.log(car.brand)
console.log(car.year)

car.color = "white"

car.year = 2001

delete car.model

car.owner = "me I want to have it"
car.owne_age = "over 18"

console.log(car)

car.model = "M3 GTR GT E46"

console.log(car)