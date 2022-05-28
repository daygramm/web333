const { assert } = require("chai")

const Storage = artifacts.require("./Storage.sol")

require("chai")
    .use(require("chai-as-promised"))
    .should();

contract('Storage', ([contractOwner]) =>
{
    let storage

    before(async () =>
    {
        storage = await Storage.deployed()
    })

    it("deploys successfully", async () =>
    {
        const address = await storage.address

        assert.notEqual(address, "")
        assert.notEqual(address, undefined)
        assert.notEqual(address, null)
        assert.notEqual(address, 0x0)
    })

    it("set number", async () =>
    {
        await storage.setNumber(666)
        const data = await storage.getNumber()

        assert.equal(data, 666)
    })

    it("add number", async () =>
    {
        await storage.addNumber()
        const data = await storage.getNumber()

        assert.equal(data, 667)
    })
}
)