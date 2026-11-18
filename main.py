import re
import json
import math


json_string = '''
{
    "name": "Jane Doe",
    "age": 33,
    "full-time": true
}'''

data = json.loads(json_string)
new_json = json.dumps(data, indent=3) #content of list gets indented 
print(new_json) #prints the JSON data in a formatted way

data['test'] = True

def greet():
    print(f"Hello! Welcome to the program.") 
    print('* * * * * * | * * * * * * | * * * * * * |')

greet()
#this function greets the user when the program starts

unique = {4,6,7,7,9,0}
# does not show duplicates, only unique values are stored in a set
print(unique)

year: int = 2028
money: float = 101.61

result = year*money



print(f"Year: {year}, Money: {money}, Result: {result}")