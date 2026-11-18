import re
import json
import math

temprature = 15
if temprature > 30:
    print("It's a hot day! \U0001F525")
elif temprature > 20:
    print("It's a nice day! \U0001F60A")
elif temprature > 10:
    print("It's a bit cold! \U0001F976")
print("done!")

number = 55.4
print(math.floor(number))
print(math.ceil(number))


# while True:

#     email = input("Enter email: ")
#     
#     pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#     #regular expression pattern to validate email format
#     
#     if re.match(pattern, email):
#         break
#     else:
#         print("Invalid email format \U0001f600")
# # while loop to validate the email format and prompt the user until a valid email is entered


# print(f"Your email is  {email}! \U0001F606")