const hello = require('../hello.js');
const assert = require('assert');

describe("hello world test", function(){

   it("should return a custom message when name is specified", function(){
      assert.strictEqual(hello("Jasmine"), "Hello, Jasmine!");
   });

})