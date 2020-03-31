// Code your crewMass function here:
function crewMass(crew){
  totalMassCrew = 0;
  for (let crewMember of crew) {
    totalMassCrew += crewMember.mass;
  }
  return Number(String(totalCrewMass).toFixed())
}


// Code your fuelRequired function here:
function fuelRequired(){
  let rocketMass = 75000;
  let totalCrewMass = crewMass(crew);
  let totalMass = totalCrewMass + rocketMass;
  let fuelNeeded = totalMass * 9.5;
  for (let animal of crew) {
    if (animal.species === 'dog' || animal.species === 'cat') {
      fuelNeeded += 200;
    } else {
      fuelNeeded += 100;
    }
  }
  fuelNeeded = Math.ceil(fuelNeeded);
  console.log(`The mission has a launch mass of ${totalMass}kg and requires ${fuelNeeded}kg of fuel.`);
  return fuelNeeded;
}



// The pre-selected crew is in the array at the end of this file.
// Feel free to add, remove, or switch crew members as you see fit.

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

let crew = [candidateA,candidateB,candidateD];

console.log(crewMass(crew));
