function initialPrompt () {
    var input = require('readline-sync');
    let num = input.question(`Welcome to the Scrabble score calculator!\n
    Which scoring algorithm would you like to use?\n
    0 - Scrabble: The traditional scoring algorithm.\n
    1 - Simple Score: Each letter is worth 1 point.\n
    2 - Bonus Vowels: Vowels are worth 3 pts, and consonants are 1 pt.\n
    Enter 0, 1, or 2: `);

    return num;
}


function runProgram (scoringAlgorithms) {
    let choice = initialPrompt().toLocaleLowerCase();
    var input = require('readline-sync');
    let score = 0;

if(choice != 0 || choice != 1 || choice != 2){
    while(choice != 1 || choice != 2 || choice != 0){
        choice = Number(input.question("\n Invalid input. Please enter enter 0, 1, or 2 to select an algorith. Type in 'stop' to exit: "));
    }
}

if(choice == 0 || choice == 1|| choice ==2){
    while(choice != "stop"){
        let word = String(input.question("\nEnter a word to scramble: "));
        let scoreName = "";
        score = scoringAlgorithms[choice].scoreFunction(word);
        scoreName = scoringAlgorithms[choice].name;
        console.log(`\nScore of ${word} using ${scoreName} is ${score}\n`);
        choice = initialPrompt().toLocaleLowerCase();
    }
}
    
}

function transform(obj){
    
    let keyArr = Object.keys(obj);
    let newObj = {};

    for(let each of keyArr){
        let temp = obj[each];
        for(let char of temp){
            newObj[String(char).toLowerCase()] = Number(each);
        }
    }
    newObj[" "] = 0;
    return newObj;
}

const oldScoreKey = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
 };

 let newScoreKey = transform(oldScoreKey); 
//  Create your scoringAlgorithms array here:


let scoreObj1 = {
    name: "Scrabble",
    description: "The traditional scoring algorithm.",
    scoreFunction: function (word, newScoreKey) {
        let text = String(word).toLocaleLowerCase();
        let counter = 0;
        for(let i = 0; i < text.length; i++){
            let char = text.charAt(i);
            counter += newScoreKey[char];
        }
        return counter;
    }
};

let scoreObj2 = {
    name: "Simple Score",
    description: "Each letter is worth 1 point.",
    scoreFunction: function(word) {
        let counter = 0;
     for(let i = 0; i < word.length; i++){
         counter ++;
     }
     return counter;
    }
};

let scoreObj3 = {
    name: "Bonus Vowels",
    description: "Vowels are 3 pts, consonants are 1 pt.",
    scoreFunction: function(word) {
        let counter = 0;
        let vowels = ["a","e","i","o","u"];
    
       for(let i = 0; i < word.length; i++){
            let char = word.charAt(i).toLowerCase();
    
            if(vowels.includes(char)){
                counter += 3;
            }
            else {
                counter ++;
            }
        }
    
        return counter;
    }
};

let scoringAlgorithms = [scoreObj1, scoreObj2, scoreObj3];

runProgram(scoringAlgorithms);