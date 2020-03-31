function makeSpaceLine(numSpaces, numChars, char = "#") {
    let space = "";
    let line = "";
    

    for(let i = 0; i < numSpaces; i++){
        space += " ";
    }

    for(let j = 0; j < numChars; j++){
        line += char;
    }

    let spaceLines = space + line + space;
    return spaceLines;
}

function makeIsoscelesTriangle(size, char = "#") {
    let ioTriangle = "";


		let spaceNum = 0;
		let hashNum = 0;
		let spaceLine ="";
		let i = 0;
		for (i = 0; i < size - 1; i++){
			spaceNum = size - i - 1;
			 hashNum = 2 * i + 1;
			 spaceLine = makeSpaceLine(spaceNum, hashNum, char);
			 ioTriangle = ioTriangle + spaceLine + "\n"
		}	

		spaceNum = size - i - 1;
		hashNum = 2 * i + 1;
		spaceLine = makeSpaceLine(spaceNum, hashNum, char);
		ioTriangle = ioTriangle + spaceLine;

return ioTriangle;
		
}

function reverse(str) {
   let lettersArray = str.split('');
   let reversedLettersArray = lettersArray.reverse();
   return reversedLettersArray.join('');
}

function makeDiamond(size, char = "#") {
	let str = makeIsoscelesTriangle(size, char);
	let reverseTriangle = reverse(str);
		return str + "\n" + reverseTriangle;
}

const input = require('readline-sync');
let char = input.question("Enter a character: ");

if (char != '') {
    console.log(makeDiamond(5, char));
}
else {
    console.log(makeDiamond(5));
}