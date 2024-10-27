// https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/javascript

function getCount(str) {
    let count = 0;
    
    for(let i = 0; i < str.length; i++){
      const char = str[i];
      
      if(char === "a" || char === "e" || char == "i" || char == "o" || char == "u"){
        count += 1
      }
    }
    return count;
  }