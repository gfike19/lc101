function funPhrase(str) {
    let char = "";

    if(str.length <= 3) {
        char += str.charAt(str.length);
    }

    if(str.length >= 3) {
        char += str.slice(0,3);
    }

    return `We put the ${char} in ${str}`;
}

console.log(funPhrase("ugh"));

function getRectArea(l, w = l) {

    let area = 0;

    if(l = w) {
        area = l *l;
    }
    else {
        area = l * w;
    }

    return area;
}

let area = getRectArea(2, 4);
let str = `The area is ${area}cm^2`;
console.log(str);

area = getRectArea(20);
str = `The area is ${area}cm^2`;
console.log(str);