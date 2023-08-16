import pandas as pd
# - means negtive
class Bank:
    
    def _init_(self ,balance  ,  income , expensses , investing_amount , investing_return ):
        self.balance =balance
        self.income =  income
        self.expensses = expensses
        self.investing_amount = investing_amount
        self.investing_returns = investing_return
        self.income_dict = [[
          self.balance,
          self.income,
          self.expensses,
          self.investing_amount,    
           self.investing_returns
        ]]
    
                
        
class Expenses(Bank):
     def _init_(self, balance  , income , expensses ,investing_amount , investing_return):
          super()._init_(balance  ,  income , expensses ,investing_amount , investing_return )

          

     def new_balance(self):
          print('youre old balance is', self.balance)
          self.balance += self.income - self.expensses +self.investing_returns 
          print("youre monthly stats" , self.income_dict)
          self.income_dict[0][0] = self.balance
          self.df = pd.DataFrame(self.income_dict ,columns=['balance', 'income' , 'expensses' , 'investing_amount' , 'investing return'])
          print(self.df)

     def withdrall(self, amount_withdrawal):
         self. amount_withdrawal =  amount_withdrawal
         if self. amount_withdrawal > self.balance:
                raise Exception("please enter a withdrall amount smaller than youre balance")
         elif self. amount_withdrawal < self.balance:
                self.balance = self.balance - self. amount_withdrawal
                print("withdrall successfull youre balance after withdrall: ",self.balance)

         elif self. amount_withdrawal == self.balance:
                self.balance = self.balance - self. amount_withdrawal
                print("withdrall successfull youre balance after withdrall: ",self.balance)
          
class BudgetGoal(Bank):
     
     def _init_(self,balance ,  income , expensses , investing_amount , investing_return  , income_goal ,expenses_goal ,investing_return_goal  ):
          super()._init_(balance ,  income , expensses , investing_amount , investing_return )
          self.income_goal = income_goal 
          self.expenses_goal = expenses_goal
          self. investing_return_goal = investing_return_goal
     
     def goals_budget (self):
          if self.income_goal > self.income:
               print('Youre income  is more then expected by',(self.income_goal - self.income) / self.income_goal * 100,"%")

          elif self.investing_return_goal < self.investing_returns:
                print('Youre income  is less then expected by',(self.income - self.income_goal) / self.income * 100,"%")

          elif self.income_goal == self.income:
               print('youre income goal is equal to youre income')

          if self.expenses_goal > self.expensses:
               print('Youre expense is more then expected by',(self.expenses_goal - self.expensses) / self.expenses_goal * 100,"%")

          elif  self.expenses_goal < self.expensses:
                print('Youre income goal is less then expected by',(self.expensses - self.expenses_goal) / self.expensses * 100,"%")

          elif self.expenses_goal == self.expensses:
               print('youre expenses goal is equal to youre expenses')
          

          if self.investing_return_goal > self.investing_returns:
               print('Youre investing return goal is more then expected by',(self.investing_return_goal - self.investing_returns) / self.investing_return_goal * 100,"%")

          elif  self.investing_return_goal < self.investing_returns:
                print('Youre income goal is less then expected by',(self.investing_returns - self.investing_return_goal) / self.investing_returns * 100,"%")

          elif self.investing_return_goal == self.investing_returns:
               print('youre invsting return goal is equal to youre invsting')

          
class Transactions:
     def _init_ (self , name , account_number  ,transaction_amount,date):
            self.name = name
            self.account_number = account_number
            self.transaction_amount = transaction_amount
            self.date = date
            self.df = pd.DataFrame()

     def create_transaction(self):
          self.Transaction_data = [[
           self.name,
            self.account_number ,
           self.date,
           self.transaction_amount
          ]]
          self.df = pd.concat([self.df, pd.DataFrame(self.Transaction_data, columns=['name', 'account_number', 'date', 'transaction_amount'])]).reset_index(drop=True)

     
     def transaction_history(self):
         print(self.df)
     



        
  

          



 
       
print('Welcome to personal finance tracker💼')

option = input("What option do you want A Add monthly earning and expensses B add monthly goal , C do a transaction💸: ")
option = option.upper()
if option == "A":
     try:
        income = int(input('please enter youre income'))
        balance = int(input('please enter bank balance '))
        expensses = int(input('please enter youre expenses'))
        investing_returns  = int(input('please enter youre invsting return'))
        investing_amount = int(input('please enter youre invsting amount'))

        obj_1 = Expenses(balance,income,expensses,investing_amount,investing_returns)
        obj_1.new_balance()
        
        withdrall=input("do you want to withdrall money Y:N")
        withdrall= withdrall.upper()
        if withdrall =="Y":
          withdrall_amount = int(input('please enter withdrall'))
          obj_1.withdrall(withdrall_amount)




     except ValueError:
          raise Exception("Value Error: please enter a number not alphbaticle letter")



    
elif option == "B":
     
    try:
        balance = int(input('please enter youre balance'))
        income = int(input('please enter youre income '))
        expensses = int(input('please enter youre expenses'))
        investing_amount  = int(input('please enter youre investing amount'))
        investing_returns  = int(input('please enter youre invesment return'))
        income_goal = int(input('please enter youre income goal'))
        expensses_goal = int(input('please enter youre expenses goal'))
        investing_return_goal = int(input('please enter investing return goal'))
        obj = BudgetGoal(balance,income,expensses,investing_amount,investing_returns , income_goal ,expensses_goal,investing_return_goal)
        obj.goals_budget()
    except ValueError:
         raise Exception("Value Error: please enter a number not alphbaticle letter")
    
    

     
  
elif option =="C":
     try:
        name = str(input('please enter youre name '))
        account_number = int(input('please enter youre account number'))
        date  = str(input('please enter the `transaction date'))   
        transaction_amount  = int(input('please enter youre transaction amount'))
        obj = Transactions(name,account_number,date,transaction_amount)
        obj.create_transaction()
        savetransaction = input('do you whant to save transaction Y:N')
        savetransaction.upper()
        if savetransaction =='Y':
             obj.transaction_history()
        elif savetransaction =='N':
             print('thank you for using personal finance taracker')
        else:
             print('please enter valid number')
             
     except ValueError:
          raise Exception("please enter valid value")
