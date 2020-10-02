# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    f = open(filename,'rt')
    headers = next(f)
    headers = headers.strip()
    cost = 0
    for line in f:
        row = line.strip().split(',')
        cost = cost+float(row[1])*float(row[2])
    f.close()
    return(cost) 
    
filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print(cost)