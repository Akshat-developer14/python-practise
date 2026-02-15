'''
Docstring for python_basics.DataTypes.datatypes

In python number is immutable but variable is mutable.
'''

# Here we are assigning to 2 number to amount
amount = 2
print(amount)

# Here we are changing amount containing reference from 2 to 12, not making 2 to 12
amount = 12
print(amount)

print(f'Id of 2: {id(2)}')
print(f'Id of 12: {id(12)}')