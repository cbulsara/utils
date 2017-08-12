#!/usr/bin/python2.7
import csv
import sys
import pandas as pd

acceptable_inputs = ['text', 'keyword', 'long', 'integer',
                        'short', 'byte', 'double', 'float',
                        'date', 'boolean', 'binary',
                        'integer_range', 'float_range',
                        'double_range', 'date_range',
                        'object', 'nested', 'geo_point',
                        'geo_shape', 'ip', 'completion',
                        'token_count', 'murmur3', 'mapper-attachments']

preamble = """{
                "mappings": {
                  "logs": {
                    "properties": {
                     "@timestamp": {
                      "type": "date",
                      "format": "basic_date"
                     },
                     "@version": {
                       "type": "string"    
                     },
"""

def writeIndex(headers, types):
    outbuffer = []
    outbuffer.append("{")
    outbuffer.append("\t" + '"mappings": {')
    outbuffer.append("\t\t" + '"logs": {')
    outbuffer.append("\t\t\t" + '"properties": {')
    outbuffer.append("\t\t\t\t" + '"@timestamp": {')
    outbuffer.append("\t\t\t\t\t" + '"type": "date",')
    outbuffer.append("\t\t\t\t\t" + '"format": "basic_date"')
    outbuffer.append("\t\t\t\t" + "},")
    outbuffer.append("\t\t\t\t" + '"@version": {')
    outbuffer.append("\t\t\t\t\t" + '"type": "string"')
    outbuffer.append("\t\t\t\t" + '},')


    for h, t in zip(headers,types):
        outbuffer.append("\t\t\t\t" + '"' + h + '"' + ": {")
        outbuffer.append("\t\t\t\t\t" + '"type":' + ' "' + t + '"')
        outbuffer.append("\t\t\t\t" + "},")
    outbuffer[-1] = outbuffer[-1].replace(",", "")

    outbuffer.append("\t\t\t" + '}')
    outbuffer.append("\t\t" + '}')
    outbuffer.append("\t" + '}')
    outbuffer.append('}')

    textfile = open("outbuffer.txt", 'wb')
    for s in outbuffer:
        textfile.write(s + "\n")
    textfile.close()

if len(sys.argv) == 1:
    print "No args passed"
    quit()

for i in sys.argv[1:]:
    print preamble
    headersout = []
    typesout = []

    f = pd.read_csv(i)
    headersout = list(f)
    print("Please enter the desired data type for each column.")
    print acceptable_inputs
    for h in list(f):
        while True:
            column_type = raw_input("Enter data type of " + h + ": ")
            try:
                column_type = column_type.lower()
            except ValueError:
                continue
            if column_type in acceptable_inputs:
                typesout.append(column_type)
                break
            else:
                print("Invalid Entry")
    
    writeIndex(headersout,typesout)
    filename =  i.split(".")[0] + "_headers.csv"
    with open(filename, 'wb') as csvfile:
        w = csv.writer(csvfile, quoting=csv.QUOTE_ALL, quotechar='"')
        w.writerow(headersout)
        w.writerow(typesout)









#    with open(i, 'rb') as csvfile:
#        c = csv.reader(csvfile)
#        r = c.next()
#        headersout.append(r)
#        print headersout
        
# with open("results.csv", 'wb') as csvfile:
#    w = csv.writer(csvfile, quoting=csv.QUOTE_ALL, quotechar='"')
#    for r in headersout:
#        print r
#        w.writerow(r)



