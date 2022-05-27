pragma solidity ^0.8.9;

contract TruffleTutorial {
    address public owner = msg.sender;
    string public message;

    constructor() public {
        message = "Hello World!";
    }

    modifier ownerOnly(){
        require(
            msg.sender == owner,
            "This function is restricted to the contract's owner"
        );
        _;
    }

    function setMessage(string memory _message) public ownerOnly returns (string memory){
        require(bytes(_message).length > 0);
        message = _message;
        return message;
    }
}