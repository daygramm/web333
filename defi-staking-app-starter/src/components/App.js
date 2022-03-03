import React, {Component} from "react";
import "./App.css";
import Navbar from "./Navbar"
import Main from "./Main"
import Web3 from "web3";
import Tether from "../truffle_abis/Tether.json";
import RWD from "../truffle_abis/RWD.json";
import DecentralBank from "../truffle_abis/DecentralBank.json";
import ParticleSettings from "./ParticleSettings";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            account: "0x0",
            tetherBalance: "0",
            rwdBalance: "0",
            stakingBalance: "0",
            rwd: {},
            reward: {},
            decentralBank: {},
            loading: true
        }
    }

    render() {
        let content;
        {
            this.state.loading
                ? content = <p id='loader' className='text-center' style={{margin: '60px',color:'white'}}>LOADING PLEASE...</p>
                : content =
                    <Main
                        tetherBalance={this.state.tetherBalance}
                        rwdBalance={this.state.rwdBalance}
                        stakingBalance={this.state.stakingBalance}
                        stakeTokens={this.stakeTokens}
                        unstakeTokens={this.unstakeTokens}
                    />
        }

        return (
            <div className='App' style={{position: 'relative'}}>
                <div style={{position: 'absolute'}}>
                    <ParticleSettings/>
                </div>
                <Navbar account={this.state.account}/>
                {/*<div className='text-center' style={{color: 'deepskyblue'}}>*/}
                {/*    <h1 className="content">{this.state.loading ? "loading" : "loaded"}</h1>*/}
                {/*</div>*/}
                <div className="container-fluid mt-5">
                    <div className="row">
                        <main role="main" className="col-lg-12 ml-auto mr-auto" style={{maxWidth: '600px', minWidth: '100vm'}}>
                            <div>
                                {content}
                            </div>
                        </main>
                    </div>
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

        const rwdData = RWD.networks[networkId];
        if (rwdData) {
            const rwd = new web3.eth.Contract(RWD.abi, rwdData.address);
            this.setState({rwd: rwd});
            let rwdBalance = await rwd.methods.balanceOf(account[0]).call();
            this.setState({rwdBalance: rwdBalance.toString()});
        } else {
            alert("Error! RWD contract not deployed - no detected network!");
        }

        const decentralBankData = DecentralBank.networks[networkId];
        if (decentralBankData) {
            const decentralBank = new web3.eth.Contract(DecentralBank.abi, decentralBankData.address);
            this.setState({decentralBank: decentralBank});
            let stakingBalance = await decentralBank.methods.stakingBalance(account[0]).call();
            this.setState({stakingBalance: stakingBalance.toString()});
        } else {
            alert("Error! Decentral Bank contract not deployed - no detected network!");
        }

        console.log(account);
        console.log(networkId);
        this.setState({loading: false});
    }

    async UNSAFE_componentWillMount() {
        await this.loadWeb3();
        await this.loadWeb3Data();
    }

    stakeTokens = (amount) => {
        this.setState({loading: true});
        this.state.tether.methods.approve(this.state.decentralBank._address, amount).send({from: this.state.account}).on("transactionHash", (hash) => {
        });
        this.state.decentralBank.methods.depositTokens(amount).send({from: this.state.account}).on("transactionHash", (hash) => {
            this.setState({loading: false});
        });
    }

    unstakeTokens = () => {
        this.setState({loading: true});
        this.state.decentralBank.methods.unstakeTokens().send({from: this.state.account}).on("transactionHash", (hash) => {
            this.setState({loading: false});
        });
    }
}

export default App;