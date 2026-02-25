'''
Set:
    Set in python are mutable but the elements in set are immutable.
    Set is unordered collection of unique elements.
    Set is represented by -> {}
    Set is used to remove duplicate elements.
    Set is used to perform mathematical operations like union, intersection, difference, symmetric difference.
'''

essential_spices = {'cumin', 'ginger', 'cardamom', 'cumin'}
print(f'Essential spices: {essential_spices}') # duplicates are removed and order is not preserved, only unique elements are stored and the duplicate only one element is stored

optional_spices = {'cloves', 'pepper', 'ginger', 'turmeric'}

# Union of two sets
all_spices = essential_spices | optional_spices
print(f'All spices (Union): {all_spices}') # it will return all the elements from both the sets without any duplicates

# Intersection of two sets
common_spices = essential_spices & optional_spices
print(f'Common spices (Intersection): {common_spices}') # it will return the elements which are common in both the sets

# Difference of two sets
unique_spices = essential_spices - optional_spices
print(f'Unique spices (Difference): {unique_spices}') # it will return the elements which are in essential_spices but not in optional_spices

# Symmetric difference of two sets
unique_spices = essential_spices ^ optional_spices
print(f'Unique spices (Symmetric Difference): {unique_spices}') # it will return the elements which are not common in both the sets

# Set membership test
print(f"Is 'cloves' in essential spices? {'cloves' in optional_spices}") # it will return True if the element is present in the set else False

# Frozenset
frozen_spices = frozenset(essential_spices) # it will freeze the set and make it immutable
print(frozen_spices)

# Try to add element in frozenset
# frozen_spices.add('cinnamon') # it will throw an error because frozenset is immutable