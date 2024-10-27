let num = [1,2,3,4,5,6,7,8,9]
let num2 = ["helo", "I", "am", "just", "typing"]

// გვეუბნება მონაცემის სიგრძეს
console.log(num.length);

// აქცევს ყველა მონაცემს სტრინგად
console.log(num.toString());

// გვეუბნება რა მონაცემი დგას მოცემულ ადგილზე
console.log(num.at(1));

// აერთიანებს მონაცემებს მოცემული ნიშნით
console.log(num.join(" * "));

// აშორებს ბოლო მონაცემს 
console.log(num2.pop());

// ამატებს მონაცემს ან ბოლოში ან მოცემულ ადგილას
console.log(num.push());

// იღებს პირველ მონაცემს და სხვა ყველას აქცევს დაბალ ასოდ
console.log(num2.shift());

// უმატებს ელემენტს და აბრუნებს როგორც იყო
console.log(num2.unshift("luka"));

// უღებს მოცემულ ინფორმაციას გაფრთხილება გამოიყენეთ pop და push რადგან ეს ფუნქცია ტოვებს ცარიელ ადგილს
console.log(num2.delete);

// აერთიანებს ორ მონაცემს ერთში
let combine = num2.concat(num);

// აკოპირებს ელემენტებს და გადააქვს ის მოცემულ ადგილას
console.log(num2.copyWithin(2,0));

// ქმნის დამატებით მონაცემს მონაცემში
const myArr = [[1,2],[3,4],[5,6]];
const newArr = myArr.flat();

// ამატებს მონაცემებს მოცემულ ადგილას ერთზე მეტი მონაცემის დამატება შეიძლება
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.splice(2, 0, "Lemon", "Kiwi");

// აბრუნებს მონაცემს მანამ სანამ დაემატებოდა
const months = ["Jan", "Feb", "Mar", "Apr"];
const spliced = months.toSpliced(0, 1);

// ყოფს ნაწილებად მოცემულ ადგილას
fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
const citrus = fruits.slice(1);