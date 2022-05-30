const HDWalletProvider = require('truffle-hdwallet-provider');

require('dotenv').config({ path: '.env' })
const mnemonic = process.env.MNEMONIC;
const infuraUrl = process.env.INFURA_URL;

module.exports = {
    networks: {
        loc_development_development: {
            host: "127.0.0.1",
            port: 7545,
            network_id: "*"
        },
        inf_Mega_rinkeby: {
            network_id: 4,
            gasPrice: 100000000000,
            provider: () => new HDWalletProvider(mnemonic, infuraUrl)
        }
    },
    mocha: {},
    compilers: {
        solc: {
            version: "0.8.10"
        }
    }
};
