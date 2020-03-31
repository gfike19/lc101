function makeDownwardStairs(num) {
    let stair = "";
    let line = "";
    for(let i = 0; i < num - 1; i++) {
        line += "#";
        stair += line + "\n";
    }
    stair += line +"#";

    return stair;
}

function makeSpaceLine(numSpaces, numChars) {
    let space = "";
    let line = "";
    

    for(let i = 0; i < numSpaces; i++){
        space += " ";
    }

    for(let j = 0; j < numChars; j++){
        line += "#";
    }

    let spaceLines = space + line + space;
    return spaceLines;
}

function makeIsoscelesTriangle(size) {
    let ioTriangle = "";


		let spaceNum = 0;
		let hashNum = 0;
		let spaceLine ="";
		let i = 0;
		for (i = 0; i < size - 1; i++){
			spaceNum = size - i - 1;
			 hashNum = 2 * i + 1;
			 spaceLine = makeSpaceLine(spaceNum, hashNum);
			 ioTriangle = ioTriangle + spaceLine + "\n"
		}	

		spaceNum = size - i - 1;
		hashNum = 2 * i + 1;
		spaceLine = makeSpaceLine(spaceNum, hashNum);
		ioTriangle = ioTriangle + spaceLine;

return ioTriangle;
		
}

console.log(makeIsoscelesTriangle(9));
