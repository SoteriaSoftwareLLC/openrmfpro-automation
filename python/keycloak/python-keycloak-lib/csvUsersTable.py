from prettytable import from_csv

with open('users.csv') as file:
    table = from_csv(file)

print(table)