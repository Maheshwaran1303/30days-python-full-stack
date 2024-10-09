// Get the necessary elements
const fan = document.getElementById('fan');
const statusText = document.getElementById('status');
const speedText = document.getElementById('speed');
const onButton = document.getElementById('onButton');
const offButton = document.getElementById('offButton');

// Function to turn the fan on (start with speed 1)
function turnOn() {
    fan.classList.add('speed1');
    statusText.textContent = "Fan is on";
    speedText.textContent = "Speed: 1";
    onButton.disabled = true;
    offButton.disabled = false;
}

// Function to turn the fan off
function turnOff() {
    fan.classList.remove('speed1', 'speed2', 'speed3');
    statusText.textContent = "Fan is off";
    speedText.textContent = "Speed: 0";
    onButton.disabled = false;
    offButton.disabled = true;
}

// Function to set the fan speed and update the display
function setSpeed(speed) {
    // Remove previous speed classes
    fan.classList.remove('speed1', 'speed2', 'speed3');

    // Add the selected speed class and update speed text
    if (speed === 1) {
        fan.classList.add('speed1');
        speedText.textContent = "Speed: 1";
        onButton.disabled = true;
        offButton.disabled = false;
    } else if (speed === 2) {
        fan.classList.add('speed2');
        speedText.textContent = "Speed: 2";
        onButton.disabled = true;
        offButton.disabled = false;
    } else if (speed === 3) {
        fan.classList.add('speed3');
        speedText.textContent = "Speed: 3";
        onButton.disabled = true;
        offButton.disabled = false;
    }
}
