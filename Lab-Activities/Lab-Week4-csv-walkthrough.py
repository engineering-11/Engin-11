"""Reference script for the Week 4 Part 1 group walkthrough.

This is what the live-coded walkthrough script ends up looking like. The lab
handout (Lab Activity Week 4.docx, Part 1) deliberately doesn't include this
verbatim — students type it out as the instructor walks through it, with
explanatory commentary at each step. Kept here for future instructors who
didn't run the original walkthrough themselves.

Run on a laptop (no Pi, no sensor needed). Produces test_data.csv in the
working directory with 10 rows of (timestamp, random number).
"""
import csv
import time

import numpy as np


# Open a file for writing. "w" makes it writeable; newline="" prevents the csv
# module from inserting blank lines between rows on Windows.
file = open("test_data.csv", "w", newline="")

# Wrap the open file with a csv.writer. The default delimiter is "," already —
# we pass it explicitly so students see that the option exists.
writer = csv.writer(file, delimiter=",")

# Header row. Pandas expects this when reading the file later.
writer.writerow(["Time", "data"])

# Generate 10 stand-in readings, one per second.
nentries = 10
counter = 0
while counter < nentries:
    data = np.random.random()      # random float in [0, 1) as stand-in sensor data
    itime = time.time()             # Unix timestamp (seconds since 1970)
    writer.writerow([itime, data])
    time.sleep(1)
    counter += 1

# Close the file so the last writes are flushed to disk.
file.close()
