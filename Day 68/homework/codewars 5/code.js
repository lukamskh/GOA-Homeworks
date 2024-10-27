// https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/javascript

function dnaStrand(dna) {
    let ans = "";
    for (let i = 0; i < dna.length; i++) {
      switch (dna[i]) {
        case "A":
          ans += "T";
          break;
        case "T":
          ans += "A";
          break;
        case "C":
          ans += "G";
          break;
        case "G":
          ans += "C";
          break;
        default:
          throw new Error("Invalid DNA character");
      }
    }
    return ans;
  }