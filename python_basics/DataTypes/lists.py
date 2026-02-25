'''
List:
    list in python are mutable arrays can contain multiple datatypes.
'''

ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")

chai_ingredients.reverse()
print(f"{chai_ingredients}")

chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print (f"Maximum sugar level: {max(sugar_levels)}")
print (f"Minimum sugar level: {min(sugar_levels)}")

#operator overloading
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ['black tea', 'water'] * 3
print(f"Strong brew: {strong_brew}")

# Working with bytearray
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data_changed = raw_spice_data.replace(b"CINN", b"CARD")
print(f"Working with bytearray:\n   {raw_spice_data}\nAfter some changes:\n   {raw_spice_data_changed}")