let string = 1234;

function reverseCharacters(string) {
    if(typeof(string) == "number"){
         num = "" + string;
         reversedNumber = num.split("").reverse().join("");
         reversedNumber = Number(reversedNumber);
        return reversedNumber;
    }
    if(typeof(string) == "string") {
         reversedString = string.split("").reverse().join("");
        return reversedString;
    }
    
}

function completeReversal(arr){
    let newArr = [];

    for(let i = 0; i < arr.length; i++){
        let newString = reverseCharacters(arr[i]);
        newArr.unshift(newString);
    }

    return newArr;
}

// let arr1 = ['apple', 'potato', 'Capitalized Words'];
// let arr2 = [123, 8897, 42, 1138, 8675309];
// let arr3 = ['hello', 'world', 123, 'orange'];

// console.log(completeReversal(arr1));
// console.log(completeReversal(arr2));
// console.log(completeReversal(arr3));

console.log(typeof(reverseCharacters("fuck you")));