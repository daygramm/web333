const { ethers } = require("hardhat");

async function main ()
{
    // Contract Token
    const [deployer] = await ethers.getSigners();
    console.log("Deploying contracts with the account:", deployer.address);
    console.log("Account balance:", (await deployer.getBalance()).toString());

    const Token = await ethers.getContractFactory("Token");
    const token = await Token.deploy();
    console.log("Contract Token deployed to address:",token.address);

    // Contract NFT
    const NFT = await ethers.getContractFactory("NFT");
    const nft = await NFT.deploy();
    console.log("Contract NFT deployed to address:",nft.address);
}

main()
    .then(() => process.exit(0))
    .catch(error =>
    {
        console.error(error);
        process.exit(1);
    });