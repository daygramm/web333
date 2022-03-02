import React, {Component} from "react";
import "./App.css";
import Navbar from "./Navbar"

class App extends Component {
    render() {
        return (
            <div>
                <Navbar/>
                <div className='text-center' style={
                    {
                        color: 'deepskyblue'
                    }}>
                    <h className="content">Hello World!</h>
                </div>
            </div>
        );
    }
}

export default App;