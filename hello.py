import re

message1 = 'Hello, World!'
for i in range(5):
    print(message1)


name = input("Enter your name: ")
print(name)


while True:
    
   
    email = input("Enter email: ")
    
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    #regular expression pattern to validate email format
    
    if re.match(pattern, email):
        break
    else:
        print("Invalid email format")

print(f"Your email is {email}!")