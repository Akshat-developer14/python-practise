'''
Tuples:
tuples in python are immutable datatype, represented by -> ()
It can store multiple variables of different datatypes
'''

menu = ('cardmon', 'ginger', 'blackpeper')

(s1, s2, s3) = menu

print(f'Here is the menu: {s1}, {s2}, {s3}')

#python allows us to write tuple without ()

r1 , r2 = 2, 1

print(f'\nRatio is {r1}:{r2}')

r1, r2 = r2, r1

print(f'\nFliped Ratio is {r1}:{r2}')

print(f'Does ginger in menu? \n {'ginger' in menu}')