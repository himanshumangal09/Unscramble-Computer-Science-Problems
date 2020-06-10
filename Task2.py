"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
dictionary = {}
maxDuration =0
for i in range(len(calls)):
    if calls[i][0] in dictionary.keys():
        dictionary[calls[i][0]] += int(calls[i][-1])
    else:
        dictionary[calls[i][0]] = int(calls[i][-1])
    if calls[i][1] in dictionary.keys():
        dictionary[calls[i][1]] += int(calls[i][-1])
    else:
        dictionary[calls[i][1]] = int(calls[i][-1])


for number in dictionary:
    if maxDuration < dictionary[number]:
        maxDuration = dictionary[number]
        maxDurationNumber = number

print("%s spent the longest time, %d seconds, on the phone during September 2016." %(maxDurationNumber, maxDuration))

