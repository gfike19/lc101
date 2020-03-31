const input = require('readline-sync');
let word = input.question("Enter a word: ");
let lettersToMove = word.slice(0,3);
let wordLength = word.length;
let newBegin = word.slice(3, wordLength + 1);
let newWord = newBegin + lettersToMove;
console.log(`The word ${word} is ${newWord} in pig latin`);

let word2 = input.question("Enter another word: ");
let moveAmt = input.question("How many letters to move? ");
let word2Length = word2.length;
let shiftLetters = word2.slice(0, moveAmt);
let newBegin2 = word.slice(moveAmt, word2Length + 1);
let newWord2 = newBegin2 + shiftLetters;
console.log(`The word ${word2} is ${newWord2} in pig latin`);

let word3 = input.question("Enter another word: ");
let moveAmt2 = input.question("How many letters to move? ");

if (moveAmt2 > 3) {
    moveAmt2 = 3;
}

let word3Length = word3.length;
let shiftLetters2 = word3.slice(0, moveAmt2);
let newBegin3 = word.slice(moveAmt2, word3Length + 1);
let newWord3 = newBegin3 + shiftLetters2;

if(moveAmt2 == 3){
    console.log("Shift amount was too high. Shift amount set to 3");
}
console.log(`The word ${word3} is ${newWord3} in pig latin`);