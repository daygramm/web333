import React, {Component} from "react";
import bank from "../bank.png";

class Navbar extends Component {
    render() {
        return (
            <nav className="navbar navbar-dark fixed-top" style={{
                background: "black",
                height: 60
            }}>
                <a style={{
                    color: "white"
                }}>
                    <img src={bank} width={50} height={30}/>

                    DAPP Yield Staking (Decentralized Bank)
                </a>
                <ul>
                    <li>
                        <small style={{
                            color: "white"
                        }}>
                            ACCOUNT NUMBER:
                        </small>
                    </li>
                </ul>
            </nav>
        );
    }
}

export default Navbar;