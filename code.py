import board
import pulseio
import digitalio
import time
import array
import json

# Define the IR LED and button pins
IR_LED_PIN = board.GP16
BUTTON_PIN = board.GP15

# Create a PulseOut object using the IR LED pin
ir_out = pulseio.PulseOut(IR_LED_PIN, frequency=38000, duty_cycle=2**15)

# Setup the button as input with pull-up resistor
button = digitalio.DigitalInOut(BUTTON_PIN)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Load the IR codes from a JSON file
def load_ir_codes():
    with open("ir_codes.json", "r") as file:
        return json.load(file)

# Set the current device and action
current_device = "veon"  # Change as needed
current_action = "mute"  # Change as needed

# Load the pulse codes for the selected device and action
ir_codes = load_ir_codes()
raw_pulses = array.array("H", ir_codes[current_device][current_action])

# Transmit the IR signal
while True:
    if not button.value:  # Button is pressed
        print(f"Transmitting {current_action} action for {current_device}...")
        raw_pulses = array.array("H", ir_codes[current_device][current_action])
        ir_out.send(raw_pulses)
        time.sleep(0.2)  # Simple debounce delay
    time.sleep(0.1)  # Small delay to avoid busy-waiting
