let str = 'LaunchCode';
let arr = [1, 5, 'LC101', 'blue', 42];

let strLen = str.length;

for(let i = strLen; i >= 0; i-=1){
    console.log(str.slice(i, i + 1));
}