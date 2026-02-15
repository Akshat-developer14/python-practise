'''
Docstring for python_basics.DataTypes.numbers

In python there are different types of numbers 
    - Intergers
    - Boolean -> Generally False or True but can be accessed as a number in 0 or 1
    - Float -> decimal
    - Complex Number
'''

# Integer

num = 12
neg_num = -45

num2 = 12

# Boolean

true_b = True
false_b = False

# Float

float_num = 3.14
neg_float_num = -3.14

# Complex Numbers

complex_num = 3 + 4j

print(f'''
Integer: {num}
Negative Integer: {neg_num}

In Boolean:-
Boolean true: {true_b}
Boolean false: {false_b}

Boolean in number:-
Boolean true: {int(true_b)}
Boolean false: {int(false_b)}

Float:-
Float: {float_num}
Negative Float: {neg_float_num}

Complex Number: {complex_num}

Some operations on numbers:-

Addition of {num} and 10 is {num + 10}

Subtraction of {num} and 30 is {num - 30}

Multiplication of {num} and 10 is {num * 10}

Division of {num} and 10 is {num / 10}

Modulus of {num} and 10 is {num % 10}

Exponential of {num} and 2 is {num ** 2}

Floor division of {num} and 10 is {num // 10}

{'Integer one is equal to integer two' if num == num2 else 'Integer one is not equal to integer two'}
''')