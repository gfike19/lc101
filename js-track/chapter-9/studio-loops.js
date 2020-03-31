let protein = ['chicken', 'pork', 'tofu', 'beef', 'fish', 'beans'];
let grain = ['rice', 'pasta', 'corn', 'potato', 'quinoa', 'crackers'];
let veg = ['peas', 'green beans', 'kale', 'edamame', 'broccoli', 'asparagus'];
let bev = ['juice', 'milk', 'water', 'soy milk', 'soda', 'tea'];
let dess = ['apple', 'banana', 'more kale', 'ice cream', 'chocolate', 'kiwi'];

for(let i = 0; i <= 5; i = i + 1){
    console.log(`Meal ${i} is ${protein[i]}, ${grain[i]}, ${veg[i]}, ${bev[i]}, and ${dess[i]}`);
}

let pantry = [protein, grain, veg, bev, dess];
console.log(pantry);

let string = "1234";
let otherString = "5678";
let combine = "";

for(let i = 0; i <= string.length; i++) {
    combine += string.charAt(i);
    combine += otherString.charAt(i);
}

console.log(combine);

const input = require('readline-sync');
let num = 0;

while(num < 1 || num > 6) {
    num = input.question("How many meals to make? ");
}

let meal = [];
for(let i = 0; i < num; i++){
    console.log(`Meal ${i} is ${protein[i]}, ${grain[i]}, ${veg[i]}, ${bev[i]}, and ${dess[i]}`);
    meal.push([protein[i], grain[i], veg[i], bev[i], dess[i]]);
    if (meal[i].includes("kale")){
        console.log("Don't worry, you can have double chocolate tomorrow.");
    }
}

