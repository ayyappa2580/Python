# import sys
# from addition import  Addition
# from substration import Substration
# from mul import multiplication
# from div import division
# from exp import expontation
print("-"*50)
print("\t\t\t\tCALCULATOR")
print("-"*50)
# """Means multi line quotes
print("""\t1.ADDITION
\t2.SUBSCRATION
\t3.MULTIPLICATION
\t4.DIVISION
\t5.EXPONENTATION
\t6.EXIT""" )
print("-"*50)
while(True):
    ch=int(input("ENTER ANY ONE ABOVE THIS OPTIONS:"))
    match(ch):
                case 1:
                    print("Enter Two Values for Addition")
                    print("-" * 50)
                    a, b = float(input("Enter first Value:")), float(input(("Enter Second Value:")))
                    print("\tSUM({},{})={}".format(a, b, a + b))
                case 2:
                    print("Enter Two number for SUBSCRATION")
                    print("-" * 50)
                    a, b = float(input("Enter first Value:")), float(input("Enter Second Value:"))
                    print("\tSUB({},{})={}".format(a, b, a - b))
                case 3:
                    print("Enter Two number for MULTIPLICATION")
                    print("-" * 50)
                    a, b = float(input("Enter first Value :")), float(input("Enter Second Value:"))
                    print("\tMUL({},{})={}".format(a, b, a * b))
                case 4:
                    print("Enter Two Values for DIVISION")
                    print("-" * 50)
                    a, b = float(input("Enter first Value:")), float(input("Enter Second Value:"))
                    print("\tDIV({},{})={}".format(a, b, a / b))
                case 5:
                    print("Enter Two Values for.EXPONENTATION")
                    print("-" * 50)
                    a, b = float(input("Enter Base value:")), float(input("Enter Power Value:"))
                    print("Pow({},{})={}".format(a, b, a ** b))
                case 6:
                    print("Thanks for using this Program\n We will meet Next Time")
                case _:
                    print("Don't Enter Invalid Number plz try--again")
