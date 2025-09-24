'''

2. array Module (homogeneous arrays)

- Provides a true array type with all elements of the same type.
- More memory-efficient than lists for large datasets of uniform type.
- Requires specifying a typecode (e.g., 'i' for integers, 'f' for floats)

'''

import array as arr

a = arr.array('i', [1, 2, 3])
a.append(5)
print(a)   # array('i', [1, 2, 3, 5])

