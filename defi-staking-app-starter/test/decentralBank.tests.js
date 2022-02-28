const {assert} = require("chai");
const {default: Web3} = require("web3");

const Tether = global.artifacts.require("Tether");
const RWD = global.artifacts.require("RWD");
const DecentralBank = global.artifacts.require("DecentralBank");

require("chai")
    .use(require("chai-as-promised"))
    .should();

contract("DecentralBank", ([owner, customer]) => {
    let tether;
    let reward;
    let decentralBank;

    function tokens(number) {
        return Web3.utils.toWei(number, "ether");
    }

    before(async () => {
        tether = await Tether.new();
        reward = await RWD.new();
        decentralBank = await DecentralBank.new(reward.address, tether.address);

        await reward.transfer(decentralBank.address, tokens("1000000"));
        await tether.transfer(customer, tokens("100"), {from: owner});
    });

    describe("Mock Tether Deployment", async () => {
        it("matches name successfully", async () => {
            let tether = await Tether.new();
            const name = await tether.name;
            assert.equal(name, "Mock Tether Token");
        });
    });

    describe("Reward Token Deployment", async () => {
        it("matches name successfully", async () => {
            let tether = await Tether.new();
            const name = await tether.name;
            assert.equal(name, "Reward Token");
        });
    });

    describe("Decentral Bank Deployment", async () => {
        it("matches name successfully", async () => {
            const name = await decentralBank.name();
            assert.equal(name, "Decentral Bank");
        });

        it("contract has tokens", async () => {
            let balance = await reward.balanceOf(decentralBank.address);
            assert.equal(balance, tokens("1000000"));
        });
    });
});
