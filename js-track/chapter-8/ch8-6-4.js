let str1 = "water bottles, meal packs, snacks, chocolate";
let str2 = "space suits, jet packs, tool belts, thermal detonators";
let str3 = "parrots, cats, moose, alien eggs";
let str4 = "blankets, pillows, eyepatches, alarm clocks";

let cabA = str1.split(", ");
let cabB = str2.split(", ");
let cabC = str3.split(", ");
let cabD = str4.split(", ");

let cargoHold = [];
cargoHold.push(cabA, cabB, cabC, cabD);

console.log(cargoHold);

const input = require('readline-sync');
let cabNum = input.question("Enter a cabinet number (0-3): ");
if(cabNum >= 0 && cabNum <= 3){
    console.log(`The contents of cabinet number ${cabNum} are as follows: ${cargoHold[cabNum]}`);
    
    // bonus bonus below
    let currCab = cargoHold[cabNum];
    let searchItem = input.question("Enter the name of an item to find: ");

    if(currCab.includes(searchItem)){
        console.log(`Cabinet ${cabNum} does contain ${searchItem}`);
    } else {
        console.log(`Cabinet ${cabNum} does not contain ${searchItem}`);
    }
    // bonus bonus above
} else{
    console.log("That is an invalid number");
}


