#Apollo bill Generating by python program?
while(True):
    import sys
    print("-"*50)
    print("""\t\t\t\tAPOLLO HOSPITALS
    \t\topposite IMB,1/151, SR NAGAR,
    \t\tHYDERABAD-500095(India)
    Tel:(+91) 8080080837/26604356 FAC-+(91)804148772""")
    print("\t-------------------------------------------------")
    print("""\t\t\t\tMedical bill Receipt
    ------------------------------------------------
    1.Building information
    2.Hospital/clinic Information
    3.patient information
    4.Top Doctors Are there my Hospital Only
    5.Medical services and Charges
    6.Payment Information
    7.Exit To Home""")
    print("-"*50)
    ch = int(input("ENTER YOUR CHOICE:"))
    print("-"*50)
    match ch:
        case 1:
            print("invoice number:\t 1092029")
            input(print("[DD-MM-YY]"))
            input(print("Due Date:[DD-MM-YY]"))
        case 2:
             input(print("patient name:"))
             print("Hospital reg-998299282:")
             print("Patient Doctor Name is [Vinay]")
             print("Email ID:apollo@gmail.com")
        case 3:
            input(print("patient name:"))
            input(print("Address:"))
            input(print("Phone Number:"))
            input(print("Alternative Numbers:"))
            input(print("Email id:"))
        case 4:
            print("1.DR RAVI \n \tspecialist-(Obstetrics and gynecology)")
            print("2.DR Rohan\n \t specialist-(Gynecologist)")
            print("3.DR Rudra\n \t specialist-(Psychiatrist)")
            print("4.DR Sathwik\n \t specialist-(General practitioner)")
            print("5.DR Ayyappa\n \t specialist-(Neurologist)")
        case 5:
            print("1.Emergency Cases charge Amount of 180$")
            print("2.Ambulance Free of cost")
            print("3.cleaning Charges 50$")
            print("4.Only buy Medicines are My Shop Only ")
        case 6:
            print("Phone pay & G-pay & paytm Accept Here [+91 9902282764]")
            print("Account No:711411099817")
            print("IFSC CODE-UNIBOCG117")
            print("Account Holder Name:Apollo")
        case 7:
            print("Thanks for using this program!")
        case _:
            print("Your option is Incorrect plz--try Again")











# line number 57 is a default case
# iam also using multiline string notations in this program

