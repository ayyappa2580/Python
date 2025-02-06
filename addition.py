def Addition():
    print("Enter Two Values for Addition")
    print("-" * 50)
    a, b = float(input("Enter first Value:")), float(input(("Enter Second Value:")))
    print("\tSUM({},{})={}".format(a, b, a + b))

Addition()