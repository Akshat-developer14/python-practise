"""
Advanced Datatypes in Python
Demonstrates: Array, Deque, Counter, OrderedDict, defaultdict, namedtuple
"""

from collections import namedtuple, deque, Counter, OrderedDict, defaultdict
import arrow

# ============================================================================
# 1. NAMEDTUPLE - Structured data with named fields
# ============================================================================
ChaiProfile = namedtuple('ChaiProfile', ['flavour', 'spices', 'milk'])

chai1 = ChaiProfile(flavour='Masala', spices=['cardamom', 'cinnamon'], milk='whole')
chai2 = ChaiProfile(flavour='Ginger', spices=['ginger', 'clove'], milk='almond')

print("=== NAMEDTUPLE ===")
print(f"Chai 1: {chai1}")
print(f"Chai 1 Flavour: {chai1.flavour}\n")

# ============================================================================
# 2. DEQUE - Double-ended queue for efficient insertions/deletions
# ============================================================================
print("=== DEQUE ===")
chai_queue = deque(['Masala', 'Ginger', 'Turmeric'], maxlen=5)
chai_queue.appendleft('Cardamom')  # Add to left
chai_queue.append('Honey')          # Add to right
print(f"Chai Queue: {chai_queue}\n")

# ============================================================================
# 3. COUNTER - Count occurrences of elements
# ============================================================================
print("=== COUNTER ===")
chai_orders = ['Masala', 'Ginger', 'Masala', 'Turmeric', 'Masala', 'Ginger']
order_count = Counter(chai_orders)
print(f"Order Count: {order_count}")
print(f"Most Common: {order_count.most_common(2)}\n")

# ============================================================================
# 4. ORDEREDDICT - Dictionary maintaining insertion order (Python 3.7+ default)
# ============================================================================
print("=== ORDEREDDICT ===")
chai_recipe = OrderedDict()
chai_recipe['water'] = '2 cups'
chai_recipe['tea_leaves'] = '2 tsp'
chai_recipe['spices'] = ['ginger', 'cardamom']
chai_recipe['milk'] = '1 cup'
print(f"Chai Recipe (ordered): {chai_recipe}\n")

# ============================================================================
# 5. DEFAULTDICT - Dictionary with default values for missing keys
# ============================================================================
print("=== DEFAULTDICT ===")
chai_inventory = defaultdict(int)
chai_inventory['Masala'] += 10
chai_inventory['Ginger'] += 5
chai_inventory['Masala'] += 3
print(f"Chai Inventory: {dict(chai_inventory)}")
print(f"Missing item (default 0): {chai_inventory['Turmeric']}\n")

# ============================================================================
# 6. ARRAY - Typed array for efficient storage
# ============================================================================
print("=== ARRAY ===")
import array
chai_ratings = array.array('f', [4.5, 4.8, 4.2, 4.9, 4.6])
print(f"Chai Ratings: {chai_ratings}")
print(f"Average Rating: {sum(chai_ratings) / len(chai_ratings):.2f}\n")

# ============================================================================
# 7. ARROW - Time handling (Bonus)
# ============================================================================
print("=== ARROW TIME HANDLING ===")
brewing_time = arrow.utcnow()
print(f"Brewing time (UTC): {brewing_time}")

brewing_time_paris = brewing_time.to("Europe/Paris")
print(f"Brewing time in Paris: {brewing_time_paris}\n")

# ============================================================================
# PRACTICAL EXAMPLE: Chai Shop Management
# ============================================================================
print("=== CHAI SHOP MANAGEMENT SYSTEM ===")

# Store chai profiles
menu = {
    'Masala': ChaiProfile('Masala', ['cardamom', 'cinnamon', 'ginger'], 'whole'),
    'Ginger': ChaiProfile('Ginger', ['ginger', 'clove'], 'almond'),
}

# Track daily sales
daily_sales = Counter()
daily_sales.update(['Masala', 'Ginger', 'Masala', 'Masala'])

print(f"Menu: {list(menu.keys())}")
print(f"Daily Sales: {dict(daily_sales)}")
print(f"Top Seller: {daily_sales.most_common(1)}")