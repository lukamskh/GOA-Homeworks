// https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/javascript

function reverseWords(str) {
    const wordsArray = str.split(/( )/)
    for (let i = 0; i < wordsArray.length; i++) {
      if (wordsArray[i] !== ' ') {
        wordsArray[i] = wordsArray[i].split('').reverse().join('')
      }
    }
    return wordsArray.join('');
  }