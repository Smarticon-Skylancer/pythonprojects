# Setting all outputs to 0 so we can easilly add what the user inputs to it
totalIncome = 0
essentialExpense = 0
noneEssential =0
totalexpenses = 0
remainingBudget = 0
# Function for Adding Income
def addIncome():
	income = float(input("Enter income : "))
	totalIncome =+ income
	print(totalIncome)
def addExpense():
	expenses = float(input('Enter Expenses : '))
# Checks whether or not Expenses are less than income
	totalExpenses =+ expenses
	if totalExpenses < totalIncome:
		remainingBudget= totalIncome -totalExpenses
# Checks the type of the Expense
		option = input("Enter expense Category (essential/non-essential : )").lower()
		if option == "essential":
			essentialExpense += totalExpenses
		elif option == "nonessential":
			noneEssential += totalExpenses
		else:
			print("Invalid parameters passed please check your input and try again")
	else:
		print('Sorry your expenses are above your income try again')
# Function for Budget Summary Generation
def budgetSummary():
	print('Budget Summary : ')
	print(f'Income : £{totalIncome}')
	print(f'Total Expenses : £{expenses} ')
	print(f'Remaing Budget : £{remainingBudget}')
#checks for saving Eligibility using remaining Budget as criterion
	if remainingBudget >=1000:
		save = (remainingBudget*0.5)
		print(f'Your are Under Budget consider saving {save}')
		print(f'Essential Expense : £{essentialExpense} ')
		print(f'Non-essential Expense : £{noneEssential} ')
#Program starts here
print('Welcome to Smart Finance Manager')
# iterates while loop
while True:
	# Menu of choices
	print("""
	1. Enter Income
	2. Add Expenses
	3. Veiw Budget Summary
	4. Exit
	""")
# Choice checking 
	choice = int(input('Enter Choice of Operation : '))
	if choice == 1:
		addIncome()
		print(totalIncome)
	elif choice == 2:
		addExpense()
	elif choice == 3:
		budgetSummary()
	elif choice == 4:
			print('Thanks for Using Smart Finance Manager !')
			break
			
		
	