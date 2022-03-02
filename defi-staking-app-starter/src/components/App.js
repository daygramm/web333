import React, {Component} from "react";
import "./App.css";
import Navbar from "./Navbar"
import Web3 from "web3";
import Tether from "../truffle_abis/Tether.json";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            account: "0x0",
            tetherBalance: "0",
            rewardBalance: "0",
            stakingBalance: "0",
            tether: {},
            reward: {},
            decentralBank: {},
            loading: true
        }
    }

    render() {
        return (
            <div>
                <Navbar account={this.state.account}/>
                <div className='text-center' style={{color: 'deepskyblue'}}>
                    {/*<h className="content">Hello World!</h>*/}
                </div>
            </div>
        );
    }

    async loadWeb3() {
        if (window.ethereum) {
            window.web3 = new Web3(window.ethereum);
            await window.ethereum.enable();
        } else if (window.web3) {
            window.web3 = new Web3(window.web3.currentProvider);
        } else {
            alert("No ethereum browser detected! You can check out MetaMask!");
        }
    }

    async loadWeb3Data() {
        const web3 = window.web3;

        const account = await web3.eth.getAccounts();
        this.setState({account: account[0]});

        const networkId = await web3.eth.net.getId();
        const tetherData = Tether.networks[networkId];
        if (tetherData) {
            const tether = new web3.eth.Contract(Tether.abi, tetherData.address);
            this.setState({tether: tether});
            let tetherBalance = await tether.methods.balanceOf(account[0]).call();
            this.setState({tetherBalance: tetherBalance.toString()});
        } else {
            alert("Error! Tether contract not deployed - no detected network!");
        }

        console.log(account);
        console.log(networkId);
        console.log(this.state.tetherBalance);
    }

    async UNSAFE_componentWillMount() {
        await this.loadWeb3();
        await this.loadWeb3Data();
    }
}

export default App;