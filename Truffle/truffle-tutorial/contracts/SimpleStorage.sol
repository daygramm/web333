pragma solidity >=0.7.0 <0.9.0;

contract simpleStorage {
    uint256 storeData;

    // string names = "Michael";
    // bool switchON = true;

    function set(uint256 x) public {
        storeData = x * 5;
    }

    function get() public view returns (uint256) {
        return storeData;
    }
}
