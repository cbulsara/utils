#!/usr/bin/python2.7

import sys
import pandas as pd

if len(sys.argv) == 1:
    print "No args passed"
    quit()

for i in sys.argv[1:]:
    measure_date = raw_input("Enter measurement date as MM/DD/YYYY: ")
    df = pd.read_csv(i)
    df.insert(0, 'Measure_Date', measure_date)
    df.to_csv(i, index=False)