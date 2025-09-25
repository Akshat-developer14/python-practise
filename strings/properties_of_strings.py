"""
Properties of strings:-

"""
print("\nAccessing characters in string: \n")
s = "Python"
print('s[0]: ',s[0])    # 'P'
print('s[-1]: ',s[-1])   # 'n'

print("\nIterating through string using for loop: \n")
index = 0
for ch in s: 
    print(f"character {index}: ",ch)
    index += 1

print("\nSlicing a string: \n")
s1 = "GeeksforGeeks"
print('s1[1:5]: ', s1[1:5])    # 'eeks'
print('s1[:4]: ', s1[:4])     # 'Geek'
print('s1[5:]: ', s1[5:])     # 'forGeeks'
print('s1[::-1]', s1[::-1])   # 'skeeGrofskeeG' (reverse)

print("\nString methods: \n")
