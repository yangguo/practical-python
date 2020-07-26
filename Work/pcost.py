# pcost.py
#
# Exercise 1.27
# Totalcost = 0
# with open('Data/portfolio.csv', 'rt') as f:
#     next(f)
#     for line in f:
#         row = line.split(',')
#         # print(row)
#         Totalcost+=int(row[1])*float(row[2])
import csv
import sys

def portfolio_cost(filename):
    Totalcost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            # row = line.split(',')
            # print(row)
            try:
                Totalcost+=int(row[1])*float(row[2])
            except ValueError:
                print('value error')
    return Totalcost

if len(sys.argv)==2:
    filename = sys.argv[1]
else:
    filename='Data/portfolio.csv'

Totalcost = portfolio_cost(filename)
print('Total cost ',Totalcost)