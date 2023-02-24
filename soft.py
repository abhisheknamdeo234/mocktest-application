
# balance = 10000
# print( "    ATM    ")
# print("""
#       1)  Balance
#       2)  Withraw
#       3)  Deposit
#       4)  Quit
      
# """)
# try:
#     Option = int(input("Enter option: "))
# except : 
    
#     print("Enter 1,2,3, or 4 Only")
    
# if Option ==1:
#     print("Balance $",balance)
# if Option == 2:
#     print("Balance $",balance)
#     Withraw=float(input("Enter any amount $ "))
#     if Withraw >0:
#         Foreward_balance=(balance - Withraw)
#         print("Foreward_balance $",Foreward_balance)
#     elif Withraw > balance:
#         print("Insufficient balance")
#     else:
#         print("No withraw made")
# if Option == 3:
#       print("Balance $",balance)
#       Deposit = float(input("Enter any amount $ "))
#       if Deposit > 0:
#           Foreward_balance=(balance + Deposit)
#           print("Foreward_balance $",Foreward_balance)
#       else:
#           print("No Deposit made")
# if Option == 4:
#      exit() 

class bank:
    def __init__(self,Balance = 100000):
        self.Balance = Balance
        
    def Check_Balance(self) :
        print("Balance $",self.Balance)  
        
    def Withdraw(self):
        print("Balance $",self.Balance)
        withdraw = float(input("Enter amount: "))
        if withdraw >0:
            balance=self.Balance - withdraw
            print(" Balance $",balance)    
        elif withdraw>self.Balance:
            print("Insufficient Balance") 
        else:
            print("no transaction were made")
            
    def Deposit(self):
        print("Balance $",self.Balance)    
        deposit = float(input("Enter amount: "))
        if deposit > 0: 
            balance = self.Balance + deposit 
            print("Balance $",balance)
        else:
            print("no transaction were made")
     
    def quit(self):
        exit() 
        
    def menu(self):
        while True:
            print( "  ATM  ")
            print("""
            1)  Balance
            2)  Withraw
            3)  Deposit
            4)  Quit
            """)  
            
            try:
             option = int(input("enter Option no"))
            except :
             print("please type no 1 ,2 ,3  or 4")    
                
            
            if option ==1:
                self.Check_Balance()
            elif option==2:
                self.Withdraw()
            elif option == 3:
                self.Deposit()
            elif option == 4:
                self.quit()
                
                                
atm = bank()     
atm.menu()     
                             
               
             
        



         
              
                        
        
         
   
    

    