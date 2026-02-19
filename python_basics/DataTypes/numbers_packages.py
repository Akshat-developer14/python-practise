from decimal import Decimal, getcontext
from fractions import Fraction

# 1. Setup Decimal Precision
# Setting global precision to 6 significant digits
getcontext().prec = 6


print("--- 1. The Floating Point Problem ---")
a, b = 0.1, 0.2
float_sum = a + b
print(f"Standard Float (0.1 + 0.2): {float_sum}") 
# Output: 0.30000000000000004

print("\n--- 2. The Decimal Solution (Best for Money) ---")
# ALWAYS pass numbers as strings to Decimal to avoid float issues
dec_a = Decimal('0.1')
dec_b = Decimal('0.2')
decimal_sum = dec_a + dec_b
print(f"Decimal Sum: {decimal_sum}") 
    # Output: 0.3
    
# Demonstration of precision limit set above (6 digits)
div_result = Decimal('1') / Decimal('7')
print(f"1 / 7 with precision 6: {div_result}")

print("\n--- 3. The Fraction Solution (Best for Ratios) ---")
# Keeps numbers as numerator/denominator (no rounding at all)
f1 = Fraction(1, 3)
f2 = Fraction(1, 6)
fraction_sum = f1 + f2
    
print(f"Fraction: 1/3 + 1/6 = {fraction_sum}") 
# Output: 1/2
print(f"Fraction as Float: {float(fraction_sum)}")

print("\n--- 4. Practical Comparison Table ---")
print(f"{'Method':<15} | {'Result of 1/3':<20}")
print("-" * 40)
print(f"{'Float':<15} | {1/3}")
print(f"{'Decimal':<15} | {Decimal(1)/Decimal(3)}")
print(f"{'Fraction':<15} | {Fraction(1, 3)}")
