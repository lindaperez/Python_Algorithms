"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    hm = {}
    countEE=0
    totalCalls = 0
    for rowCall in calls:
        incoming = rowCall[0]
        ans = rowCall[1]
        first = ans[:1]
        three = ans[:3]
        eight = incoming[1:4]
        if  first == "(":
            answered = ans[1:].split(')')[0]
        elif three== "140":
            answered=three
        elif first == "7" or first == "8" or first == "9":
            answered= ans[:4]
        else:
            answered=ans
        if eight=="080" and answered[:3]=="080":
            countEE+=1
        if eight =="080":
            totalCalls += 1
            if eight not in hm:
                hm[eight]={answered}
            else:
                if answered not in hm[eight]:
                    hm[eight].add(answered)
    ##output
    print("The numbers called by people in Bangalore have codes:")
    for sol in hm:
        for sal in sorted(hm[sol]):
            print(sal)
    print('%.2f' % ((countEE*100)/totalCalls),"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
