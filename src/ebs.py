print("-------- ELECTRICITY BILLING SYSTEM --------")

print("---- way to check your bill -----")

print("""
--> 1.user_login
--> 2.customer_details
--> 3.customer_payment
--> 4.exit""")

#------main menu-----#

def menu():
    z='y'
    while (z=='y'):
        step=int(input("enter the choice from 1 to 3 one by one"))

        if step==1:
            user()
        elif step==2:
            customer()
        elif step==3 :
            payment()
        else:
            break
print("\n")

        
#--------user login and user details updation--------#    

def user():
    import mysql.connector as a
    try:
        conn=a.connect(host="localhost",user="root",passwd="learn",database="ebbooking")
        cursor=conn.cursor()
        username= input("enter the username")
        admin_no= int(input("enter your admin number"))
        password=input("enter the password")
        a="insert into admin(username,admin_no,password) values('{}',{},'{}')"
        cursor.execute(a.format(username,admin_no,password))
        conn.commit()
        
        print("your user details are:")
        print("your username:",username)
        print("your admin number:",admin_no)
        print("your password:",password)
        print("\n")

        print("your details confirmed!")
        print("\n")
        c=int(input("type 1 to continue"))
        if c==1 :
            print("will be continued")
        else:
            print("want to change?")
            print("\n")
            x=int(input("enter 1 to change"))
            if x==1:
                user_name=input("enter the username to be deleted")
                adminno=int(input("enter the admin number to be deleted"))
                b="delete from admin where admin_no={}"
                cursor.execute(b.format(adminno))
                conn.commit()

        print("successfully completed user login")
        print("\n")
        print("any changes?...if changed successfully uploaded :)")
        print("\n")
    except:
        print("Error:unable to upload")


#----------customer address and bill checking----------#
    
def customer():
    import mysql.connector as a
    conn=a.connect(host="localhost",user="root",passwd="learn",database="ebbooking")
    cursor=conn.cursor()
        
    
    print("---here comes customer bill---")
    print("1.verify your address")
    print("2.verify your bill")
    print("3.payment of your bill")
    print("---- kindly check your address---")
    print("\n")
    
    meterno=int(input("enter your admin number"))
    c="select * from customer where meter_no={}"
    cursor.execute(c.format(meterno))
    
    for x in cursor:
        print('meter_no:',x[0])
        print('name:',x[1])
        print('address:',x[2])
        print('phone number:',x[3])

    print("\n")
    print("is your details correct or need to change")
    print("\n")
    d=input("if yes click 1")
    if d==1:
        pass
    if d!=1:
        print("what you need to change?")
        print("1.name")
        print("2.addess")
        print("3.phone number")
        print("4.password")
        print("\n")
        g=int(input("enter number of options to be updated"))
        print("\n")
        for x in (0,g):
        
            e=int(input("enter the number to which you need to change"))
            print("\n")
            if e==1:
                new_name=input("enter the new name")
                f="update customer set name='{}' where meter_no={}"
                cursor.execute(f.format(new_name,meterno))
                conn.commit()
            elif e==2:
                new_address=input("enter the new address")
                f="update customer set address='{}' where meter_no={}"
                cursor.execute(f.format(new_address,meterno))
                conn.commit()
            elif e==3:
                new_phonenum=int(input("enter the new phone number"))
                f="update customer set phone={} where meter_no={}"
                cursor.execute(f.format(new_phonenum,meterno))
                conn.commit()
            elif e==4:
                new_password=input("enter the new password")
                f="update customer set password='{}' where meter_no={}"
                cursor.execute(f.format(new_password,meterno))
                conn.commit()
            else:
                print("refer options correctly")

    print("\n")            
    print("updated your details")
    print("\n")
    print("---for your reference below---")
    c="select * from customer where meter_no={}"
    cursor.execute(c.format(meterno))
    
    for x in cursor:
        print('meter_no:',x[0])
        print('name:',x[1])
        print('address:',x[2])
        print('phone number:',x[3])
        print('password:',x[4])
    print("\n")
            
#--------customer bill payment and reviewing---------#


def payment():
    from datetime import datetime
    
    current_date = datetime.now().date()

    import mysql.connector as a
    conn=a.connect(host="localhost",user="root",passwd="learn",database="ebbooking")
    cursor=conn.cursor()

    print("---here comes your bill payment---")
    print("\n")
    print("1.view your bill")
    print("2.make transaction according to your assigned bill")
    print("\n")
    
    meterno=int(input("enter your meter number/admin number"))
    c="select * from bill where meter_no={}"
    cursor.execute(c.format(meterno))

    for x in cursor:
        print('meter_no:',x[1])
        print('bill_id:',x[0])
        print('units this month:',x[2])
        print('total bill:',int(x[3]))
        print('status:',x[4])
        print('bill date:',x[5])
        
    print("\n")
    print("--- do you wish to pay now--- ")
    print("\n")
    i=int(input("enter 1 if yes"))
    if i==1:
        print("\n")
        print("---payment---")
        
        cost=int(input("enter the cost of your bill"))
        print("\n")
        real_cost=int(x[3])
        if real_cost==cost:
            print('successfully paid')
            print("\n")
            print('thank you')
            k="update bill set status='paid' where meter_no={}"
            cursor.execute(k.format(meterno))
            conn.commit()
            print("---- thank you for the payment---")
            print("\n")
            print("kindly check your status now of your bill this month")
            print("\n")
            print('bill number :',meterno)
            print('your cost:',real_cost)
            print('status',x[4])
            print('paid date', current_date)
            print('enter 4 to quit')

        else:
            j=real_cost-cost
            if j < 0:
                j= cost-real_cost
                print("you have paid extra",j)
                print("\n")
                print("you will receive your cash back")
                k="update bill set status='paid' where meter_no={}"
                cursor.execute(k.format(meterno))
                conn.commit()
                print("---- thank you for the payment---")
                print("\n")
                print("kindly check your status now of your bill this month")
                print("\n")
                print('bill number :',meterno)
                print('your cost:',real_cost)
                print('status',x[4])
                print('paid date', current_date)
                print('enter 4 to quit')

            else:
                print("you have paid less",j)
                print("\n")
                print("pay it soon")
                
    
    
                
    else:
        print("\n")
        print("pay it soon ")
        


menu()

    

    
    
    




    
    
    
    
    
