// https://www.codewars.com/kata/5556282156230d0e5e000089/train/javascript

function DNAtoRNA(dna) {
    let res = "";
    
    for(let i = 0; i < dna.length; i++){
      if(dna[i] === "T"){
        res += "U";
      } else {
        res += dna[i]; 
      };
    }
    return res;
  }