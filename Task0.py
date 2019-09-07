"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    rownText = texts[0]

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    rownCalls = calls[-1]

    print("First record of texts,", rownText[0],"texts", rownText[1], "at time",rownText[2])
    print("Last record of calls,",rownCalls[0] ,"calls", rownCalls[1],"at time", rownCalls[2]+",","lasting", rownCalls[3],"seconds")
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

