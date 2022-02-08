// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Target.sol";

contract Attacker {
    Privacy public target;

    constructor(address _target) public {
        target = Privacy(_target);
    }

    function attack(bytes32 _key) public {
        bytes16 key = bytes16(_key);
        target.unlock(key);
    }
}
