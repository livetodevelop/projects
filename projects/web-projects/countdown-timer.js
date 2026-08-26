// Countdown Timer for Presentations
// usage: new CountdownTimer(300, document.getElementById('timer'))

class CountdownTimer {
    constructor(seconds, container) {
        this.totalSeconds = seconds;
        this.remaining = seconds;
        this.container = container;
        this.interval = null;
        this.running = false;
        
        this.render();
    }
    
    start() {
        if (this.running) return;
        
        this.running = true;
        this.interval = setInterval(() => {
            this.remaining--;
            this.render();
            
            if (this.remaining <= 0) {
                this.stop();
                this.container.style.color = '#d0021b';
                // could add a beep sound here but it's annoying
            }
        }, 1000);
    }
    
    stop() {
        this.running = false;
        clearInterval(this.interval);
    }
    
    reset() {
        this.stop();
        this.remaining = this.totalSeconds;
        this.container.style.color = '#e0e0e0';
        this.render();
    }
    
    formatTime(seconds) {
        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${mins}:${secs.toString().padStart(2, '0')}`;
    }
    
    render() {
        this.container.textContent = this.formatTime(this.remaining);
        
        // Change color when under 1 minute
        if (this.remaining <= 60 && this.remaining > 0) {
            this.container.style.color = '#f5a623';
        } else if (this.remaining <= 0) {
            this.container.style.color = '#d0021b';
        } else {
            this.container.style.color = '#e0e0e0';
        }
        
        // Make it bigger when running out of time
        if (this.remaining <= 10 && this.remaining > 0) {
            this.container.style.fontSize = '4rem';
        } else {
            this.container.style.fontSize = '3rem';
        }
    }
}

// Quick setup for common durations
const timers = {
    '5min': 300,
    '10min': 600,
    '15min': 900,
    '30min': 1800
};

// Example usage in HTML:
/*
<div id="timer" style="font-size: 3rem; font-family: monospace;"></div>
<button onclick="timer.start()">Start</button>
<button onclick="timer.stop()">Pause</button>
<button onclick="timer.reset()">Reset</button>

<script src="countdown-timer.js"></script>
<script>
    const timer = new CountdownTimer(300, document.getElementById('timer'));
</script>
*/
