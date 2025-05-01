# Infrared Tests with Raspberry Pi Pico RP2040 Microcontroller

## Setup

- **Device:** Raspberry Pi Pico (RP2040)
- **Language:** Adafruit CircuitPython 9.2.1 (released on 2024-11-20)
- **Library:** Adafruit_CircuitPython_IRRemote

## Testing notes

The Adafruit sample code captures both raw and decoded IR signals. Raw codes can be captured and retransmitted, but decoding shorter encoded signals may result in incomplete or inaccurate transmissions.

### IR Codes for Devices in `transmitter/ir_codes.json`

| Alias       | Model        | Protocol | Buttons Captured (Approx) |
|-------------|--------------|----------|---------------------------|
| edifier     | R1280DBs     | NEC      | 4                         |
| Veon        | SRO322016    | NEC      | 10                        |
| hisense     | 55Q6NNZ      | NEC      | 18                        |
| fan_seville | ehf10119p    | Panasonic| 3                         |
