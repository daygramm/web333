pragma solidity ^0.5.4;

contract Tether {
    string public name = "Mock Tether Token";
    string public symbol = "mUSDT";
    uint256 public totalSupply = 1000000000000000000000000; // 1百万
    uint8 public decimals = 18;

    event Transfer(
        address indexed _from,
        address indexed _to,
        uint _value
    );

    event Approve(
        address indexed _owner,
        address indexed _spender,
        uint _value
    );

    //    error insufficientBalance(
    //        uint requested,
    //        uint avaliable
    //    );

    mapping(address => uint256) public balanceOf;

    constructor(){
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address to, uint value) public returns (bool success) {
        //        if (value > balanceOf[msg.sender]) {
        //            revert insufficientBalance(value, balanceOf[msg.sender]);
        //            return false;
        //        }
        require(balanceOf[msg.sender] >= value);
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }
}