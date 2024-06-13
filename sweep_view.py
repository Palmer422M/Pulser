"""
Python interpreter as pulse generator
M. Palmer, June 2, 2024
"""
from typing import List
import matplotlib.pyplot as plt
import numpy as np
import argparse
import importlib

from constants import DEFAULT_SWEEP_DEF_MODULE

TTL_V = 5.0 # on (1) to Volts for TTL signals
GRAPHICAL_EXPANSION_FACTOR = 10   # for graphical visualization purposes only

def expand_sequence_for_veiwing(seq : List) -> List:
    # expand sequence by replicating samples 10x.  Purely for graphical viewing.
    z = [[s]*GRAPHICAL_EXPANSION_FACTOR for s in seq] # expand
    return [item for items in z for item in items] # A bit of magic to flatten the list


def view_sequences(seq1: List, seq2: List, pp_ms: int, title: str):
    """
    Graph the two pulse-trains using standard MATPLOTLIB stuff.  Only trickery is in the waveform
    expansion stuff.
    """

    dt_s = pp_ms /1000.

    graphical_seq1 = expand_sequence_for_veiwing(seq1)
    graphical_seq2 = expand_sequence_for_veiwing(seq2)

    va = np.array(graphical_seq1) * TTL_V
    vb = np.array(graphical_seq2) * TTL_V

    t = np.arange(len(graphical_seq2)) * dt_s / GRAPHICAL_EXPANSION_FACTOR    # time sequence

    fig, (ax1, ax2) = plt.subplots(2,1)
    ax1.plot(t, va)
    ax1.set_ylabel('Output A (V)')
    ax2.plot(t, vb)
    ax2.set_ylabel('Output B (V)')
    ax2.set_xlabel('Time (s)')
    fig.suptitle(title)
    plt.show()

"""
Main Code
Here I use argparse to get the command line.  That allows varible number of arguments:
    > python pulse_view.py      # use default pulse-definition module
    > python pulse_view.py mypulse_def1     # use this pulse-definition module instead (mupulse_def1.py)
"""

parser = argparse.ArgumentParser(description='Display sweeps graphically')
parser.add_argument('module', nargs='?', default=DEFAULT_SWEEP_DEF_MODULE, help='Name of sweep definition module')
args = parser.parse_args()

"""
Only way to allow for run-time (variable) module loading (import) is to use python's importlib module.
"""

module = importlib.import_module(args.module)

title = args.module + ': ' + module.DESCRIPTION     # create a title for the graph from module name and it's doc-string

view_sequences(module.SWEEP_A, module.SWEEP_B, module.PULSE_PERIOD_MS, title)
