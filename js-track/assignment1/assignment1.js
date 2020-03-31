// part one below
// let name = "";
// let quizQ = 'Given the array [8, "Orbit", "Trajectory", 45], what entry is at index 2 ?';
// let answer = "trajectory";
// let canAnswer = "";

// let input = require('readline-sync');
// name = input.question("What is you name? ")
// canAnswer = input.question(quizQ);

// if(canAnswer.toLowerCase() == answer) {
//     console.log(`${name} you got the question correct!`);
// } else {
//     console.log(`${name} unfortunately that is not correct.`);
// }

// parts 2 and 3 below
let input = require('readline-sync');
let name = input.question("What is your name? ");
let quizQs = [
    ["True or false: 5000 meters = 5 kilometers.", "(5 + 3)/2 * 10 = ? ", 'Given the array [8, "Orbit", "Trajectory", 45], what entry is at index 2? ', "Who was the first American woman in space? ", "What is the minimum crew size for the International Space Station (ISS)? "],
    ["true", "40", "trajectory", "sally ride", "3"]
];

let numQs = quizQs[0].length;
let canAnswerNum = 0;
for (let i = 0; i <numQs; i++) {
    let a = input.question(`${i + 1}) ${quizQs[0][i]}`);
    let actualA = quizQs[1][i];

    if(a.toLowerCase() == actualA) {
        console.log(`${name} you got the question correct!`);
        canAnswerNum += 1;
    } else {
     console.log(`${name} unfortunately that is not correct.`);
    }
}

let score = canAnswerNum / numQs * 100;
console.log(`>>> Overall Grade: ${score}% (${canAnswerNum} of 5 responses correct) <<<`);

if (score < 70) {
    console.log(`>>> Status: FAILED <<<`);
} else {
    console.log(`>>> Status: PASSED <<<`);
}