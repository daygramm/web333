pragma solidity ^0.5.4;

contract Migrations {
    address public owner;
    uint public last_completed_migration;

    constructor() public {
        owner = msg.sender;
    }

    modifier restricted(){
        if (msg.sender == owner)
        {
            _;
        }
    }

}