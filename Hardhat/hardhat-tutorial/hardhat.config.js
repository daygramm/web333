require("@nomiclabs/hardhat-waffle")
require("@nomiclabs/hardhat-etherscan");

const GANACHE_PRIVATE_KEY1 = "b479759b7683d3cdca2b276674e1a52724351ae1e8eb0b9170b82c2f8e464121";
const GANACHE_PRIVATE_KEY2 = "defb5e09db709f6afadcaa49127b36bbffa94343f4fd593c6f1c7b2e56d96ce9";
const GANACHE_PRIVATE_KEY3 = "51d961b040fdfc86e1a6aa6d6c3d3e319e74d41a2993e180eb5fc84f112e3507";

const RINKEBY_PRIVATE_KEY1 = "972ff45576a91a46b600be4b2ab7f41545858a1940fa2976172c168fe6d705ae";

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
    solidity: "0.8.10",
    networks: {
        ganache: {
            url: `http://127.0.0.1:7545`,
            accounts: [`0x${GANACHE_PRIVATE_KEY1}`, `0x${GANACHE_PRIVATE_KEY2}`, `0x${GANACHE_PRIVATE_KEY3}`]
        },
        rinkeby: {
            url: `https://rinkeby.infura.io/v3/1649bfcc28344a1cb472a4b7640f72c0`,
            accounts: [`0x${RINKEBY_PRIVATE_KEY1}`]
        }
    },
    etherscan: {
        // Your API key for Etherscan
        // Obtain one at https://etherscan.io/
        apiKey: "FRDHJP4ZBMH3X7R45XBAIWD23NPGQMD2TP"
    }
};


