const { assert } = require("console");
const { default: Web3 } = require("web3");

const Tether = global.artifacts.require("Tether");
const RWD = global.artifacts.require("RWD");
const DecentralBank = global.artifacts.require("DecentralBank");

require("chai")
  .use(require("chai-as-promised"))
  .should();

contract("DecentralBank", ([accounts]) => {
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

    await reward.transfer(decentralBank.address,tokens("1000000"));
    await tether.transfer(accounts[1],tokens("100"),{from:accounts[0]});
  });

  describe("Mock Tether Deployment", async () => {
    it("matches name successfully", async () => {
      let tether = await Tether.new();
      const name = await tether.name;
      assert.equal(name, "Mock Tether Token");
    });
  });
});
