function greet(name = "Guest"){
    alert("hello " + name)
}
greet()

function sum_of_two(num1, num2 = 0){
    alert(num1 + num2)
}
sum_of_two(1,3)

function convert_temperature(temperature,scale = "C"){
    if (scale == "F"){
        let ans = (5/9 * (temperature-32))
        alert(ans)
        console.log(ans)
    } else {
        ans = ((temperature * 9/5) + 32)
        alert(ans)
        console.log(ans)
    }
}
convert_temperature(5,"F")

function add_to_shopping_list(item,quantity = 1){
    alert("amount: "+ quantity + " of " + item + "'s")
}
add_to_shopping_list("bag",3)

function power(num1,powerBy = 2){
    alert(num1 ** powerBy)
}
power(2,3)

function create_message(text = "hello",name){
    alert(text + " "+ name)
}
create_message("welcome","luka")

function apply_discount(price,discount = 10){
    let discount_ = (price * discount/100)
    alert(price - discount_ + "$")
}
apply_discount(100,20)

function introduce(name,age = "unknown",country = "unknown"){
    alert("hello " + name + " your age is: " + age + " and you are from: " + country)
}
introduce("luka",14)

function calculate_price(price,tax = 5){
    let tax_ = (price * tax/100)
    alert(price + tax_ + "$")
}
calculate_price(100,10)

function find_max(num1,num2,num3){
    if (num1 > num2 && num1 > num3){
        alert(num1)
    } else if (num2 > num1 && num2 > num3){
        alert(num2)
    } else{
        alert(num3)
    }
}
find_max(1,2,3)

function pass_or_fail(score){
    if (score > 50){
        alert("pass")
    } else{
        alert("fail")
    }
}
pass_or_fail(51)

function sum_of_numbers(numbers){
    ans = 0
    for (let num in numbers){
        ans += numbers[num]
    }
    alert(ans)
}
sum_of_numbers([1,2,3,4,5,6,7,8,9])

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
// 100