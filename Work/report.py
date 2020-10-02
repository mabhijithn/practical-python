# report.py
#
# Exercise 2.4
import csv
def read_portfolio(filename):
    '''
    

    Parameters
    ----------
    filename : string
        Name of CSV file.

    Returns
    -------
    A list of tuples consisting of stock name and share price

    '''
    portfolio = []
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]),float(row[2]))
            portfolio.append(holding)
    
    return(portfolio)

def read_prices(filename):
    '''
    

    Parameters
    ----------
    filename : string
        Name of CSV file.

    Returns
    -------
    A list of dictionaries with stock name and price.

    '''
    prices = {}
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row)>1:
                prices[row[0]] = float(row[1])
    
    return prices

pf_name = 'Data/portfolio.csv'
prices_fname = 'Data/prices.csv'

portfolio = read_portfolio(pf_name)
prices = read_prices(prices_fname)
cost = 0
curr_value = 0

for item in portfolio:
    stock = item[0]
    shares = item[1]
    cost += item[1]*item[2]
    print('Cost of ', stock,'=',item[2],'\t','Curr-price of ',stock,'=',prices[stock])
    curr_value += item[1]*prices[stock]

gain_loss = curr_value-cost
print('Gain/Loss = ', gain_loss)    