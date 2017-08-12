#!/usr/bin/python2.7

import sys
import pandas as pd

if len(sys.argv) == 1:
    print "No args passed"
    quit()

col = raw_input("Enter name of date column to be pruned down to MM/DD/YYYY: ")

for i in sys.argv[1:]:
    df = pd.read_csv(i)
    df[col].replace('Never', '', inplace=True)
    df[col] = df[col].map(lambda x: str(x).split(" ")[0])
    df.to_csv(i, index=False)