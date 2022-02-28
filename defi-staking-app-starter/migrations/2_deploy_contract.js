const Tether = global.artifacts.require("Tether");
const RWD = global.artifacts.require("RWD");
const DecentralBank = global.artifacts.require("DecentralBank");

module.exports = async function (deployer, network, accounts) {
    // 部署Tether代币
    await deployer.deploy(Tether);
    const tether = await Tether.deployed();

    // 部署奖励代币
    await deployer.deploy(RWD);
    const rwd = await RWD.deployed();

    // 部署去中心化银行
    await deployer.deploy(DecentralBank, rwd.address, tether.address);
    const decentralBank = await DecentralBank.deployed();

    // 把代币全部存入去中心化银行
    await rwd.transfer(decentralBank.address, "1000000000000000000000000");

    // 发送Tether代币到投资者
    await tether.transfer(accounts[1], "100000000000000000000");
};
