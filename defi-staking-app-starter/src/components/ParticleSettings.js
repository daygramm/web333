import React, {Component} from "react";
import Particles from "react-tsparticles";

class ParticleSettings extends Component {

    render() {
        return (
            <div>
                <Particles
                    height='100vh'
                    width='100vw'
                    id='tsparticles'
                    options={{
                        background: {
                            color: {
                                value: "#6097e3"
                            }
                        },
                        fpsLimit: 60,
                        interactivity: {
                            detect_on: 'canvas',
                            events: {
                                onclick: {
                                    enable: true,
                                    mode: "push"
                                },
                                onhover: {
                                    enable: true,
                                    mode: "repulse"
                                }
                            },
                            modes: {
                                bubble: {
                                    distance: 300,
                                    duration: 2,
                                    opacity: 0.8,
                                    size: 40,
                                },
                                push: {
                                    quantity: 4,
                                },
                                repulse: {
                                    distance: 200,
                                    duration: 0.5,
                                },
                            }
                        },
                        particles: {
                            color: {
                                value: "#ffffff",
                            },
                            links: {
                                color: "#ffffff",
                                distance: 200,
                                enable: true,
                                opacity: 0.5,
                                width: 1
                            },
                            collisions: {
                                enable: true
                            },
                            move: {
                                direction: "none",
                                enable: true,
                                outMode: "bounce",
                                random: false,
                                speed: 1,
                                straight: false
                            },
                            number: {
                                density: {
                                    enable: true,
                                    value_area: 1000
                                },
                                value: 60
                            },
                            opacity: {
                                value: 0.6
                            },
                            shape: {
                                type: "circle"
                            },
                            size: {
                                random: true,
                                value: 3
                            }
                        }
                    }
                    }
                />
            </div>
        );
    }
}

export default ParticleSettings;
