"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import operator
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    rowTexts = texts[0]
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    #phone:timeCall
    timeCall = {}
    for rowCall in calls:
        phone_number_0=rowCall[0]
        phone_number_1=rowCall[1]
        time = int(rowCall[3])
        date = rowCall[2]
        if phone_number_0 not in timeCall:
            timeCall[phone_number_0]=time
        else:
            timeCall[phone_number_0] += time

        if phone_number_1 not in timeCall:
            timeCall[phone_number_1]=time
        else:
            timeCall[phone_number_1] += time
    maxElem=max(timeCall.items(), key=operator.itemgetter(1))[0]
    maxTime = timeCall[maxElem]
    print(maxElem,"spent the longest time,", maxTime, "seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""