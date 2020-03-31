const launchOutput = require('../launchCodeRocks.js');
const assert = require('assert');

describe("launchOutput", function(){

  //testing code here...
    it("should determine if a number is divisble by 2",function(){
      assert.strictEqual(launchOutput(4), "Launch!")
    });

    it("should determine if a number is divible by 3", function() {
      assert.strictEqual(launchOutput(9), "Code!");
    });

    it("should determine if a number is divisible by 5", function () {
      assert.strictEqual(launchOutput(25), "Rocks!");
    })

    it("should determine if a number is divisible by 2 and 3", function() {
      assert.strictEqual(launchOutput(6), "LaunchCode!");
    } );

    it("should determine if a number is divisible by 3 and 5", function() {
      assert.strictEqual(launchOutput(15), "Code Rocks!");
    } );

    it("should determine if a number is divisible by 2 and 5", function() {
      assert.strictEqual(launchOutput(10), "Launch Rocks! (CRASH!!!!)");
    } );

    it("should determine if a number is divisble by 2, 3, and 5", function() {
      assert.strictEqual(launchOutput(30), "LaunchCode Rocks!");
    });

    it("should determine if a number is not divisble by 2, 3, or 5", function() {
      assert.strictEqual(launchOutput(7), "Rutabagas! That doesn't work.");
    });
})