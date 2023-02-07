import re

with open('./regex_test.txt') as data:
    names = data.readlines()

for name in names:
    found = re.match(r'[A-Za-z]+[" "][A-Z][- a-zA-Z]+',name)
    if found: 
        print(found[0])
    else:
        print("None")