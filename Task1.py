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


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# ,calls[-1][0],"calls", calls[-1][1],
# ,texts[0][0]," texts", texts[0][1] ,

unique_numbers = []
for call  in calls:
    if call[0] not in unique_numbers:
        unique_numbers.append(call[0])
    if call[1] not in unique_numbers:
        unique_numbers.append(call[0])
for text in texts:
    if text[0] not in unique_numbers:
        unique_numbers.append(text[0])
    if text[1] not in unique_numbers:
        unique_numbers.append(text[0])

# print("Unique numbers")
# print(len(unique_numbers))

# print("numbers of calls ")
# print(len(calls))

# print("number of texts")
# print(len(texts))

print("There are", len(unique_numbers) ,"different telephone numbers in the records.")
    

