// https://www.codewars.com/kata/546e2562b03326a88e000020/train/javascript

function squareDigits(num) {
    let result = ""
    let numStr = num.toString()
    for (let i = 0; i < numStr.length; i++) {
      let digit = Number(numStr[i])
      if (!isNaN(digit)) {
        let squared = digit * digit
        result += squared
      }
    }
    return parseInt(result)
  }
  