// https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/javascript

function filter_list(l) {
    let ans = [];
    for (let num of l) {
      if (Number.isInteger(num)) {
        ans.push(num);
      }
    }
    return ans;
  }