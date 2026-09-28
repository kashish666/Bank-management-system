import mysql.connector
from decimal import Decimal 
from datetime import datetime
class BankingApp:
    def __init__(self):
         self.customer_id=None
         self.current_user=None
    def run (self):
        while True:
            if not self.current_user:
               print("\n=============")
               print("\nBANKING SYSTEM ")
               print("---------------------")
               print("-----MAIN MENU----------")
               print("1.CUSTOMER REGISTRATION")
               print("2.CUSTOMER LOGIN")
               print("3.ADMIN LOGIN ")
               print("4.EXIT")
               choice=input("select an option (1-4):").strip()
               if choice=='1':
                    self.registration()
               elif choice=='2':
                     self.login() 
               elif choice=='3':
                 pwd=input("Enter Admin Password: ").strip().lower()
                 if pwd=="admin123":
                   self.Admin_login()
                 else:
                     print("Wrong Password ")  

                   
            else:
                print(f"\n------------------------")
                print("1.My Profile")
                print("2.My Accounts")
                print("3.Deposite Money")
                print("4.Withdraw Money") 
                print("5.Transfer Money")
                print("6.Account Statement")
                print("7.Beneficiaries ")
                print("8. Loans")
                print("9.Change password")
                print("10.LOGOUT")
               
                print("-------------------------------------------")  
               
                choice=input ("Select an option :").strip()    
                if choice=='1':
                    self.My_profile()
                elif choice=='2':
                    self.My_account()
                elif choice=='3':
                    self. Deposite_money()   
                elif choice=='4':
                    self.Withdraw_money()   
                elif choice=='5':
                    self.Transfer_money()
                elif choice=='6':
                    self.Bank_Statement()      
                elif choice =='7':
                    self.beneficiary()  
                elif choice == '8':
                    self.Loans()
                elif choice=='9':
                    self.Change_Password()
                elif choice =="10":
                     self.Logout()  
               

                             

                          
    def registration(self):
         print ("\n-----REGISTER NEW USER")
         first_name=input("ENTER FIRST NAME: ").strip()
         last_name=input("ENTER LAST NAME : ") .strip()
         dob_str=input("ENTER DATE OF BIRTH (dd-mm-yyyy):")             
        
         dob=datetime.strptime(dob_str,"%d-%m-%Y").date() 
         gender=input("ENTER GENDER(male/female: ")
         phone_num=input("ENTER MOBILE NUMBER: ").strip()
         email=input("ENTER EMAIL ID: ").strip()  
         address=input("ENTER YOUR ADDRESS: ")
         city=input("ENTER CITY : ")
         state=input("ENTER SATAE: ")
         pincode=input("ENTER PINCODE: ")
         password=input("ENTER PASSWORD : ").strip().lower()
         conform_password=input("ENTER CONIRM PASSWORD:").strip().lower()
         '''
         if password !='kash':
             print("[!]ERROR: password wrong ")        
             return
        '''     
         if password==conform_password:
              print("password matched ")
         else:
              print ("password not matched ")    
              return
         
         if not first_name or not last_name  or not dob or not gender or not phone_num or not email or not address or not city or not state or not pincode or not password or not conform_password:
              print ("[!]ALL FIELDS ARE REQUIRED ")
              return
         conn=mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="KW2005",
                                      database="myproject")
         cursor=conn.cursor(dictionary=True)
         try:
              cursor.execute("SELECT customer_id FROM customers WHERE LOWER(email)=%s",(email,))
              if cursor.fetchone() is not None:
                   print("[!]EMAIL is already registered.please login")
                   return
              cursor.execute("SELECT customer_id FROM customers WHERE phone_num=%s",(phone_num,))
              if cursor.fetchone() is not None:
                    print("[!]  PHONE NUMBER is already registered.please login")
                    return
              cursor.execute(
              "INSERT INTO customers(first_name,last_name,dob,gender,phone_num,email,address ,city,state,pincode,password_hash) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
              (first_name,last_name,dob,gender,phone_num,email,address,city,state,pincode,password)
              )
              conn.commit()
              self.customer_id=cursor.lastrowid 
              print("[+]REGISTRATION SUCCESSFUL ! you can now login.")
              print(f"YOUR CUSTOMER ID : {self.customer_id}.please remember ID WHICH Required for LOGIN ")
         except mysql.connector.Error as err:
              print (f"[!]DATABASE ERROR:{err}")
         finally:
              cursor.close()
              conn.close()
################################ LOGIN ###############################
    def login (self):
        print("\n----------LOGIN-----------------")
        self.customer_id=input("CUSTOMER ID : ").strip()
        passw=input("ENTER PASSWORD: ").strip().lower()

        conn=mysql.connector.connect(host="localhost",
                                           user="root" ,
                                           password="KW2005",
                                           database="myproject"
                                    )      
        cursor=conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM customers WHERE customer_id=%s",(self.customer_id,))
            user=cursor.fetchone()
            cursor.execute("SELECT account_number FROM account WHERE customer_id=%s",(self.customer_id,))
            acc_data=cursor.fetchone()
            if acc_data:
                self.account_number=acc_data['account_number']
            if user and user['password_hash']==passw:
              self.customer_id=self.customer_id 
              self.current_user={
                   "CUSTOMER ID ":user['customer_id'],
                   "FIRST NAME":user['first_name'],
                   "LAST NAME":user['last_name'],
                   "ROLE":user['role']

              }
              print(f"\n[+]WELCOME BACK {user['customer_id']} (FIRST NAME:{user['first_name']})  (LAST NAME:{user['last_name']})  (ROLE:{user['role']})")
            else:
              print("[!]INVALID CUSTOMER ID OR PASSWORD.")
        finally:
            cursor.close()
            conn.close()        
  #============================== MY PROFILE ====================================
    def My_profile(self):
        print("-----------------------------------------")
        print("1.View Profile")
        print("2.Update Profile")
        print("3.Back")
        print("-----------------")
        choice=input("enter choice (1-3): ")
        print("----------MY PROFILE-----------")
        print("===================================================")
        if choice=='1':
            self.View_profile()
        elif choice=='2':
            self.Update_profile()
        elif choice =='3':
            self.Back()
             

     #---------------BACK FUNCTION---------------
    def Back(self):
      print("Going Back.......")
      return



    #-------------View Profile----------
    def View_profile(self):
      
        conn=mysql.connector.connect(
            host="localhost",user="root",
            password="KW2005",database="myproject"
        )    
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers where customer_id=%s",(self.customer_id,))#sirf login vale ka profile      
        profile=cursor.fetchall()
        cursor.close()
        conn.close()

        if not profile:
            print("your profile is empty .")
            return
        print("------- 1. VIEW PROFILE-----------")
        print("\n"+ "="*150)
       
        for p in profile:
         
            print(f"ID : {p['customer_id']}") 
            print(f"FIRST NAME : {p['first_name']} ")
            print(f"LAST NAME : {p['last_name']}")
            print(f"DATE OF BIRTH :  {p['dob']} ")
            print(f"GENDER : {p['gender']} ")
            print(f"PHONE NUMBER : {p['phone_num']}")
            print(f"EMAIL :  {p['email']}")
            print(f"ADDRESS : {p['address']}  ")
            print(f"CITY :{p['city']}")
            print(f"STATE : {p['state']} ")
            print(f"PINCODE : {p['pincode']} ")
            print(f"PASSWORD :{p['password_hash']} ")
            print(f"CREATED AT :{p['created_at']}")
            print(f"ROLE : {p['role']}")
            
            print("-"*150)  

    #-----------------UPDATE PROFILE -----------------------")

    def Update_profile(self):
        print("--------UPDATE PROFILE--------")
        print ("1. Email")
        print("2.Phone Number")
        print("3.Address")

        print("--------------------------")
        ch=input("enter choice ")
        conn=mysql.connector.connect(host="localhost",user="root",password="KW2005",database="myproject")
        cursor=conn.cursor()
        try:
           if ch=='1':
              new_val=input("enter new email : ").strip()
              cursor.execute("SELECT customer_id FROM customers WHERE email=%s  AND customer_id != %s",(new_val,self.customer_id) )
               
              if cursor.fetchone():
                print ("this email is already used : ")
                return
              query="UPDATE customers SET email=%s WHERE customer_id=%s"
           elif ch=='2':
              new_val =input("enter new phone number: ").strip()
              cursor.execute("SELECT customer_id FROM customers WHERE phone_num=%s AND customer_id != %s",(new_val,self.customer_id))
              
              if cursor.fetchone():
                print("this number already used :")
                return
              query="UPDATE  customers SET phone_num=%s WHERE customer_id=%s" #if fetchone is false ten this query automatically execute 
           elif ch=='3':
               
               new_val=input("enter new address: ").strip()
               query="UPDATE  customers SET address=%s WHERE customer_id=%s"    
           else:
            print("wrong choice: ")
            return
           cursor.execute  (query,(new_val,self.customer_id)) 
           conn.commit()
           print("PROFILE UPDATED SUCCESSFULLY")
        except mysql.connector.Error as e:
            print (f"[!]Error:{e}")
        finally:
            cursor.close()
            conn.close()

    #======================================MY ACCOUNT============================
    def My_account(self):
        print("---------------MY ACCOUNT-------------")
        print("1. View My Account")
        print("2. Open New Account ")
        print("3. Back")
        ch=input ("enter choice :")
        if ch == '1':
            self.View_My_Account()
        elif ch == '2':
            self.Open_New_Account()
        elif ch=='3':
            self.Back()

    #---------------OPEN NEW ACCOUNT ------------------------
    def Open_New_Account(self):      
        print("--------OPENING NEW ACCOUNT -----------")
        self.customer_id=input("enter customer id :")
        acc_type_id=input("enter account type : 1-Saving  and 2-Current : ")
        balanc=input("enter amount:  ")
        conn=mysql.connector.connect(host="localhost",user="root",password="KW2005",database="myproject")
        cursor=conn.cursor(dictionary=True)
        try: 
            cursor.execute("SELECT account_number FROM account WHERE customer_id=%s", (self.customer_id,) )      
            if cursor.fetchone():
                print ("Account Already Exists of this user")
                return
            cursor.execute("INSERT INTO account (customer_id,account_type_id,balance,opening_date ) VALUES (%s,%s,%s,CURDATE())" ,
                           (self.customer_id,acc_type_id,balanc))
            conn.commit()
            print("ACCOUNT CREATED SUCESSFULLY")
        finally:
            cursor.close()
            conn.close() 

    #------------------VIEW MY ACCOUNT---------------------------
    def View_My_Account(self):
        print("----------------VIEW MY ACCOUNT ------------")
       
        
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="KW2005",
            database="myproject"
        )
        cursor=conn.cursor()
        if not self.customer_id:
            print ("please login first ")
            return 
        else:
            cursor.execute("""SELECT a.account_number ,c.first_name, c.last_name,t.account_type_name,a. balance, a.opening_date, a.status
            FROM account a JOIN customers c ON a.customer_id = c.customer_id
            JOIN account_types t on a.account_type_id= t.account_type_id
            WHERE a.customer_id= %s""",(self.customer_id,))

            row=cursor.fetchone()
       
            if  not row:
              print(f"Account of this {self.customer_id} is not valid  ")
              print("-"*150)
              return False
            print("/n"+ "-"*150)
            print(f"{'ACCOUNT NUMBER':<20}{'FIRST NAME':<20} {'LAST NAME':<20} {'ACCOUNT TYPE':<20} {'BALANCE':<20} {'OPENING DATE' :<20} {'STATUS':<6}")
            print("-"*150)
          
        
            print(f"{row[0]:<20}{row[1]:<20} {row[2]:<20}{row[3]:<20} {row[4]:<20} {str(row[5]):<20}  {row[6]:<6}") 
                                                 
            cursor.close()
            conn.close()                                          
    #==================================DEPOSITE MONEY  ===========================
    def Deposite_money(self):
        acc_num=input("enter Account Number : ").strip()
        amount=input("enter amount for deposite : ")
        conn=mysql.connector.connect(host="localhost",user="root",password="KW2005",database="myproject")
        cursor=conn.cursor()
        cursor.execute("SELECT balance FROM account WHERE account_number=%s", (acc_num,))
        dep=cursor.fetchone()
        if not dep:
            print ("Account number not exists ")
            return
        cursor.execute("UPDATE account SET balance=COALESCE(balance ,0)+ %s WHERE account_number=%s", (amount,acc_num))
        
        old_balance=dep[0] if dep[0] is not None else 0
        new_bal_after=old_balance+int(amount)
        cursor.execute("INSERT INTO bank_statement (account_number,transaction_type,amount,balance_after)VALUES(%s,'CREDIT',%s,%s)",(acc_num,amount,new_bal_after))

        conn.commit()
        print("Deposite Successfully .")
        cursor.execute("SELECT balance FROM account WHERE account_number=%s",(acc_num,))
        final_amount=cursor.fetchone()
        print (f"FINAL AMOUNT IS : {final_amount[0]}") 
       

        #---------------WITHDRAWL AMOUNT---------------------------------------------
    def Withdraw_money(self):
        
      acc_num=input("enter Account Number : ").strip()
      try:  
        amount=Decimal(input("enter amount for withdrawl: "))
      except Exception as e:
         
           print ("please insert amount in right way ex.2000 / 2000.00")
           return

      conn=mysql.connector.connect(host="localhost",user="root",password="KW2005",database="myproject")
      cursor=conn.cursor()
      cursor.execute("SELECT balance FROM account WHERE account_number=%s", (acc_num,))
      withdraw=cursor.fetchone()
        
      if not withdraw:
            print ("Account number not exists ")
            return
       
      balance=withdraw[0]
       
      if balance is None or balance==0:
            print("Balance is empty . ")
            print ("Withdraw Cancelled")
            return
      if balance < amount:
            print("INSUFFICIENT BALANCE")
            return
      cursor.execute("UPDATE account SET balance=COALESCE(balance ,0)- %s WHERE account_number=%s", (amount,acc_num))
               
      new_bal_after=balance-amount
      cursor.execute("INSERT INTO bank_statement (account_number,transaction_type,amount,balance_after)VALUES(%s,'DEBIT',%s,%s)",(acc_num,amount,new_bal_after))
      print("Withdrwal Successfully done.")
      cursor.execute("SELECT balance FROM account WHERE account_number=%s",(acc_num,))
      final_amount=cursor.fetchone()
      print (f"FINAL AMOUNT IS : {final_amount[0]}")
      conn.commit()
      cursor.close()
      conn.close()
       
      #------------ADD BENEFICIARY ------------------
    def beneficiary(self):
          print ("1.Add Beneficiary")
          print ("2.View Beneficiary")
          print ("3.Delete Beneficiary")
          print ("4.Back")
          ch=input("enter choice (1-4):")
          if ch =='1':
              self.Add_beneficiary()
          elif ch == '2':
              self.View_beneficiary()
          elif ch == '3':
              self.Delete_beneficiary()
          elif ch=='4':      
              self.Back()

              
#----------------ADD BENEFICIARY---------------
    def Add_beneficiary(self):       
              print("--------------ADD NEW BENEFICIARY------------------")
             
              name=input("Beneficiary Name : ").strip()
              acc_number=input("enter beneficiary account number : ").strip()
              bank_name=input("enter bank name of beneficiary : ")
              ifsc=input("enter ifsc code (6 digit code ) : ").strip()
              conn=mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="KW2005",
                  database="myproject"
              )
              cursor=conn.cursor()
              cursor.execute("SELECT * FROM account WHERE customer_id=%s",(self.customer_id,))
              id = cursor.fetchone()
              if not id :
                  print("INVALID CUSTOMER ID :")
                  return
              cursor.execute("INSERT INTO beneficiaries (customer_id, beneficiary_name,account_number,bank_name, ifsc_code ,added_date)VALUES (%s,%s,%s,%s,%s,CURDATE())",
                             (self.customer_id,name,acc_number,bank_name,ifsc))
              conn.commit()
              print ("beneficiary added successfully :")
              cursor.close()
              conn.close()
#---------------VIEW BENEFICIARY -----------------------------
    def View_beneficiary(self):       
                  print("-------------- VIEW YOUR BENEFICIARY------------------")
                
                 
                  conn=mysql.connector.connect(
                      host="localhost",
                      user="root",
                      password="KW2005",
                      database="myproject"
                  )
                  cursor=conn.cursor(dictionary=True)
                  try:
                     cursor.execute("SELECT * FROM account WHERE customer_id=%s",(self.customer_id,))
                     id = cursor.fetchone()
                     if not id :
                       print("INVALID CUSTOMER ID :")
                       return
                     cursor.execute("SELECT * FROM beneficiaries WHERE customer_id=%s",(self.customer_id,))
                     view=cursor.fetchall()
                     if not view:
                        print(f"Customer id doesn't have any beneficiary , please add first . ")
                        return
                
                     
                     print("-"*150)
                     print (f"{'CUSTOMER ID ':<20}{'BENEFICIARY NAME ':<20}{'ACCOUNT NUMBER':<20}{'BANK NAME OF BENEFICIARY ':<40}{'IFSC':<20}{'ADDED DATE':<20}")
                     print("-"*150)
                     
                     for views in view :  
                      print (f"{views['customer_id']:<20}{views['beneficiary_name']:<20}{views['account_number']:<20}{views['bank_name']:<40}{views['ifsc_code']:<20}{str(views['added_date']):<20}")
                      print("-"*150)
                  except Exception  as e:
                    print("Error:",e) 
                  finally:  
                   cursor.close()
                   conn.close()   
  #-----------------DELETE BENEFICIARY-----------------------------                      
    def Delete_beneficiary(self):       
                      print("-------------- DELETE  BENEFICIARY------------------")
                  
                      acct_num=input("Enter beneficiary account number: ")
                     
                      conn=mysql.connector.connect(
                          host="localhost",
                          user="root",
                          password="KW2005",
                          database="myproject"
                      )
                      cursor=conn.cursor(dictionary=True)
                      try:
                         cursor.execute("SELECT * FROM account WHERE customer_id=%s",(self.customer_id,))
                         id = cursor.fetchone()
                         if not id :
                           print("INVALID CUSTOMER ID :")
                           return
                         cursor.execute("SELECT * FROM beneficiaries WHERE account_number=%s AND customer_id=%s ",(acct_num,self.customer_id))
                         view=cursor.fetchone()
                         if not view:
                            print(f"Customer id doesn't have any beneficiary of Account Number {acct_num}  . ")
                            return
                         cursor.execute("DELETE FROM beneficiaries WHERE account_number=%s AND customer_id=%s",(acct_num,self.customer_id))
                         conn.commit()
                         print (f"Beneficiary of {acct_num} is Deleted Successfully  ")
                      except Exception  as e:
                        print("Error:",e) 
                      finally:  
                       cursor.close()
                       conn.close()  
    #----------------------------TRANSFER MONEY---------------------------                   
    def Transfer_money(self):
        
        conn=mysql.connector.connect(
                                                  host="localhost",
                                                  user="root",
                                                  password="KW2005",
                                                  database="myproject"
                                              )
        cursor=conn.cursor(dictionary=True)
        acc_num=self.account_number
        ben_id=input("enter beneficiary  id  :")
        amount=float(input("enter amount for transfer: "))
        mode=input("enter mode of payment (NEFT/RTGS/IMPS/UPI): ").strip().upper()
        allowed=['NEFT','RTGS','IMPS','UPI']

        if mode not in allowed:
            print ("Invalid Mode !  NEFT/RTGS/IMPS/UPS ")
            return
        
        try:
            cursor.execute("SELECT balance FROM account WHERE account_number=%s",(acc_num,))
            data=cursor.fetchone()
            if not data:
                print("Invalid customer:")
                return
            if data['balance']<amount:
                print("balance is unsufficient:")
                return
            if mode=='RTGS' and  amount <20000:
                print("RTGS Required Minimun Amount 20000 For Transfer5")
                return
            if mode=='UPI' and amount >100000:
                print("UPI Maximum Amount is 100000")
                return
           
           
            cursor.execute("SELECT account_number,beneficiary_id FROM beneficiaries WHERE customer_id=%s AND beneficiary_id=%s",(self.customer_id,ben_id))
            data=cursor.fetchone()
            if not data:
                print(f"THIS {ben_id}IS NOT MATCH WITH ACCOUNT NUMBER {acc_num}") 
                return
            to_acc=data['account_number']
            to_ben=data['beneficiary_id']
            
            
            cursor.execute("INSERT INTO  transfer_money (account_number_from,beneficiary_id,account_table_to,amount) VALUES(%s,%s,%s,%s)",(acc_num,to_ben,to_acc,amount))
           
            transfer_id=cursor.lastrowid
            
            cursor.execute("UPDATE account SET balance=COALESCE(balance,0)-%s WHERE account_number=%s",(amount,acc_num))
           
            cursor.execute("UPDATE transfer_money SET status='SUCCESS' WHERE transfer_id=%s",(transfer_id,))
            print("********************* TRANSACTION SUCCESSFUL ! *************")
            cursor.execute("SELECT balance from account where account_number=%s",(acc_num,))
            new_bal=cursor.fetchone()
            print(f"Your Final Balance : {new_bal}")
            conn.commit()
           
            
            
        except Exception as e:
            conn.rollback()
           
            try:
                if transfer_id is not None:
                    cursor.execute("UPDATE transfer_money SET status='FAILED' WHERE transfer_id=%s",(transfer_id,))
                    conn.commit()
            except:
                pass
           
            print(f"Error:{e}")        
        finally:
            cursor.close()
            conn.close()      

#------------------BANK STATEMENT--------------------------------------

    def Bank_Statement(self):     
        acc_num=input("enter account number : ")
        conn=mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="KW2005",
                                    database="myproject"
                                        )
        cursor=conn.cursor()

        cursor.execute("SELECT account_number FROM account WHERE account_number=%s",(acc_num,))
        check=cursor.fetchone()
        if not check:
            print("Account Number is not exists")
            return
        print (f"\n--------------------BANK STATEMENT--------------------------------")
        print(f"                     Account Number : {acc_num}             ")
        cursor.execute("SELECT customer_id FROM account WHERE account_number=%s",(acc_num,))
        cust_id_row=cursor.fetchone()
        cust_id=cust_id_row[0] if cust_id_row else None
        cursor.execute("SELECT first_name,last_name FROM customers WHERE customer_id=%s",(cust_id,))
        name=cursor.fetchone()
        if name:
            print("-"*150)
            print(f"                  NAME: {name[0]}{name[1]}                       ")
                       
        cursor.execute("SELECT transaction_type, amount, balance_after,transaction_date FROM bank_statement WHERE account_number=%s ORDER BY transaction_date DESC",
                       (acc_num,))
        records=cursor.fetchall()
        if not records:
            print(f" statement is Empty in Account Number {acc_num} ")
        else:
            print("-"*150)
            print(f"{'TRANSACTION DATE ':<30} {'AMOUNT':<30}{'TRANSACTION TYPE ':<30}{ 'BALANCE ':<30}")
            for row in records:
                print (f"{str(row[3]):<30} {row[1]:<30} {row[0]:<30} {row[2]:<30}")
        cursor.close()
        conn.close()

  #===================================LONES=======================================      
    def Loans(self):
        print ("\n ---------------LOANS --------------------")
        print("1.Apply for Loans")
        print("2.View Your loan")
        print ("3.Pay EMI ")
        print ("4.View EMI Statement ")
        print ("5.Exit ")
        ch=input("enter choice (1-4): ")
        if ch=='1':
            self.Apply_loans()
        elif ch=='2':
            self.View_loans()
        elif ch=='3':
            self.Add_Pay_emi()
        elif ch=='4':
            self.View_Emi_Transactions()    
        elif ch=='5':
            self.Back()

   #------------------------------APPLY LOANS --------------------------         
    def Apply_loans (self):
        
        print("\n-------APPLY FOR LOAN---------")
        print("Types : HOME,PERSONAL,EDUCATION,CAR")
      
        conn=mysql.connector.connect(
                                            host="localhost",
                                            user="root",
                                            password="KW2005",
                                            database="myproject"
                                                )
        cursor=conn.cursor()
        
        cursor.execute("SELECT customer_id FROM customers WHERE customer_id =%s",(self.customer_id,))
        check=cursor.fetchone()
        if not check:
            print("Customer id  is not valid")
            return
        loan_type=input("Enter Loan Type: ").strip().upper()
        loan_amount=float (input("Enter Loan Amount : "))
        loan_duration=int(input("Enter Duration in Months: "))
        if loan_type=="HOME":
            interest=8.5
        elif loan_type=="CAR":
            interest=9.5  
        elif loan_type=="EDUCATION":
            interest=7.0
        else:
            interest=12.0

        cursor.execute("""INSERT INTO loans(customer_id,loan_type,loan_amount,loan_duration ,interest_rate ,application_date,loan_status)VALUES(%s,%s,%s,%s,%s,CURDATE(),'PENDING')""",
        ( self.customer_id,loan_type,loan_amount, loan_duration, interest))
        conn.commit()
        print(f"[+]{loan_type} Loan of {loan_amount}  Apllied Successfully!  , Status:PENDING")
        cursor.close()
        conn.close() 

#----------------------VIEW LOANS--------------------------
    def View_loans(self):
        conn=mysql.connector.connect(
                                     host="localhost",
                                    user="root",
                                     password="KW2005",
                                    database="myproject"
                                                        )
        cursor=conn.cursor()
     
        cursor.execute("SELECT customer_id FROM customers WHERE customer_id =%s",(self.customer_id,))
        check=cursor.fetchone()
        if not check:
            print("Customer id  is not valid")
            return
        cursor.execute("SELECT * FROM loans WHERE customer_id =%s",(self.customer_id,))
        loans=cursor.fetchall()
        if not loans:
            print ("No Loans Found : ")
        else:
            print ("------------------------------VIEW YOUR LOAN-------------------")
            print (f"CUSTOMER ID :{self.customer_id}")
            print("-"*150)
            print (f"{'LOAN ID ':<20}{'CUSTOMER ID  ':<20}{'LOAN TYPE ':<20}{'LOAN AMOUNT ':<20}{'LOAN DURATION':<20}{'INTEREST':<20}{'APPLICATION DATE':<20}{'STATUS':<20}")
            print("-"*150)
            for loan in loans:
              
                print (f"{loan[0]:<20}{loan[1]:<20}{loan[2]:<20}{loan[3]:<20}{loan[4]:<20}{loan[5]:<20}{str(loan[6]):<20}{loan[7]:<20}")
                print("-"*150)
          
            cursor.close()
            conn.close()
    def Add_Pay_emi(self):
        conn=mysql.connector.connect(
                                 host="localhost",
                                user="root",
                                password="KW2005",
                            database="myproject"
                            )
        cursor=conn.cursor()
       
        cursor.execute("SELECT customer_id FROM customers WHERE customer_id =%s",(self.customer_id,))
        check=cursor.fetchone()
        if not check:
            print("Customer id  is not valid")
            return
        cursor.execute("SELECT loan_id,loan_amount,interest_rate,loan_status FROM loans WHERE customer_id =%s AND loan_status ='APPROVED'",(self.customer_id,))
        loans=cursor.fetchall()
        if not loans:
            print ("No Approved Loans Found : ")
        print("YOUR ACTIVE LONES")
        for loan in loans :
                       
            print (f"LOAN ID :{loan[0]:<20} AMOUNT:{loan[1]:<20} RATE:{loan[2]:<20} STATUS:{loan[3]:<20}")
        loan_id=int(input("enter loan id: "))
        cursor.execute("SELECT IFNULL(SUM(payment_amount),0)FROM loan_payments WHERE loan_id=%s",(loan_id,))
        total_paid=float(cursor.fetchone()[0])
        cursor.execute("SELECT loan_amount, interest_rate ,loan_duration FROM loans WHERE loan_id=%s",(loan_id,))
        data =cursor.fetchone()
        if not data:
            print("loan id is not valid :")
        loan_amount, interest_rate, loan_duration=data
        loan_amount=float(loan_amount)
        interest_rate=float(interest_rate)
        n=int(loan_duration)

        remaining=(loan_amount)-total_paid
        if remaining<=0:
            print("this loan already completed ")
            return
        print(f"\n REMAING LOAN : {remaining}")

        r=interest_rate/(12*100) 
        if r==0: 
            monthly_emi=loan_amount/n
        else:
             monthly_emi=loan_amount * r* ((1+r)**n)/(((1+r)**n)- 1 )
        print(f"Duration: {n}months ")
        print(f"Monthly Emi  : {round(monthly_emi,2)}")
        confirm=input(f"{round(monthly_emi,2)} YOU WANT TO PAY EMI ? (y/n): ") 
        if confirm.lower()!='y':
            print("Cancelled")
        new_remaining=remaining-monthly_emi
        cursor.execute("INSERT INTO loan_payments (loan_id, payment_amount,payment_date,remaining_amount , payment_status)VALUES (%s,%s,CURDATE(),%s,'PAID')",
                       (loan_id,round(monthly_emi,2),round (new_remaining,2)))
        conn.commit()
        print(f"EMI ADDED SUCCESSFULLY! {round(monthly_emi,2)} Paid , New Balance :{round(new_remaining,2)}")

      
        if new_remaining <=0:
            cursor.execute("UPDATE loans SET loan_status='COMPLETED' WHERE loan_id=%s",(loan_id,))
            conn.commit()
            print("*** Loan Installment Completed ***")
        
        cursor.close()
        conn.close()

#------------VIEW EMI TRANSACTION----------------------------------

    def View_Emi_Transactions(self):
        conn=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="KW2005",
                                database="myproject"
                                )
        cursor=conn.cursor()
       
        cursor.execute("SELECT customer_id FROM customers WHERE customer_id =%s",(self.customer_id,))
        check=cursor.fetchone()
        if not check:
            print("Customer id  is not valid")
            return
        cursor.execute("SELECT loan_id,loan_amount,interest_rate,loan_status FROM loans WHERE customer_id =%s AND loan_status ='APPROVED'",(self.customer_id,))
        loans=cursor.fetchall()
        if not loans:
            print ("No Loans Found for this customer id  : ")
            return
        

        print ("------------------------------VIEW LOAN STATEMENT -------------------")
        print(f"CUSTOMER ID : {self.customer_id}")
        cursor.execute("SELECT account_number FROM account WHERE customer_id=%s",(self.customer_id,))
        acc_num=cursor.fetchone()
        if acc_num:  
            print (f"                ACCOUNT NUMBER: {acc_num[0]}              ")
        cursor.execute("SELECT first_name,last_name FROM customers WHERE customer_id=%s",(self.customer_id,))
        name=cursor.fetchone()
        if name:
            print(f"                  NAME: {name[0]}{name[1]}                 ")
        print(f"\nCustomer {self.customer_id} have Total {len(loans)} Loans ")
        print("-"*150)
        for loan in loans :
                    print (f"LOAN ID :{loan[0]:<20} AMOUNT:{loan[1]:<20} RATE:{loan[2]:<20} STATUS:{loan[3]:<20}")
        loan_id=input("enter loan id: ")
        cursor.execute("SELECT loan_id FROM loans WHERE loan_id=%s",(loan_id,))
        data =cursor.fetchone()
        if not data:
            print("loan id is not valid :")
        cursor.execute("SELECT * FROM loan_payments WHERE loan_id=%s ORDER BY payment_date",(loan_id,))
        payments =cursor.fetchall()
        if not payments:
            print(f"No EMI Transaction of Lone Id {loan_id}")
            return
        print (f"{'PAYMENT ID':<20}{'LOAN ID  ':<20}{'PAYMENT AMOUNT ':<20}{'PAYMENT DATE ':<20}{'REMAINING AMOUNT':<20}{'PAYMENT STAUTS':<20}")
        print("-"*150)
        for pay in payments:
            print (f"{pay [0]:<20}{pay [1]:<20}{pay [2]:<20} {str(pay [3]):<20}{pay [4]:<20}{pay [5]:<20}")
            print("-"*150)
                    
        cursor.close()
        conn.close()    

    #-------------------------------CHANGE PASSWORD-----------1
    # --------------------------")                        
    def Change_Password(self):
        old_pass=input("enter password :").strip().lower()
        conn=mysql.connector.connect(
                                            host="localhost",
                                            user="root",
                                            password="KW2005",
                                            database="myproject"
                                                )
        cursor=conn.cursor()
        cursor.execute("SELECT password_hash FROM customers WHERE customer_id=%s",(self.customer_id,))
        data =cursor.fetchone()
        if not data:

            print("[!] Customer Id not found ")
            return
        stored_pass=data[0].lower()      
        if stored_pass != old_pass:
            print("[!] wrong password")
            
            return
        new_pass=input("enter new password : ").strip().lower()
        conform_new_pass=input("Conform New Password : ").strip().lower()

        if new_pass!=conform_new_pass:
            print("[!] new password not match with conform password")
            return
        if not new_pass:
            print("New password Should not empty.")
            return
        cursor.execute("UPDATE customers SET password_hash=%s WHERE customer_id=%s",(new_pass,self.customer_id))
        conn.commit()
        print("PASSWORD UPDATED SUCCESSFULLY ! ")
        cursor.close()
        conn.close()
    def Logout(self):
            self.customer_id=None
            self.current_user = None
            print("[+] Logged out successfully.")

########################### ADMIN LOGIN ###############################
    def Admin_login(self):
        while True:
            print("              WELCOME TO THE ADMIN LOGIN           ")
            print("1.View All Customer  ")
            print("2.View All Customer Account ")     
            print("3.View Beneficiaries of Customer") 
            print("4.View All Loans ")
            print("5.Apporved / Reject Loans") 
            print("6.View All Loan Payments ")
            print("7.Return  ")


            ch=input("enter choice : ").strip()
            if ch=='1':
                self.View_All_Customer()
            elif ch=='2':
                self.View_All_Account()
            elif ch=='3':
                self.View_All_Beneficiaries() 
            elif ch=='4':
                self.View_All_loans() 
            elif ch=='5':
                self.Aprroved_Reject_lones()
            elif ch=='6':
                self.View_All_loan_Payment()
            elif ch=='7':
                break   
            else:
                print("invalide choice")

    #-------------VIEW ALL CUSTOMERS-- ADMIN SIDE---------------------------
    def View_All_Customer(self):
        conn=mysql.connector.connect(
                    host="localhost",user="root",
                    password="KW2005",database="myproject"
                )    
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers ")    
        profile=cursor.fetchall()
        if not profile:
            print(" profile is empty .")
            return
        print("------- 1. VIEW PROFILE-----------")
        print("\n"+ "="*150)
      
        for p in profile:
                  
                    print(f"ID : {p['customer_id']}") 
                    print(f"FIRST NAME : {p['first_name']} ")
                    print(f"LAST NAME : {p['last_name']}")
                    print(f"DATE OF BIRTH :  {p['dob']} ")
                    print(f"GENDER : {p['gender']} ")
                    print(f"PHONE NUMBER : {p['phone_num']}")
                    print(f"EMAIL :  {p['email']}")
                    print(f"ADDRESS : {p['address']}  ")
                    print(f"CITY :{p['city']}")
                    print(f"STATE : {p['state']} ")
                    print(f"PINCODE : {p['pincode']} ")
                    print(f"PASSWORD :{p['password_hash']} ")
                    print(f"CREATED AT :{p['created_at']}")
                    print(f"ROLE : {p['role']}")
                    
                    print("-"*150)  

        cursor.close()
        conn.close()
       #-------------------------VIEW ALL ACCOUNTS --ADMIN SIDE------------------ 
    def View_All_Account(self):
        conn=mysql.connector.connect(
                            host="localhost",user="root",
                            password="KW2005",database="myproject"
                        )    
        cursor=conn.cursor(dictionary=True) 
        cursor.execute("""SELECT  a.account_id ,c.customer_id,c.first_name, c.last_name,a.account_number,t.account_type_name,a. balance, a.opening_date, a.status
                FROM account a JOIN customers c ON a.customer_id = c.customer_id
                JOIN account_types t ON a.account_type_id= t.account_type_id
                """
                )
        account=cursor.fetchall()
        if not account:
            print(" Accounts is empty .")
            return
        print("------- 1. VIEW ACCOUNTS DETAILS-----------")
        print("\n"+ "="*170)
        print(f"{'ACCOUNT ID':<20}{'CUSTOMER ID ':<20} {'FIRST NAME ':<20} {'LAST NAME':<20} {'ACCOUNT NUMBER':<20} {'ACCOUNT TYPE' :<20} {'BALANCE':<20} {' OPENING DATE':<20} {' STATUS':<20}")
        for acc in account:
            print("\n"+ "="*170)
            print(f"{acc['account_id']:<20}{acc['customer_id']:<20} {acc['first_name']:<20} {acc['last_name']:<20} {acc['account_number']:<20} { acc['account_type_name']:<20} {acc['balance']:<20} {str(acc['opening_date']):<20} {acc['status']:<6}")
            print("\n"+ "="*170)
        cursor.close()
        conn.close()
 #------------VIEW ALL Beneficiaries - ADMIN SIDE ------------------
    def View_All_Beneficiaries(self):
        conn=mysql.connector.connect(
                            host="localhost",user="root",
                            password="KW2005",database="myproject"
                        )    
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM  beneficiaries ")
        beneficiary=cursor.fetchall()
        if not beneficiary:
          print("  beneficiariy table empty .")
          return
        print("-------VIEW CUSTOMERS BENEFICIARY-----------")
        print("\n"+ "="*150)
        print(f"{"BENEFICIARY ID":<20}{"CUSTOMER ID ":<20}{"BENEFICIARY NAME":<20}{"ACCOUNT NUMBER":<20}{"BANK NAME":<20}{"IFSC CODE":<20} {"ADDED DATE ":<20}")
        print("\n"+ "="*150)
        for ben in beneficiary:
             
             print (f"{ben['beneficiary_id']:<20}{ben['customer_id']:<20}{ben['beneficiary_name']:<20}{ben['account_number']:<20}{ben['bank_name']:<20}{ben['ifsc_code']:<20}{str(ben['added_date']):<20}")
             print("\n"+ "-"*150)
        cursor.close()
        conn.close()

        #------------VIEW ALL LOANS - ADMIN SIDE ------------------
    def View_All_loans(self) :
        conn=mysql.connector.connect(
                                    host="localhost",user="root",
                                    password="KW2005",database="myproject"
                                )    
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM loans ")      
        loan=cursor.fetchall()
        if not loan:
            print("  Loans table empty .")
            return
        print("-------VIEW CUSTOMERs LOANS-----------")
        print(f"{"LOAN ID":<20}{"CUSTOMER ID":<20}{"LOAN TYPE":<20}{"LOAN AMOUNT":<20}{"LOAN DURATION":<20}{"INTEREST RATE":<20}{"APPLICATION DATE":<20}{"STATUS":<20}")
        print("\n"+ "="*150)
        for l in loan:
            print (f"{l['loan_id']:<20}{l['customer_id']:<20}{l['loan_type']:<20}{l['loan_amount']:<20}{l['loan_duration']:<20}{l['interest_rate']:<20}{str(l['application_date']):<20}{l['loan_status']:<20}")
            print("\n"+ "-"*150)
        cursor.close()
        conn.close()

        #---------------------APPROVED/REJECT LOAN--------------------
    def Aprroved_Reject_lones(self):
        conn=mysql.connector.connect(
                                    host="localhost",user="root",
                                    password="KW2005",database="myproject"
                                        )    
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM loans WHERE loan_status='PENDING'")
        pay=cursor.fetchall()
        if not pay:
            print ("Not any Loan is Pending for your Approval")
            return
        print("----------- FOR APPROVED/REJECT------------------")
        print("="*150)
        print(f"{"LOAN ID":<20}{"CUSTOMER ID":<20}{"LOAN TYPE":<20}{"LOAN AMOUNT":<20}{"LOAN DURATION":<20}{"INTEREST RATE":<20}{"APPLICATION DATE":<20}{"LOAN STATUS":<20}")
        for p in pay:
              print(f"{p['loan_id']:<20}{p['customer_id']:<20}{p['loan_type']:<20}{p['loan_amount']:<20}{p['loan_duration']:<20}{p['interest_rate']:<20}{str(p['application_date']):<20}")
        loan_id=input("enter loan id : ")
        action=input("enter 1 - Approved , 2 - Reject  : ")
        if action=='1':
            new_loan_status='APPROVED'
            
        elif action == '2':
             new_loan_status='REJECTED'
        else:
            print("Invalid Action ")     
             
        cursor.execute("UPDATE loans SET loan_status=%s WHERE loan_id=%s",(new_loan_status,loan_id)) 
        conn.commit()
        print(f"LOAN IS SUCCESSFULLY SANCTION OF LOAN ID {loan_id} , NOW STATUS IS {new_loan_status}")  
        cursor.close()
        conn.close()

    def View_All_loan_Payment(self):
        conn=mysql.connector.connect(
                                            host="localhost",user="root",
                                            password="KW2005",database="myproject"
                                        )    
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM loan_payments ")    
        loan=cursor.fetchall()
        if not loan:
            print("  Loans table empty .")
            return
        print("-------VIEW  LOANS   EMI  PAYMENT -----------")
        print(f"{"PAYMENT ID":<20}{"LOAN ID":<20}{"PAYMENT AMOUNT":<20}{"PAYMENT DATE":<20}{"REMAINING AMOUNT":<20}{"PAYMENT STATUS":<20}")
        print("\n"+ "="*150)
        for l in loan:
            print (f"{l['payment_id']:<20}{l['loan_id']:<20}{l['payment_amount']:<20}{str(l['payment_date']):<20}{l['remaining_amount']:<20}{l['payment_status']:<20}")
            print("\n"+ "-"*150)
        cursor.close()
        conn.close()     
########################################################
bank=BankingApp()
bank.run()