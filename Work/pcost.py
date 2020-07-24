# pcost.py
#
# Exercise 1.27
Totalcost = 0
with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        row = line.split(',')
        # print(row)
        Totalcost+=int(row[1])*float(row[2])

print('Total cost ',Totalcost)