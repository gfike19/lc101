let pirateOut = function(someInput) {
    if (typeof(someInput) ==  "number") {
        return someInput * 3;
    }
    else if(typeof(someInput) == "string") {
        return "ARRR!";
    }
    else {
        return someInput;
    }
};

let arr = ['Elocution', 21, 'Clean teeth', 100];

let pirateOut2 = arr.map(function(val) {
    
    if (typeof(val) ==  "number") {
        return val * 3;
    }
    else if(typeof(val) == "string") {
        return "ARRR!";
    }
    
});

console.log(pirateOut2);