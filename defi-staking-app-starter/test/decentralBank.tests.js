const { assert } = require("console");

const Tether = global.artifacts.require("Tether");
const RWD = global.artifacts.require("RWD");
const DecentralBank = global.artifacts.require("DecentralBank");

require("chai")
  .use(require("chai-as-promised"))
  .should();

describe("DecentralBank", (accounts) => {
  describe("Mock Tether Deployment", async () => {
    it("matches name successfully", async () => {
      let tether = await Tether.new();
      const name = await tether.name;
      assert.equal(name, "Mock Tether Token");
    });
  });
});
