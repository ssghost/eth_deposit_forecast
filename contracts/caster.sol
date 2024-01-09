// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@chainlink/contracts/src/v0.8/automation/AutomationCompatible.sol";
import "@jsmnSol/JsmnSolLib.sol";

contract Caster is AutomationCompatibleInterface, Ownable {
    bytes32 public _castdata = "";
    uint256 public _interval = 1 days;

    constructor(uint256 interval, bytes32 calldata castdata) {
        castdata = _castdata;
        interval = _interval;
        lastTimeStamp = block.timestamp;
    }

    function checkUpkeep()
        external
        view
        override
        returns (bool upkeepNeeded)
    {
        upkeepNeeded = (block.timestamp - lastTimeStamp) > interval;
    }

    function performUpkeep(bytes32 calldata castdata) external override {
        if ((block.timestamp - lastTimeStamp) > interval) {
            lastTimeStamp = block.timestamp;
            json = vm.readFile("../castdata.json");
            (_, tokens, _) = JsmnSolLib.parse(json);
            castdata = getBytes(json, tokens.start, tokens.end);
            console.log(castdata);
        }
    }

    function showData() view onlyOwner returns (bytes32 calldata castdata) {
        return castdata;
    }

    function payAndShow(uint96 _amount) payable returns (bytes32 calldata castdata) {
        require(_amount >= 0.0001 ether);
        require(msg.sender.value >= _amount);
        (bool success, ) = owner.call{value: _amount}("");
        require(success);
        return castdata;
    }
}
