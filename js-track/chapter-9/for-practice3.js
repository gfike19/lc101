let arr = [2, 3, 13, 18, -5, 38, -10, 11, 0, 104];

let evens = [];
let odds = [];

for(let i = 0; i < arr.length; i++){

    let num = arr[i];

    if(num % 2 == 0){
        evens.push(num);
    } else{
        odds.push(num);
    }

}

console.log(evens);
console.log(odds);