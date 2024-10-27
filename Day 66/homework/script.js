
function filter(num){
        if (num % 2 == 0){
            console.log(num + " is even")
        } else{
            console.log(num + " is odd")
        }
}
filter(2)

function sum_of_list(list_){
    let ans = 0
    if (list_ == ""){
        console.log("your list is empty")
    } else {
        for (let num of list_) {
            ans += Number(num);
        }
        console.log(ans);
    }
}
sum_of_list([2,3,4,5,6,7,8,9,0,1])

function is_above_20_after_multyplying_it_by_three(list2){
    ans = []
    if (list2 == ""){
        console.log("its empty")
        return;
    } else {
        for (let num of list2) {
            if (num * 3 > 20) {
                ans.push(num * 3);
            }
        }
        console.log(ans);
    }
}
is_above_20_after_multyplying_it_by_three([10,11,12])

function biggest_num(list3){
    if (list3 == ""){
        console.log("It's empty");
        return;
    } else{
        ans = Math.max(...list3)
        console.log(ans)
    }
}
biggest_num([3,6,1,3,6,8,3,4,7,9,10])

function is_it_above_100_when_multyplyied_on_each_other(num1,num2){
    if (num1 * num2 < 100){
        console.log("its below 100")
    } else {
        console.log("its above 100")
    }
}
is_it_above_100_when_multyplyied_on_each_other(2,50)

function is_first_and_last_letter_same(list4){
    if (list4 == "") {
        console.log("its empty");
        return;
    }
    list4 = list4.join("");
    list4 = list4.toLowerCase();
    list4 = list4.split("");
    let firstLetter = list4[0];
    let lastLetter = list4[list4.length -1];
    if (firstLetter === lastLetter) {
        console.log("they are the same:", firstLetter, lastLetter);
    } else {
        console.log("not the same:", firstLetter, lastLetter);
    }
}
is_first_and_last_letter_same(["hello my name is luke"])

// დავალება NUM7 ვერ გავიგე

function is_it_palindrome(word) {
    word = word.split("");
    let reversed = word.reverse().join("");
    if (word === reversed){
        console.log("your word is a palindrome");
    } else{
        console.log("your word is not a palindrome");
    }
}
is_it_palindrome("luka")