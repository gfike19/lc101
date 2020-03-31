function checkFuel(level) {
   if (level > 100000){
      return 'green';
   } else if (level > 50000){
      return 'yellow';
   } else {
      return 'red';
   }
}

console.log(`checkFuel(100000) is ${checkFuel(100000)}`);
console.log(`checkFuel(50000) is ${checkFuel(50000)}`);
console.log(`checkFuel(100001) is ${checkFuel(100001)}`);
console.log(`checkFuel(50001) is ${checkFuel(50001)}`);