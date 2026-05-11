"""Reference script for the Week 5 Part 1 group walkthrough.

Builds on csv_walkthrough_test.py (Week 4 Part 1). The new bits:
- import sys; read sys.argv for a run-time argument
- check len(sys.argv) and exit cleanly with a usage message if missing
- convert the string arg to int
- replace the fixed-iteration counter loop with a time-based loop

As with Week 4, this is the end-state of the live walkthrough — students type
it out as the instructor walks through it. Kept here for future instructors
who didn't run the original walkthrough themselves.

Run on a laptop, e.g.:
    python csv_walkthrough_with_args.py 30
to write 30 seconds of stand-in data to test_data.csv.
"""
import csv
import sys
import time

import numpy as np


# Check that the user actually passed a run-time argument
if len(sys.argv) < 2:
    print("Usage: python csv_walkthrough_with_args.py <runtime_seconds>")
    sys.exit(1)

# Command-line arguments arrive as strings; convert to int
runtime = int(sys.argv[1])

# Open the CSV file the same way as last week
file = open("test_data.csv", "w", newline="")
writer = csv.writer(file, delimiter=",")
writer.writerow(["Time", "data"])

# Time-based loop instead of counter-based: stop after runtime seconds
start = time.time()
while time.time() - start < runtime:
    data = np.random.random()      # random float in [0, 1) as stand-in sensor data
    itime = time.time()             # Unix timestamp (seconds since 1970)
    writer.writerow([itime, data])
    time.sleep(1)

file.close()
