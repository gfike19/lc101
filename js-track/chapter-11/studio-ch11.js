// Code findMinValue here:
function findMinValue (arr) {
    let smallest = arr[0];
    for(let i = 0; i < arr.length; i++){
      if (arr[i] < smallest){
        smallest = arr[i];
      }
    }
    return smallest;
  }
  
  function sort(arr){
      let newArr = [];
  
      while(arr.length != 0){
          let minVal = findMinValue(arr);
          let minIndex = arr.indexOf(minVal);
          arr.splice(minIndex, 1);
          newArr.push(minVal);
      }
  
      return newArr;
  }
  
  let sorted = sort([ -2, 0, -10, -44, 5, 3, 0, 3 ]);
  console.log(sorted);