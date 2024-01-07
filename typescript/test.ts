import { expect } from "chai";
import { it } from "types/jest";
import { deploy } from "./deploy";

it("Valid contract address", async function() {
    let [c_address, _] = await deploy();
    expect(c_address.notEqual(null));
});

it("Valid Upkeep ID", async function() {
    let [_, upkeepID] = await deploy();
    expect(upkeepID.notEqual(0));
});