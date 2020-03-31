// Code your orbitCircumference function here:
function orbitCircumference(radius){
    let num = Number((2 * Math.PI * radius).toFixed());
    return num;
}

// Code your missionDuration function here:
function missionDuration(orbitsNum, orbitRad = 2000, orbitSpeed = 28000){
    let totalCircum = Number(orbitCircumference(orbitRad) * orbitsNum);
    let dur = totalCircum/ orbitSpeed;
    dur = Number(dur.toFixed(2));
    console.log(`The mission will travel ${totalCircum} km around the planet, and it will take ${dur} hours to complete.`);
    return dur;
}

// Copy/paste your selectRandomEntry function here:
function selectRandomEntry (arr){
    let index = Math.floor(Math.random()*arr.length);
    return arr[index];
 }

// Code your oxygenExpended function here:

// unrefactored below
// function oxygenExpended(canidate){
//   let dur = missionDuration(3, 6371);
//   let oxyUsed = Number(canidate.o2Used(dur).toFixed(3));
//   console.log(`${canidate.name} will perform the spacewalk, which will last ${dur} hours and require ${oxyUsed} kg of oxygen.`)
// }

function oxygenExpended(canidate, radius, speed){
  let dur = missionDuration(3, radius, speed);
  let oxyUsed = Number(canidate.o2Used(dur).toFixed(3));
  console.log(`${canidate.name} will perform the spacewalk, which will last ${dur} hours and require ${oxyUsed} kg of oxygen.`)
}

function conserveO2(crewArray){
  let can = crewArray[0];
  for(let i = 1; i < crewArray.length; i++){
    let o = can.o2Used(1);
    
    if(crewArray[i].o2Used(1) < o){
      can = crewArray[i];
    }
  }

  return can;
}


// Candidate data & crew array.
let candidateA = {
  'name':'Gordon Shumway',
  'species':'alf',
  'mass':90,
  'o2Used':function(hrs){return 0.035*hrs},
  'astronautID':414
};
let candidateB = {
  'name':'Lassie',
  'species':'dog',
  'mass':19.1,
  'o2Used':function(hrs){return 0.030*hrs},
  'astronautID':503
};
let candidateC = {
  'name':'Jonsey',
  'species':'cat',
  'mass':3.6,
  'o2Used':function(hrs){return 0.022*hrs},
  'astronautID':796
};
let candidateD = {
  'name':'Paddington',
  'species':'bear',
  'mass':31.8,
  'o2Used':function(hrs){return 0.047*hrs},
  'astronautID':291
};
let candidateE = {
  'name':'Pete',
  'species':'tortoise',
  'mass':417,
  'o2Used':function(hrs){return 0.010*hrs},
  'astronautID':599
};
let candidateF = {
  'name':'Hugs',
  'species':'ball python',
  'mass':2.3,
  'o2Used':function(hrs){return 0.018*hrs},
  'astronautID':890
};

let crew = [candidateA,candidateC,candidateE];

// missionDuration(1, 6371, 28000);
let canidate = conserveO2(crew);
console.log(orbitCircumference(6371));