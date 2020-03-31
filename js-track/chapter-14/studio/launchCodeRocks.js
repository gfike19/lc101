function launchOutput(num){
    //your code here
    if(num % 2 == 0){  
      if(num % 3 == 0){
        if(num % 5 == 0 && num % 3 == 0){
          return "LaunchCode Rocks!";
        }
        return "LaunchCode!";
      }
      if(num % 5 == 0) {
        return "Launch Rocks! (CRASH!!!!)";
      }   
      return "Launch!";
    }

    if (num % 3 == 0){
      if(num % 5 == 0){
        return "Code Rocks!"
      }
      return "Code!";
    }

    if(num % 5 == 0){
      return "Rocks!";
    }
    return "Rutabagas! That doesn't work.";
  }
  
  module.exports = launchOutput;