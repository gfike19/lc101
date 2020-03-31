let element1 = ['hydrogen', 'H', 1.008];
let element2 = ['helium', 'He', 4.003];
let element26 = ['iron', 'Fe', 55.85];

let table = [];
table.push(element1, element2, element26);

console.log(table);
console.log(table[1]);
console.log(typeof(table[1]));
console.log(table[1][1]);
console.log(typeof(table[1][1]));
console.log("Element 1 mass:", table[0][2]);
console.log("Element 2 name:", table[1][0]);
console.log("Element 26 symbol", table[2][1]);

let columnNames = ["House Name", "Animal", "Motto"];
let s = ["Stark", "Direwolf", "Winter is Coming"];
let t = ["Targaryen", "Dragon", "Fire and Blood"];

table2.push(columnNames, s, t);

console.log(table2[0][1], table[1][1]);