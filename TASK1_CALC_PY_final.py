print("AKSHAT SHARMA- CALCULATOR")
a=float(input("Enter 1st no. = "))
b=float(input("Enter 2nd no. = "))
def fac(r):
    x=1
    for i in range(1,r+1):
        x=x*i
    return x
def sin(c):
    j=0
    for i in range(0,6):
        j+=((((-1)**i)*((c)**((2*i)+1))))/(fac(2*i+1))
    return j
def cos(c):
    t=(1-((sin(c))**2))**(0.5)
    return t
def tan(c):
    return ((sin(c)/cos(c)))
while True:
    t=input("Enter any operation from : +,-,*,**,/,//,%,sin,cos,tan,exp : \t")
    if t=="+":
        print("SUM =",a+b)
    elif t=="-":
        print("DIFF. =",a-b)
    elif t=="*":
        print("PRODUCT =",a*b)
    elif t=="/":
        print("QUOTIENT =",a/b)
    elif t=="//":
        print("FLOOR DIVISION =",a//b)
    elif t=="**":
        print("EXPONENTIATION =",a**b)
    elif t=="%":
        print("REMAINDER =",a%b)
    elif t=="sin":
        c=float(input("Enter argument in rads. : "))
        print('sin(',c,') = ',sin(c))
    elif t=="cos":
        c=float(input("Enter argument in rads. : "))
        print('cos(',c,') = ',cos(c))
    elif t=="tan":
        c=float(input("Enter argument in rads. : "))
        print('tan(',c,') = ',tan(c))
    elif t=="exp":
        p=float(input("enter power"))
        print("value is = ",((2.71828)**p))
    else:
        print("ERROR! PLEASE ENTER CORRECT CHARACTER!")
    ch=input("Enter 'y'-yes or 'n'-no , to continue : ")
    if ch=="n":
        print()
        print("THANK YOU !")
        print("TASK1 COMPLETED: CALCULATOR @11-11-2022")
        break
