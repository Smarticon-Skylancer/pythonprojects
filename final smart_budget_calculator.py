# Initialize variables
totalIncome = 0
essentialExpense = 0
nonEssential = 0  # Standardized variable name
totalExpenses = 0
remainingBudget = 0

# Function for Adding Income
def addIncome():
    global totalIncome
    try:
        income = float(input("Enter income: "))
        totalIncome += income
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Function for Adding Expenses
def addExpense():
    global totalExpenses, essentialExpense, nonEssential, remainingBudget
    try:
        expenses = float(input("Enter Expenses: "))
        totalExpenses += expenses
        if totalExpenses <= totalIncome:  # Allow expenses up to income
            remainingBudget = totalIncome - totalExpenses
            option = input("Enter expense Category (essential/non-essential): ").lower()
            if option == "essential":
                essentialExpense += expenses  # Add individual expense
            elif option == "non-essential":  # Consistent with input prompt
                nonEssential += expenses
            else:
                print("Invalid category! Please enter 'essential' or 'non-essential'.")
        else:
            print("Sorry, your expenses exceed your income. Try again.")
            totalExpenses -= expenses  # Revert the addition
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Function for Budget Summary Generation
def budgetSummary():
    print("\nBudget Summary:")
    print(f"Income: £{totalIncome}")
    print(f"Total Expenses: £{totalExpenses}")
    print(f"Remaining Budget: £{remainingBudget}")
    print(f"Essential Expenses: £{essentialExpense}")
    print(f"Non-essential Expenses: £{nonEssential}")
    if remainingBudget >= 1000:
        save = remainingBudget * 0.5
        print(f"You are under budget! Consider saving £{save}")

# Program starts here
print("Welcome to Smart Finance Manager")

# Main loop
while True:
    # Menu of choices
    print("""
    1. Enter Income
    2. Add Expenses
    3. View Budget Summary
    4. Exit
    """)
    try:
        choice = int(input("Enter Choice of Operation: "))
        if choice == 1:
            addIncome()
        elif choice == 2:
            addExpense()
        elif choice == 3:
            budgetSummary()
        elif choice == 4:
            print("Thanks for Using Smart Finance Manager!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")
    except ValueError:
        print("Invalid input! Please enter a number.")