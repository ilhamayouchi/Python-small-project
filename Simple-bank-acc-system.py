class Bank :
       def __init__(self , acc_number,owner_name,balance=0,pin="2013"):
              self.acc_number =acc_number
              self.owner_name = owner_name
              self.balance=balance
              self.pin=pin
              self.history_transaction=[]
       def deposit_money(self) :
            try:
              new_balance=float(input("Enter the amount of monney you want to add to your Balance :"))
              self.balance += new_balance
              print(f"Your New Balance is : {self.balance}")
              self.history_transaction.append({"type":"deposit","amount":new_balance,"balance":self.balance})
            except ValueError:
               print("Invalid input. Please enter a numeric value.")
       def withdraw_Money(self):
              if self.pin == input("Enter you pin : ") :
                 if self.balance <= 0 :
                     print("You have no money to withdraw.")
                 else :
                     withdraw_balance =float(input("Enter the amount of money you want to withdraw :"))

                     
                     if withdraw_balance > self.balance :
                            print("The amount of money you want to withdraw is greather than your current Balance.")
                     else :
                            self.balance= self.balance - withdraw_balance
                            print(f"Withdrawal successful. New balance: {self.balance}")
                            self.history_transaction.append({"type":"withdraw","amount":withdraw_balance,"balance":self.balance})
              else:
                 print("Incorrect PIN. Access denied.")

       def check_balance(self):
              print(f"Your current balance{self.balance}")
       def check_history_of_transaction(self):
              print("Your History of Transictions : ")
              for history in self.history_transaction :
                     print(history)
    
       
#instance
BankAccount=Bank(3456,"ilham ayouchi", 879.89)
#Testing The Methods.
#BankAccount.deposit_money()
#BankAccount.withdraw_Money()
#BankAccount.check_balance()
#BankAccount.check_history_of_transaction() 
def main():
      #Menu 
     while True:  # Keep looping until the user chooses to quit
      print("1-Deposit Money")
      print("2-Withdraw Money")
      print("3-Check Balance")
      print("4-History of Transictions")
      print("5-Quit")
      choice=input("Choose an option(1-5) :")
      if choice == "1" :
           BankAccount.deposit_money()
      elif choice == "2" :
           BankAccount.withdraw_Money()
      elif choice == "3" :
            BankAccount.check_balance()
      elif choice == "4" :
            BankAccount.check_history_of_transaction()
      elif choice == "5" :
             print("Exiting the System.")
             break 
      else :
         print("Invalid Choice ")
main()
    
            




                     

              

