function makeLine(size){
    let line = "";
    for(let i = 0; i < size; i++){
        line += "#";
    }
    return line;
}

// function makeSquare(size){
//     let sq = "";
//     let line = makeLine(size);
//     let i = 0;

//     while(i != size - 1){
//         sq += line + "\n";
//         i++;
//     }
//     sq += line;
//     return sq;
// }

function makeRectangle(w, h){
    let line = makeLine(w);
    let i = 0;
    let rect = "";
    while(i != h - 1){
        rect += line + "\n"; 
        i += 1;
    }

    rect += line;
    return rect;
}

function makeSquare(size){
    let sq = makeRectangle(size, size);
    return sq;
}

console.log(makeSquare(5));