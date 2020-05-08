#trip
'''
def trip(mil,cost,dist):

    x=2*(cost*dist/mil)/4
    print(x)
    if(x%5==0):
        return True
    else:
        return False
mil,cost,dist=float(input("enter the mileage of vehicle:")),float(input("enter the cost for fuel:")),float(input("enter the distance travelled:"))
trip(mil,cost,dist)'''
#loan
'''
def loan(t,r,p):
    intr=(p*t*r)/100
    print("The interest for loan is ",intr)
t,r,p=float(input("enter time period:")),float(input("enter rate of interest:")),float(input("enter principle amount:"))
loan(t,r,p)'''
#armstrong
'''
def armstrong():
    num=int(input("enter a number:"))
    k=len(str(num))
    arm=0
    pres=num
    while(pres>0):
        x=pres%10
        arm=arm+(x**k)
        pres=pres//10
    if(num==arm):
        print(num,"is armstrong number")
    else:
        print(num,"is not armstrong number")
armstrong()'''
#marks
'''
def jitu(arts,engg):
    if(arts>=90 and arts%2!=0):
        print("eligible for the highest scholarship of 50%")
    elif(arts>=90):
        print("eligible for 50% scholarship")
    elif(arts%2!=0):
        print("eligible for 5% scholarship")
    else:
        print("not eligible for scholarship")
    if(engg>85):
        print("eligible for 50% scholarship")
    elif(engg%7==0):
        print("eligible for 5% scholarship")
    else:
        print("not eligible for scholarship")
arts,engg=int(input("enter your arts score:")),int(input("enter your engineering score:"))
jitu(arts,engg)'''



    


    
    
    
