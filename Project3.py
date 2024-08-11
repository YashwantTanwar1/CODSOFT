import random
import string
while True:
    def password(length):
    
        
       characters = string.ascii_letters + string.digits + '@' + '#' + '&' + '*'
       print("Your pass is")
       return ''.join(random.choice(characters) for _ in range(length))
        

    length = int(input("Enter the length of the Password(0 for Exit): "))
    if (length == 0):
        break
    x = password(length)
    print(x)