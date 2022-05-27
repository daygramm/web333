const truffleTutorial = artifacts.require("TruffleTutorial");

module.exports = function (deployer) {
    deployer.deploy(truffleTutorial);
};
