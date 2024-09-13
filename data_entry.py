from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I":"Income", "E":"Expense"}

def get_date(prompt, allow_defualt=False):
    date_str = input(prompt)
    if allow_defualt and not date_str:
        return datetime.today().strftime(date_format)

    try:
        valid_date = datetime.strptime(date_str,date_format)
        return  valid_date.strftime(date_format)

    except ValueError:
        print("Invalid date Format. Please enter the date in \n dd-mm-yyyy format")
        return get_date(prompt, allow_defualt)


def get_amount():

    try:
        amount = float(input("Enter The Amount:"))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return  amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the Category('I' for Income or 'E' for Expense)").upper()
    if category in CATEGORIES:
        return  CATEGORIES[category]
    print("invalid Category. Please enter 'I' for Income or 'E' For Expense.")
    return get_category()


def get_description():
    return  input("Enter a description ")


