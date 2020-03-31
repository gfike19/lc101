function holdStatus(arr){
   if (arr.length < 7) {
      return `Spaces available: ${7 - arr.length}`;
   } else if (arr.length > 7){
      return `Over capacity by ${arr.length - 7} items.`
   } else {
      return "Full";
   }
}


let cargoHold = ['meal kits', 'space suits', 'first-aid kit', 'satellite', 'gold', 'water', 'AE-35 unit'];


let deckMops = function(cargoHold){
   let steal = [];
   let swap = ["oranges", "crackers", "eye patch", "hankerchief", "trifol hat"];
   let search = ['dilithium', 'gold', 'AE-35 unit', 'Legos', 'TI-89 calculator'];
   itemIndex = 0;
   for(let i = 0; i < cargoHold.length; i++){
      let item = cargoHold[i];

      if(search.includes(item)){
         let replaceItem = swap.pop();
         steal.push(cargoHold[i]);
         cargoHold[i] = replaceItem;
      }
   }

   return steal;
};

console.log(deckMops(cargoHold));
