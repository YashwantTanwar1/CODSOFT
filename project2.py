def Calculator():
    while True:
        a =float(input("Enter First Number "))
        b =float(input("Enter second Number "))
        operation = int(input('''What do you want to\nEnter\n1 for Addition \n2 for Subtraction \n3 for  Multiplication \n4 for division \n0 for Exit the code\n'''))

        if (operation == 0):
                print("Thank you for using my calculator")
                break
        elif(operation==1):
            print(f"{a} + {b} = {a+b}")
        elif(operation==2):
            print(f"{a} - {b} = {a-b}")
        elif(operation==3):
            print(f"{a} X {b }= {a*b}")
        elif(operation==4):
            print(f"{a} / {b} = {a/b}")
        else:
            print("Read above paragraph carefully & Then enter the value")      

Calculator()