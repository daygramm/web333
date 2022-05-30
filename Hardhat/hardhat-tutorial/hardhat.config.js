require("@nomiclabs/hardhat-waffle")
require("@nomiclabs/hardhat-etherscan");
require("dotenv").config({ path: ".env" });

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
    solidity: "0.8.10",
    networks: {
        ganache: {
            url: `http://127.0.0.1:7545`,
            accounts: [`0x${process.env.GANACHE_PRIVATE_KEY1}`, `0x${process.env.GANACHE_PRIVATE_KEY2}`, `0x${process.env.GANACHE_PRIVATE_KEY3}`]
        },
        rinkeby: {
            url: `https://rinkeby.infura.io/v3/${process.env.APIKEY_INFURA}`,
            accounts: [`0x${process.env.RINKEBY_PRIVATE_KEY1}`]
        }
    },
    etherscan: {
        // Your API key for Etherscan
        // Obtain one at https://etherscan.io/
        apiKey: process.env.APIKEY_ETHERSCAN
    }
};


