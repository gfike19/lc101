let superChimpOne = {
    name: "Chad",
    species: "Chimpanzee",
    mass: 9,
    age: 6,
    move: function() {
        return Math.floor(Math.random() * 10);
    }
};

let salamander = {
    name: "Lacey",
    species: "Axolotl Salamander",
    mass: 0.1,
    age: 5,
    move: function() {
        return Math.floor(Math.random() * 10);
    }
};

let anOne = {name:"Brad", species: "Chimpanzee",  mass: 11, age: 6,  move: function() {
    return Math.floor(Math.random() * 10);
}};
let anTwo = {name: "Leroy", species: "Beagle", mass: 14, age:5,  move: function() {
    return Math.floor(Math.random() * 10);
}};
let anThree = {name: "Almina", species: "Tardigrade", mass:0.0000000001, age:1,  move: function() {
    return Math.floor(Math.random() * 10);
}};

let anArr = [superChimpOne, salamander, anOne, anTwo, anThree];

let ids = [];

while (ids.length < 5) {
    let r = Math.ceil(Math.random() * 10);
    if(ids.includes(r) == false) {
        ids.push(r);
    }
}

for(let i = 0; i < anArr.length; i++){
    anArr[i]["id"] = ids[i];
}

function selectRandomEntry (arr){
    let index = Math.floor(Math.random()*arr.length);
    return arr[index];
 }

 let spaceId = [];

while(spaceId.length != 3){
    let rId = selectRandomEntry(ids);
    if(spaceId.includes(rId) == false){
        spaceId.push(rId);
    }
}


 function sendToSpace(crewIds, crewArr){
     let spaceCrewArr = [];

     for(let each of crewArr){
        let crewId = each.id;
        if(crewIds.includes(crewId)){
            spaceCrewArr.push(each);
        }
     }
     return spaceCrewArr;
 }

 console.log(sendToSpace(spaceId, anArr));