# Dictionary to store expenses and payments
expenses = {
    'Alice': 100,   # Alice spent 100
    'Bob': 50,      # Bob spent 50
    'Carl': 80      # Carl spent 80
}

payments = {
    'Alice': 30,    # Alice paid 30
    'Bob': 70,      # Bob paid 70
    'Carl': 130     # Carl paid 130
}

# Calculate the total expenses and payments for each person
totals = {}
for person in expenses.keys():
    totals[person] = expenses[person] - payments[person]

# Calculate the total amount each person needs to pay/receive
for person in totals:
    if totals[person] > 0:
        print(f'{person} needs to receive {totals[person]}')
    elif totals[person] < 0:
        print(f'{person} needs to pay {-totals[person]}')
    else:
        print(f'{person} is settled')