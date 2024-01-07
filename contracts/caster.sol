// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@chainlink/contracts/src/v0.8/automation/AutomationCompatible.sol";
import "@jsmnSol/JsmnSolLib.sol";

contract Caster is AutomationCompatibleInterface {
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

    function showData() view returns (bytes32 calldata castdata) {
        return castdata;
    }
}
