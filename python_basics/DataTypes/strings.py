'''
Strings:

Stings in python is immutable, so they always create a new reference
'''

f_string = "Hi i love python"

print(f_string)

print(f'Let\'s print in slicing of above string: {f_string[3:9]}')

print(f'Reverse string: {f_string[::-1]}\n')

print('-----Encoded Label-----')

label_text = 'Python is very vàrsàtile'
encoded_label = label_text.encode('utf-8')

decoded_label = encoded_label.decode('utf-8')
print(f'''
Non encoded label: {label_text}

Encoded label: {encoded_label}

Decoded label: {decoded_label}
''')