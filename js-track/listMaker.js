let arr = [];

for(let i = 0; i <= 9; i++){
    let r = Math.floor(Math.random() * 10);
    arr.push(r);
}
console.log(arr);
console.log(arr.splice(1,1));
console.log(typeof(arr.splice(1,1)));
let test = arr.splice(1,1);
console.log(test);
console.log(typeof(test));
