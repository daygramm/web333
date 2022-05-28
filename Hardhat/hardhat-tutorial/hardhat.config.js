require("@nomiclabs/hardhat-waffle")

const PRIVATE_KEY1 = "1505163bbfe508b34defe9d58fe58052bbb65ac507c6bd670b9643b3108ea983";
const PRIVATE_KEY2 = "c967bf39e29b0946d66a167199e7732562231ebed8ef80fb952c84fd5736b632";
const PRIVATE_KEY3 = "7b13607986c5501f2db23ad278d699c7f29b8b8e25e58c4729ed8d00bd572441";

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
    solidity: "0.7.3",
    networks: {
        ganache: {
            url: `http://127.0.0.1:7545`,
            accounts: [`0x${PRIVATE_KEY1}`, `0x${PRIVATE_KEY2}`, `0x${PRIVATE_KEY3}`]
        }
    }
};


