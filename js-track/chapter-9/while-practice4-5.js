20let startFuel = 0;
let astroNum = 0;
let altitude = 0;

const input = require('readline-sync');

while (startFuel < 5000 || startFuel > 30000){
    startFuel = input.question("Entering the starting fuel level: ");
}

while(astroNum < 1 || astroNum > 7){
    astroNum = input.question("How many astronauts are there? ");
}

let astroFuel = 100 * astroNum;


while(startFuel  - astroFuel > 0){

    startFuel = startFuel - astroFuel;
    altitude = altitude + 50;
}

console.log(`The shuttle gained an altitude ${altitude} km`);

if (altitude >= 2000){
	console.log("Orbit achieved!");
} else {
	console.log("Failed to reach orbit.")
}