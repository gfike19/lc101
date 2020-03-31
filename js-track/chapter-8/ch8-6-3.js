const input = require('readline-sync');
let text = input.question("Enter a some words with commas, semicolons and/or spaces: ");
let arr = [];
let newText = "";


if (text.includes(",")){
     arr = text.split(",");
    arr.reverse();
     newText = arr.join(",");
}

else if(text.includes(";")){
     arr = text.split(";");
    arr.sort();
     newText = arr.join(",");
}

else if(text.includes(" ")){
     arr = text.split(" ");
    arr.sort();
    arr.reverse();
     newText = arr.join(" ");
}

else if(text.includes(", ")){
    arr = text.split(", ");
    arr.reverse();
     newText = arr.join(",");
}

console.log(newText);