// https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/javascript

function find_average(array) {
    if (array.length === 0) {
    return 0;
    }
    var result = 0;
    for (i=0; i<array.length; i++) {
      result +=array[i];
    }
    return result/array.length;
  }