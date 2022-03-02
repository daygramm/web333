import React, {Component} from "react";
import "./App.css";
import Navbar from "./Navbar"
import Web3 from "web3";

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
        const Web3 = window.web3;
        const account = await Web3.eth.getAccounts();
        this.setState({account: account});
        console.log(account);
    }

    async UNSAFE_componentWillMount() {
        await this.loadWeb3();
        await this.loadWeb3Data();
    }
}

export default App;