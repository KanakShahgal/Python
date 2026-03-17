import re


def isvalid(num):
    pattern = re.compile('(0|91)?[-\s]?[6-9]\d{9}')
    return pattern.match(num)
num =input("Enter the numer:")
if isvalid(num):
    print("valid mobile numer")
else:
    print("Invalid mobile number")


