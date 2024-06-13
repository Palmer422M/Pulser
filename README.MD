# Pulser - A pulse sweep generator based on Python and CircuitPython

## Synopsis
Pulse-generator definitions are encoded as python lists. Python + IDE is used on the host computer to develop and visualize the pulse trains.  CircuitPython is used on the microprocessor to deliver the TTL signal.

## Hardware
The board is the Adafruit "Feather ESP32-S3 (4GB, 2GB PSRAM)".  It's exceptionally powerful and this project really uses a tiny fraction of its capabilities.

## Files and Folders

- `pulser.py` - runs on ESP32s. Generates TTL sweeps. 
- `sweep_def.py` - the sweep definition file.  Used on PC and ESP32S systems.
- `sweep_view.py` - PC-based sweep viewer.
- `sweep_select.py` - helps maintain sweep library
- `sweeplib/` - folder for collection of sweep definitions (x.py) that can become sweep_def.py

## Pulse Generation Language
The basic idea is that for lists, Python interprets + as 
concatination, N* (or *N) as repeat N times. So start with 
single-element High and Low pulses. \
`H = [1]` \
`L = [0]` \
then just string them together, e.g. could be as simple as 
`(H + 3*L) *2` which is expanded as `[1, 0, 0, 0, 1, 0, 0, 0]`.

Using these two simple Python operators, complex pulse trains (sweeps) can be built bottom-up.
