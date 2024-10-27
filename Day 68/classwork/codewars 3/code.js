// https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/javascript

function abbrevName(name){
    const [firstName, lastName] = name.split(' ')
    const first = firstName.charAt(0).toUpperCase()
    const second = lastName.charAt(0).toUpperCase()
    return first + '.' + second
}