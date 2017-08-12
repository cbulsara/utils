#!/usr/bin/python2.7

import pandas as pd
import sys

#Define the column names that we want to keep and in what order
keep_cols = ['Computer_Name', 'Measure_Date', 
            'Pattern_Date', 'Operating_System', 'Client_Version',
            'Policy_Serial', 'HI_Status', 'Status',
            'Auto_Protect_On', 'Worst_Detection', 
            'Last_Scan_Time', 'Antivirus_engine_On',
            'Download_Insight_On', 'SONAR_On', 'Tamper_Protection_On',
            'Intrusion_Prevention_On', 'IE_Browser_Protection_On',
            'Firefox_Browser_Protection_On', 'Early_Launch_Antimalware_On',
             'Server_Name', 'MAC_Address1']

#-----------------------------------------------
#Main
#
#Iterate through CSVs passed on the command line
#and use pandas to keep the columns listed in 
#keep_cols.
#-----------------------------------------------

#Check arg count
if len(sys.argv) == 1:
    print "No args passed"
    quit()

#Loop through CSVs, keep only keep_cols, write to a _pruned.csv file
for i in sys.argv[1:]:
    f = pd.read_csv(i)
    s = i.split('.')
    filename = s[0] + "_pruned" + "." + s[1] 
    new_f = f[keep_cols]
    new_f.to_csv(filename, index=False)

