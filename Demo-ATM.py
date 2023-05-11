#####           PIN Digit Limit         #####
def DigitCount(i):
    global k
    k = 0
    while(i!=0):
        num = i//10
        k = k+1
        i = num
    return k

#####            Log-in Page Function             #####
def Log_in_Page():
    pw = open("password.txt", "r")
    Password = pw.read()
    pw.close()
    u = input("Enter Username : ")
    p = input("Enter Password : ")
    if(u!=Username or p!=Password):
        if(u!=Username):
            print("Username is not correct")
            Log_in_Page()
        else:
            print("Password is Wrong")
            Log_in_Page()
    else:
        Home_Page()


#####           Home Page Function             #####
def Home_Page():
    try:
        print("1. Check Balance\n2. PIN Change\n3. Withdrawn\n4. Credit\n5. Statements\n6. Change Password\n7. Log Out")
        a = int(input("Choose Option from Above List : "))
        if(a==1):
            Check_Balance_Page()
        elif(a==2):
            PIN_Change_Page()
        elif(a==3):
            Withdrawn_Page()
        elif(a==4):
            Credit_Page()
        elif(a==5):
            f = open("Statements.txt", "r")
            print(f.read())
            Common()
        elif(a==6):
            Pass_Page()
        elif(a==7):
            print("Logged Out Successfully")
            exit
        else:
            print("Invalid Input")
            Home_Page()
    except Exception as e:
        print(e)
        Home_Page()

#####           Check Balance Page Function           #####
def Check_Balance_Page():
    global Balance
    b = open("Balance.txt", "r")
    Balance = b.read()
    print("Balance : ", Balance)
    b.close()
    Common()
#####           PIN Change Function             #####
def PIN_Change_Page():
    global PIN
    p = open("PIN.txt", "r")
    PIN = p.read()
    p.close()
    old = int(input("Enter PIN : "))
    if(old==int(PIN)):
        new = int(input("Enter New PIN : "))
        if(old==new):
            print("You Cann't Choose Existing PIN Again")
            Home_Page()
        else:
            DigitCount(new)
            if(k==4):
                renew = int(input("ReEnter PIN : "))
                if(new==renew):
                    with open("PIN.txt", "w") as z:
                        P = str(new)
                        z.write(P)
                    print("PIN Has Been Changed, Please Login Again")
                    Log_in_Page()
                else:
                    print("New PIN not Matched")
                    Invalid_Input_PIN()
            else:
                print("PIN must be 4 Digits")
                Invalid_Input_PIN()
    else:
        print("Wrong PIN, Please Try Again\nIf You Forgot Your Password\nPlease Visit Your Bank Branch")
        Invalid_Input_PIN()

#####           Invalid Input in PIN Change Function            #####
def Invalid_Input_PIN():
    print("1. Home Page\n2. Try Again")
    c = int(input("Choose Option : "))
    if(c==1):
        Home_Page()
    elif(c==2):    
        PIN_Change_Page()
    else:
        print("Enter Valid Input")
        Invalid_Input_PIN()

#####               Common Page Function            #####
def Common():
    print("1. Home Page\n2. Log Out")
    x = int(input("Choose Option : "))
    if(x==1):
        Home_Page()
    elif(x==2):
        print("Thanks For Using Our Service\nLogged Out Successfully")
        exit
    else:
        print("Enter Valid Input")
        Common()

#####               Withdrawn Page Function             #####
def Withdrawn_Page():
    global w
    w = int(input("Amount to be Withdrawn : "))
    with open("PIN.txt", "r") as z:
        PIN = z.read()
    if(w>=100 and w<=int(Balance)):
        ps = int(input("Enter PIN : "))
        if(ps==int(PIN)):
            print(w,"Rupees to be Withdrawn")
            print("1. Confirm\n2. Cancle")
            y = int(input("Choose Option : "))
            if(y==1):
                with open("Balance.txt", "w") as b:
                    B = int(Balance) - w
                    b.write(str(B))
                print("Withdrawn is Successful")
                Debit_Statement_Page()
                Common()
            elif(y==2):
                print("Transaction Cancelled")
                Home_Page()
            else:
                print("Transaction Failed")
                Home_Page()
        else:
            print("Wrong PIN")
            Home_Page()
    elif(w<100):
        print("Minimum Transaction is 100")
        Home_Page()
    else:
        print("Not Sufficient Amount\nAvaliable Amount : ", Balance)
        Home_Page()

#####           Credit Page Function              #####
def Credit_Page():
    global c
    with open("PIN.txt", "r") as z:
        PIN = z.read()
    c = int(input("Enter Amount : "))
    if(c>=100 and c<=10000):
        pa = int(input("Enter PIN : "))
        if(pa==int(PIN)):
            print(c,"Rupees to be credited !")
            print("1. Confirm\n2. Cancle")
            a = int(input("Choose Option : "))
            if(a==1):
                with open("Balance.txt", "w") as b:
                    B = int(Balance) + c
                    b.write(str(B))
                print("Balance Updated Successfully")
                Credit_Statement_Page()
                Common()
            elif(a==2):
                print("Transaction Cancelled")
                Home_Page()
            else:
                print("Transaction Failed")
                Home_Page()
        else:
            print("Wrong PIN")
            Home_Page()
    elif(c<100):
        print("Minimum Transaction Amount is 100")
        Home_Page()
    else:
        print("You can Credit upto 10000 by this Machine\nFor Large Amount,Please Visit Bank")
        Home_Page()

#####           Statements Page Function            #####
def Credit_Statement_Page():
    with open("Statements.txt", "a") as f:
        a = str(now)
        cr = str(c)
        f.write(f"\nCredited TX-00{a} : +{cr}")

def Debit_Statement_Page():
    with open("Statements.txt", "a") as f:
        b = str(now)
        db = str(w)
        f.write(f"\nDebited TX-00{b} : -{db}")

#####           Password Change Page Function           #####
def Pass_Page():
    global Password
    with open("password.txt", "r") as pw:
        Password = pw.read()
    old = input("Enter Password : ")
    if(old==Password):
        new = input("Enter New Password : ")
        if(old==new):
            print("You Cann't Choose Existing Password Again")
            Home_Page()
        else:
            if(len(new)>=4 and len(new)<=10):
                renew = input("ReEnter Password : ")
                if(new==renew):
                    with open("password.txt", "w") as psw:
                        psw.write(new)
                    print("Password Has Been Changed, Please Login Again")
                    Log_in_Page()
                else:
                    print("New Password not Matched")
                    Home_Page()
            else:
                print("Password Strength must be 4 to 10 Characters")
                Home_Page()
    else:
        print("Wrong Password, Please Try Again\nIf You Forgot Your Password\nPlease Visit Your Bank Branch")
        Home_Page()

#####           Main Program Code           #####
from datetime import datetime
now = datetime.now()
WelcomePage = "Welcome To The Test Bank"
print(WelcomePage.center(100))
Username = "User1"
Log_in_Page()
