"""
Sweep definition file.  This file will be common between the PC-based viewer
and the microcontroller-based pulse generator.
It needs to define two sweep sequences:
    SWEEP_A and SWEEP_B (traces)
and some properties:
    DESCRIPTION - a string that documents this sweep file, e.g. "6/1/2024 - Experiment 6A"
    PULSE_PERIOD_MS - the time interval between pulses in ms.
    MANUAL_CONTROL - a boolean that controls whether the sweep repeats continuously (False)
                     or wait's for a button press before repeating (True).
"""

# These are easy so do them first
DESCRIPTION = "Another Sweep"
PULSE_PERIOD_MS = 10
MANUAL_CONTROL = True

# Now the Sequences - they have to be built bottom-up:
#The basic idea is that for lists, Python interprets + as concatination, N* (or *N) as
# repeat N times. So start with single-element High and Low pulses.
H = [1]
L = [0]

#then just string them together, e.g. could be as simple as (H + 3*L) *2 -> [1, 0, 0, 0, 1, 0, 0, 0].
#Since there are two outputs, need to setup the two pulse trains with the same length.  Here's an example.
# the final lists (sweeps) must be called SWEEP_A and SWEEP_B


# start with some things we'll reuse:
N_BURST = 8             # number of pulses in a "burst".
IB_GAP = L * 25         # inter-burst gap

# First pulse train (A channel)
# My sample, atomic pulse is one Low interval, 3 high interval, 1 more low intervals.
# so that's 3 high in total of 5 sample periods (DT) so 60% duty cycle
atom_pulse1 = L + 3*H + L
burst1 = atom_pulse1 * N_BURST

# Now the first full pulse train is burst,gap repeated 3 times
# and assign the output
SWEEP_A = (burst1 + IB_GAP) * 3

# Now my second pulse train (B output)
# I'll syncronize a set of trigger pulses to fire in the middle burst.  My atomic pulse
# is has a 20% duty cycle
atom_pulse2 = L + H + 3*L
burst2 = atom_pulse2 * N_BURST

# but now I need a no_burst pause that's as long as the burst
no_burst2 = L * len(burst2)

# and just put them all together for the B channel output:
SWEEP_B = (no_burst2 + IB_GAP) + burst2 + IB_GAP + (no_burst2 + IB_GAP)

# this is just a statement to make it crap-out if lists are not the same length
assert len(SWEEP_A) == len(SWEEP_B), "Pulse definition error - two sequences must be the same length"

