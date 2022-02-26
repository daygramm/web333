const Tether = global.artifacts.require("Tether");
const RWD = global.artifacts.require("RWD");
const DecentralBank = global.artifacts.require("DecentralBank");

module.exports = async function(deployer) {
  await deployer.deploy(Tether);
  await deployer.deploy(RWD);
  await deployer.deploy(DecentralBank);
};
