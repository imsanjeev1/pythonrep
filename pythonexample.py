# Keyword and Non-keyword example
	
def func(required_arg, *args, **kwargs):
    # required_arg is a positional-only parameter.
    print(required_arg)

    # args is a tuple of positional arguments,
    # because the parameter name has * prepended.
    if args: # If args is not empty.
        print(args)

    # kwargs is a dictionary of keyword arguments,
    # because the parameter name has ** prepended.
    if kwargs: # If kwargs is not empty.
        print(kwargs)

#func()


#func("required argument", 1, 2, '3')

func("required argument", 1, 2, '3', keyword1=4, keyword2="foo")

#---------------End keyword arugument and  nonkeyword argument----------------

#-------------------Decorator Example-----------------
def repeater(old_function):
    def new_function(*args, **kwds):
        print('test')
        old_function(*args, **kwds) 
        old_function(*args, **kwds)
    return new_function 
	
@repeater
def Multiply(num1, num2):
	print(num1*num2)
	
Multiply(2, 3)

@repeater
def add(num1, num2):
	print(num1+num2)
	
add(4, 5)

#------------------End Decorator ------------------------

# Closure : A closure is a function object that remembers value in enclosing scopes even if they are not present in memory..
# ADVANTAGE : Closures can avoid use of global variables and provides some form of data hiding.
#-------------------------Closure Example start here-------------------------
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)


#-------------------------------End Closure--------------------


#---------------------Generators---------------------------

#Generators are simple functions which return an iterable set of items, one at a time

import random

def lottery():
    # returns 6 numbers between 1 and 40
  for i in range(6):
    yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,5)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))
	   
	   
# Generators Fibonic series example 


def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break


#-------------------End-------------------------------


#---------------------Pandas DataFrames----------------

# Pandas and DataFrames : Pandas is a high-level data manipulation tool. It is built on the Numpy package and its key data structure is called the DataFrame. DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.


dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)

#print(brics) # Display the columns and rows in tabular form
# Change index of tabular in pandas

# As you can see with the new brics DataFrame, Pandas has assigned a key for each country as the numerical values 0 through 4. If you would like to have different index values, say, the two letter country code, you can do that easily as well

brics.index = ["BR", "RU", "IN", "CH", "SA"]

print(brics)


# Another way to create a DataFrame is by importing a csv file using Pandas. Now, the csv

stocks = pd.read_csv('stock.csv') # Displayed all csv files
print('Display all record', stocks)
# Indexing DataFrames :: There are several ways to index a Pandas DataFrame. One of the easiest ways to do this is by using square bracket notation.

#In the example below, you can use square brackets to select one column of the stocks DataFrame. You can either use a single bracket or a double bracket. The single bracket with output a Pandas Series, while a double bracket will output a Pandas DataFrame.

stocks = pd.read_csv('stock.csv', index_col = 0)

# Print out MSFT column as Pandas Series ,below is the syntax
print('Pandas Series', stocks[['MSFT']])

# Print out MSFT column as Pandas DataFrame

print('Pandas DataFrame', stocks[['MSFT']])

# Print out DataFrame with SPX and MSFT columns

print('Get Columns based rescord', stocks[['MSFT', 'SPX']])

# Square brackets can also be used to access observations (rows) from a DataFrame. For example:

# Print out first 4 observations

print('First 4 Observation::', stocks[0:4])

# Print out fifth, sixth, and seventh observation

print('Get Fifth,Sixth and seventh Observation', stocks[4:6])

# Print out observation for MSFT

print('Get MSFT Observation', stocks.iloc[2])

# Print out observations for SPX and MSFT

#print(stocks.loc[['SPX', 'MSFT']])
