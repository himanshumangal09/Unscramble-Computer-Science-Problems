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
"""
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

landline_numbers = []
for num in unique_numbers:
    if str(num)[0] == '(':
        landline_numbers.append(num)
        
mobile_numbers = []
for num in unique_numbers:
    if str(num)[0] == '7' or str(num)[0] == '8' or str(num)[0] == '9':
        mobile_numbers.append(num)

codes = []
for m_num in mobile_numbers:
    if m_num[:4] not in codes:
        codes.append(m_num[:4])
        
for l_num in landline_numbers:
    if l_num.split(")")[0][1:] not in codes:
        codes.append(l_num.split(")")[0][1:])
    

print("The numbers called by people in Bangalore have codes:")
#print(sorted(codes))
for code in sorted(codes):
    print(code)

    
"""

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

fixed_lines_to_bangalore = []
fixed_lines_from_bangalore = []

for call in calls:
    if call[0][:5] == "(080)":
        fixed_lines_to_bangalore.append(call[0][0])
        #print(call[0][:5])
        
    if call[1][:5] == "(080)":
        fixed_lines_from_bangalore.append(call[1][0])
        #print(call[1][:5])
percentage = round(len(fixed_lines_from_bangalore) / len(fixed_lines_to_bangalore) * 100 ,2)
print(percentage,"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

