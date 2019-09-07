"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    callers = set()
    noOthers = set()

    for rowText in texts:
        sendText = rowText[0]
        recText = rowText[1]
        if sendText not in noOthers:
            noOthers.add(sendText)
        if recText not in noOthers:
            noOthers.add(recText)

    for rowCall in calls:
        incoming = rowCall[0]
        answered = rowCall[1]
        if incoming not in callers:
            callers.add(incoming)
        if answered not in noOthers:
            noOthers.add(answered)
    print("These numbers could be telemarketers: ")
    for call in sorted(callers):
        if call not in noOthers:
            print(call)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
