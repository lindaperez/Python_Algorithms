"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    ph_nums = {}
    for rowText in texts:
        for elem in rowText[:2]:
            if  elem not in ph_nums:
                ph_nums[elem]=1
            else:
                ph_nums[elem]+=1
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for rowCall in calls:
        for elem in rowCall[:2]:
            if elem not in ph_nums:
                ph_nums[elem] = 1
            else:
                ph_nums[elem] += 1

    counts = len(ph_nums)
    print("There are",counts,"different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
