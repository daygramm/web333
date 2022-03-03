import React, {Component} from "react";

class Airdrop extends Component {
    constructor() {
        super();
        this.state = {time: {}, seconds: 20};
        this.timer = 0;
        // this.startTime = this.startTime.bind(this);
        // this.countDown = this.countDown.bind(this);
    }

    secondsToTime(secs) {
        let hours, minutes, seconds;
        hours = Math.floor(secs / 3600);
        minutes = Math.floor(secs % 3600 / 60);
        seconds = Math.floor(secs % 3600 % 60);

        let obj = {
            'h': hours,
            'm': minutes,
            's': seconds
        }
        return obj;
    }

    componentDidMount() {
        let timeLeftVar = this.secondsToTime(this.state.seconds);
        this.setState = {time: timeLeftVar};
    }

    render() {
        return (
            <div style={{color: 'black'}}>
                {this.state.time.h}:{this.state.time.m}:{this.state.time.s}
            </div>
        );
    }
}

export default Airdrop;