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
    print(f"Hello! {data['name']} Welcome to the program.") 
    print('* * * * * * | * * * * * * | * * * * * * |')

greet()
#this function greets the user when the program starts

number = 55.4
print(math.floor(number))
print(math.ceil(number))


while True:

    email = input("Enter email: ")
    
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    #regular expression pattern to validate email format
    
    if re.match(pattern, email):
        break
    else:
        print("Invalid email format")
# while loop to validate the email format and prompt the user until a valid email is entered


print(f"Your email is {email}!")