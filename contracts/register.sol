// SPDX-License-Identifier: MIT
pragma solidity ^0.8.6;

import {LinkTokenInterface} from "@chainlink/contracts/src/v0.8/shared/interfaces/LinkTokenInterface.sol";

struct RegistrationParams {
    string name;
    bytes encryptedEmail;
    address upkeepContract;
    uint32 gasLimit;
    address adminAddress;
    uint8 triggerType;
    bytes checkData;
    bytes triggerConfig;
    bytes offchainConfig;
    uint96 amount;
}

interface AutomationRegisterInterface {
    function registerUpkeep(
        RegistrationParams calldata params
    ) external returns (uint256);
}

contract UpkeepIDConditional {
    LinkTokenInterface public immutable i_link;
    AutomationRegistrarInterface public immutable i_registrar;

    constructor(
        LinkTokenInterface link,
        AutomationRegisterInterface register
    ) {
        i_link = link;
        i_register = register;
    }

    function registerAndShowID(RegistrationParams memory params) public {
        i_link.approve(address(i_register), params.amount);
        uint256 upkeepID = i_registrar.registerUpkeep(params);
        if (upkeepID != 0) {
            console.log(upkeepID);
        } else {
            revert("auto-approve disabled");
        }
    }
}
