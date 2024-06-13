# M Palmer 6/7/2024.
import board
import digitalio
import time

import sweep_def

__VERSION = '1.0'
__APP = 'Pulser'

OP_A = board.A0
OP_B = board.A1
OP_LED = board.A2
IN_BUTTON = board.A3
DEBOUNCE_TIME = 0.050     # in Seconds

def play_sequence():
    """
    Play the pulse train sequence once.
    returns:
        button_press : true if button terminated the sequence
    """
    pulse_ndx = 0
    last_time_ns = time.monotonic_ns()
    while True:

        # Get the current time using time.monotonic().
        time_now_ns = time.monotonic_ns()

        # Check if the time elapsed since the last LED state change is greater than the blink rate.
        if time_now_ns - last_time_ns > dt_ns:
            last_time_ns = time_now_ns

            op_a.value = yA[pulse_ndx]
            op_b.value = yB[pulse_ndx]
            pulse_ndx += 1
            if pulse_ndx == len(yA):
                rval = False
                break   # Normal termination - end of sequence

        if not in_button.value:
            print('Interrupt')
            rval = True
            break   # Premature termination - button press

    op_a.value = 0
    op_b.value = 0
    return rval

def wait_for_button_release():
    """
    Wait for a button to be released then wait for release plus debounce time
    """
    while not in_button.value:
        pass
    time.sleep(DEBOUNCE_TIME)


def wait_for_button_press():
    """
    Wait for a button press plus debounce time
    """

    while in_button.value:
        pass
    time.sleep(DEBOUNCE_TIME)


####### MAIN ######

print("%s V%s" % (__APP, __VERSION))

# Create a DigitalInOut object for the four i/o port lines being used here
op_a = digitalio.DigitalInOut(OP_A)
op_b = digitalio.DigitalInOut(OP_B)
op_led = digitalio.DigitalInOut(OP_LED)
in_button = digitalio.DigitalInOut(IN_BUTTON)

# Set the direction of the i/o pins.
op_a.direction = digitalio.Direction.OUTPUT
op_b.direction = digitalio.Direction.OUTPUT
op_led.direction = digitalio.Direction.OUTPUT

in_button.direction = digitalio.Direction.INPUT
in_button.pull = digitalio.Pull.UP

# Okay, preliminaries over, load the sequences.
yA = sweep_def.SWEEP_A
yB = sweep_def.SWEEP_B
dt_ms = sweep_def.PULSE_PERIOD_MS
manual = sweep_def.MANUAL_CONTROL
banner = sweep_def.DESCRIPTION

print(banner)
print('Sequence Length:', len(yA))
print('Pulse Period: %d ms' % dt_ms)
print('Manual:', manual)

# setup list element sequence time (time between pulse transitions). Note the nS time-scale
dt_ns = dt_ms * 1000 * 1000

# Initialize the output states to (off).
op_a.value = 0
op_b.value = 0

restart = True    # At start and after interruption
while True:
    if restart or manual:
        print('Waiting for button press...')
        wait_for_button_press()
        wait_for_button_release()
        restart = False

    op_led.value = 1    # Turn on LED while outputs are active
    but_term = play_sequence()
    op_led.value = 0
    if but_term:
        time.sleep(DEBOUNCE_TIME)
        wait_for_button_release()
        restart = True

