const {assert} = require("chai");
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
        return web3.utils.toWei(number, "ether");
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
            const name = await tether.name();
            assert.equal(name, "Mock Tether Token");
        });
    });

    describe("Reward Token Deployment", async () => {
        it("matches name successfully", async () => {
            let rwd = await RWD.new();
            const name = await rwd.name();
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

    describe("Yield Farming", async () => {
        it('rewards tokens for staking', async () => {
            let result;
            result = await tether.balanceOf(customer);
            assert.equal(result.toString(), tokens("100"), "customer wallet balance before staking");

            await tether.approve(decentralBank.address, tokens("100"), {from: customer});
            await decentralBank.depositTokens(tokens("100"), {from: customer});

            result = await tether.balanceOf(decentralBank.address);
            assert.equal(result.toString(), tokens("100"), "合约余额转入100个Tether");

            result = await decentralBank.isStaking(customer);
            assert.equal(result.toString(), "true", "合约当前用户的存入状态应为true");

        });
    })
});
