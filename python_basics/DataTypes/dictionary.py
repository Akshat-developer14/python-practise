'''
Dictionary:
    Dictionary in python are mutable and represented by -> {}
    Dictionary is used to store key-value pairs.
    Dictionary is used to perform operations like get, set, delete, update.
    Dictionary also has methods like keys(), values(), items(), pop(), popitem(), clear(), update(), get(), setdefault(), fromkeys()
    Dictionary is unordered.
    Dictionary is not indexed.
    Dictionary also supports the methods like Union(|), Intersection(&), Difference(-), Symmetric Difference(^).
'''
print("\n--------------------  Dictionary  --------------------\n")
chai_order = {
    "size": "medium",
    "spices": ["ginger", "cardamom"],
    "milk_type": "almond"
}
# dictionary can also be in this syntax
chai_order_dict = dict(size="medium", spices=["ginger", "cardamom"], milk_type="almond")

print(f"\nChai order: {chai_order}\nChai order dict: {chai_order_dict}")

# Empty dictionary
chai_recipe = {}

# Adding elements to dictionary
chai_recipe['type'] = 'black tea'
chai_recipe['liquid base'] = 'milk'
chai_recipe['spices'] = ['ginger', 'cardamom']
chai_recipe['sugar'] = 2

print(f"\nChai recipe: {chai_recipe}")
print(f"\nRecipe liquid base: {chai_recipe['liquid base']}")

# Deleting a element
del(chai_recipe['liquid base'])
print(f"\nChai recipe after deleting a element: {chai_recipe}")

# Membership test
print(f"\nIs 'sugar' in chai recipe? {'sugar' in chai_recipe}")

# Dictionary methods
print(f"\nChai recipe keys: {chai_recipe.keys()}")
print(f"Chai recipe values: {chai_recipe.values()}")
print(f"Chai recipe items: {chai_recipe.items()}")

# Pop item
last_item = chai_recipe.popitem()
print(f"\nRemoved Last item: {last_item}")

# Update dictionary
extra_spices = {'spices': ['cinnamon', 'cloves']}
chai_recipe.update(extra_spices)
print(f"\nChai recipe after updating: {chai_recipe}")

# Get value (two ways)
print(f"\nGet value of spices: {chai_recipe['spices']}")
print(f"\nGet value of spices: {chai_recipe.get('spices')}")

# Clear dictionary
chai_recipe.clear()
print(f"\nChai recipe after clearing: {chai_recipe}")