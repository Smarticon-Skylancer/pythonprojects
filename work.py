#display message
print("Welcome to Personal Finance Calculator")
# Function to add Income
def addIncome():
	Income = float(input("Enter Your Monthly Income: "))
#Function to add Expense
def addExpense():
	expense = float(input("Enter The Expense : "))
   category = input ("Essential or Non Essential : ")
#Function to Generate Budget Summary
def budgetSummary():
	Budget = float(input("Enter Budget Summary : "))
   income = float(input("Income: "))
   total_expense = float(input("Total Expense: "))
   remaining_budget= float(input("Remaining Budget : "))
   remaining_budget = income - total_expense
   if remaining_budget >0 and remaining_budget  <=1500.0:
    print("You're under budget. Consider saving £750 (50 %.of remaining budget).")
    print("expense breakdown  ")
    essential=float(input("Essential "))
    non_essential=float(input("Non-Essential  "))

   elif remaining_budget > 1500.0 :
     print("Well done! You have managed your budget ")

   elif remaining_budget < 0 :
     print("You have used your all budget")

   else:
     print("warning! you are over budget ")
option = 0                  
while (option !=4): 
 print("1. Enter Income")
 print("2. Add Expense")
 print("3. View Budget Summary")
 print("4. Exit")
 
 option = int(input("Enter Your Choice : "))
 if option == 1 :
   addIncome()
elif option == 2 :
    addExpense()

 elif option == 3 :
     budgetSummary()

 elif option == 4 :
   print("Thank you for using personal finance calculator!")
   break