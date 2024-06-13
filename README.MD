# Pulser - A pulse sweep generator based on Python and CircuitPython

## Synopsis
Pulse-generator definitions are encoded as python lists. Python + IDE is used on the host computer to develop and visualize the pulse trains.  CircuitPython is used on the microprocessor to deliver the TTL signal.

## Hardware
The board is the Adafruit "Feather ESP32-S3 (4GB, 2GB PSRAM)".  It's exceptionally powerful and this project really uses a tiny fraction of its capabilities.


## Files and Folders


Files
: `pulser.py` - Runs on ESP32s. Generates TTL sweeps.
: `sweep_def.py` - the sweep definition file.  Used on PC and ESP32S systems.
: `sweep_view.py` - PC-based sweep viewer.
: `sweep_select.py` - helps maintain sweep library

Folders
: `sweeplib/` - folder for collection of sweep definitions (x.py) that can become sweep_def.py

