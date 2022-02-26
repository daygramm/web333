require("babel-register");
require("babel-polyfill");

module.exports = {
    networks: {
        development: {
            host: "127.0.0.1",
            port: "7545",
            network_id: "*",
            from:"8882107d420fb7b4349c175090a3d52fb069ea854d9d661e70dc5d3a1757dfae"
        }
    },
    contracts_directory: "./src/contracts",
    contracts_build_directory: "./src/truffle_abis",
    compilers: {
        solc: {
            version: "^0.5.0",
            optimizer: {
                enabled: true,
                runs: 200
            }
        }
    }
}

