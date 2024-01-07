import { ethers } from "hardhat";
import { process } from "types/node";

export interface RegistrationParams {
    name: string;
    encryptedEmail: string;
    upkeepContract: string;
    gasLimit: number;
    adminAddress: string;
    triggerType: number;
    checkData: string;
    triggerConfig: string;
    offchainConfig: string;
    amount: number;
}

async function deploy() {
	const caster = await ethers.deployContract("Caster", [], {});

	await caster.waitForDeployment();

	const c_address = caster.address;

	let params = {upkeepContract: c_address};

    const register = await ethers.deployContract("UpkeepIDConditional", [], {});

    await register.waitForDeployment();

	const upkeepID = await register.registerAndShowID(params);

    console.log(`Deployment completed. Upkeep ID is ${upkeepID}.`);
}

deploy().catch((error) => {
  	console.error(error);
  	process.exitCode = 1;
});
