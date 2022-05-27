const { assert } = require("chai")

const SimpleStorage = artifacts.require("./SimpleStorage.sol")

require("chai")
    .use(require("chai-as-promised"))
    .should();

contract('SimpleStorage', ([contractOwner, secondAddress, thirdAddress]) =>
{
    let storage

    before(async () =>
    {
        storage = await SimpleStorage.deployed()
    })

    it("deploys successfully", async () =>
    {
        const address = await storage.address

        assert.notEqual(address, "")
        assert.notEqual(address, undefined)
        assert.notEqual(address, null)
        assert.notEqual(address, 0x0)
    })

    it("set", async () =>
    {
        await storage.set(666)
        const data = await storage.get()

        assert.equal(data, 666)
    })
}
)