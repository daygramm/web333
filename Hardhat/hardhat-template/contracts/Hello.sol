// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.22 <0.9.0;
// Import this file to use console.log
import "hardhat/console.sol";

contract Hello {
    string public name;

    constructor(string memory _name) {
        name = _name;
    }

    function setGreeting(string memory _name) public {
        name = _name;
    }

    function greet() public view returns (string memory) {
        // Uncomment this line to print a log in your terminal
        console.log("current block timestamp is: %o", block.timestamp);
        return name;
    }
}
