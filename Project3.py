import random
import string

def password(length):
    while True:
       if (length == 0):
        return "thank you"
        break 
       characters = string.ascii_letters + string.digits + '@' + '#' + '&' + '*'
       print("Your pass is")
       return ''.join(random.choice(characters) for _ in range(length))
        

length = int(input("Enter the length of the Password(0 for Exit): "))
x = password(length)
print(x)