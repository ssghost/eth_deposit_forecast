import { expect } from "chai";
import { it } from "types/jest";
import { deploy } from "./deploy";

it("Valid contract address", async function() {
    let [c_address, , ] = await deploy();
    expect(c_address.notEqual(null));
});

it("Valid Upkeep ID", async function() {
    let [, upkeepID, ] = await deploy();
    expect(upkeepID.notEqual(0));
});

it("Valid casting data", async function() {
    let [, ,s_data] = await deploy();
    expect(s_data.notEqual(""));
});