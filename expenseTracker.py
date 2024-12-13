# 1104 Assignment 2
# Natalia Bohulevych
# 100709035

# import libraries
import json, os
from datetime import datetime
import matplotlib.pyplot as plt


# Function to write expenses to JSON file
def writeExp(data, expenses):
    with open(data, "w") as file:
        json.dump(expenses, file, indent=4)  # Save the list of expenses in JSON format


# Function to add a new expense
def add_expense(data, expenses):
    format = "%d-%m-%Y"

    # prompt user for date
    date = input("Press enter for today's date\nor enter expense date (DD-MM-YYYY): ").strip()
    # validate date entry
    if not date:
        date = datetime.now().strftime("%d-%m-%Y")  # if no date is entered default to today's date
    try: # check if date is in the correct format
        datetime.strptime(date, format)
    except ValueError:
        return(print("Invlalid date format!")) 
   
    # prompt user for category
    category = input("Enter expense category: ").lower()
    if not category:
        return(print("Category cannot be empty."))
    
    # prompt user for expense amount
    amount = input("Enter expense amount: ")
    # check if amount is positive, throw exception if not
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        return(print("Invalid input. Must enter a positive number."))

    # Add new expense and save file
    expenses.append({"date": date, "category": category, "amount": amount})
    writeExp(data, expenses)
    print("Expense added successfully!")
    
# function to delete expenses (not actually implemented yet)    
def delete(expenses):
    print("Delete expense is coming soon!\nIn the mean time please manually edit the expenses.json file.")


# Function to view all expenses in terminal
def view_expenses(expenses):
    if not expenses:
        print("No expenses to display.")
        return

    print("\nRecorded Expenses:")
    print("{:<15} {:<20} {:<10}".format("Date", "Category", "Amount"))
    print("*" * 45)
    for expense in expenses:
        print("{:<15} {:<20} {:<10.2f}".format(expense["date"], expense["category"], expense["amount"]))
    print("*" * 45)


# Function to generate visual chart using matplotlib
def visualize_expenses(expenses):
    if not expenses:
        print("No expenses to visualize.")
        return

    # sort and merge expenses by category
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount

    # Prepare data for pie chart
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    # Plot the pie chart
    plt.figure(figsize=(10, 10)) # size window
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=90) # add categories and percentage values and format to one decimal place
    plt.title("Expense Distribution")
    plt.axis("equal")  # circle
    plt.show() # display chart
    return


# MAIN PROGRAM
# File to store expenses
data = "Week10/expenses.json"
with open(data, 'r') as file:
    expenses = json.load(file)

    # Initialize choice to empty, keep looping until user exits with option 5
choice = ""
while choice != "5":
    # Main menu
    print("\n--- Daily Expense Tracker ---")
    print("1. Add an Expense")
    print("2. View All Expenses")
    print("3. Visualize Expenses")
    print("4. Delete Expense")
    print("5. Exit")
    choice = input("Choose an option: ")

        # check choices and called respective function
    if choice == "1":
        add_expense(data, expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        visualize_expenses(expenses)
    elif choice == "4":
        delete(expenses)
    elif choice == "5":
        print("Thank you for using the Daily Expense Tracker!")
    else:
        print("Invalid choice. Please try again.")


# validating date (try/catch statements) from geeksforgeeks
    # https://www.geeksforgeeks.org/python-validate-string-date-format/

# displaying and formatting to terminal from pwskills
    # https://pwskills.com/blog/2f-in-python-what-does-it-mean/

# learned entire matplotlib part from 
    # https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
    # https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html