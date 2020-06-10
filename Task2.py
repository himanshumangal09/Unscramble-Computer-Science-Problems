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

def longestcalls(calls):
    long_call = calls[0][3]
    incoming_num = calls[0][0]
    for call in calls:
        if int(call[3])>int(long_call):
            long_call = call[3]
            incoming_num = call[0]
    return incoming_num,long_call
#print("Last record of calls,",calls[-1][0],"calls", calls[-1][1],"at time ",calls[-1][2],"lasting", calls[-1][3],"seconds")
telephone_num = 0
duration = 0
telephone_num,duration = longestcalls(calls)
print(telephone_num," spent the longest time,",duration,"seconds, on the phone during September 2016.")




