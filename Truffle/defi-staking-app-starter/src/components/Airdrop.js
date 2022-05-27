import React, {Component} from "react";

class Airdrop extends Component {
    constructor() {
        super();
        this.state = {time: {}, seconds: 10};
        this.timer = 0;
        this.startTimer = this.startTimer.bind(this);
        this.countDown = this.countDown.bind(this);
    }

    startFarming() {
        let stakingB = this.props.stakingBalance;
        if (stakingB >= 50000000000000000000) {
            this.startTimer();
        }
    }

    startTimer() {
        if (this.timer == 0 && this.state.seconds > 0) {
            this.timer = setInterval(this.countDown, 1000);
        }
    }

    countDown() {
        let seconds = this.state.seconds - 1;
        this.setState({
            time: this.secondsToTime(seconds),
            seconds: seconds
        });
        if (seconds == 0) {
            this.props.issueRewardTokens();
            clearInterval(this.timer);
        }
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
        this.setState({time: timeLeftVar});
    }

    render() {
        this.startFarming();
        return (
            <div style={{color: 'black'}}>
                {this.state.time.h}:{this.state.time.m}:{this.state.time.s}
            </div>
        );
    }
}

export default Airdrop;