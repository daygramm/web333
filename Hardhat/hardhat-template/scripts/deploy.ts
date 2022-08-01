import { ethers } from "hardhat";

async function main() {
  const helloFactory = await ethers.getContractFactory("Hello");
  const hello = await helloFactory.deploy("Gaojian");
  await hello.deployed();

  console.log("Contract Hello deployed to address:", hello.address);
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exitCode = 1;
  });
