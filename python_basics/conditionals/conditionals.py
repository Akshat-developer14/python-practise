# python_conditionals.py
# A complete reference for Python conditional statements

# ---------------------------------------------------------
# 1. Simple 'if' statement
# ---------------------------------------------------------
model_accuracy = 0.92

if model_accuracy >= 0.90:
    print(f"Model has achieved target accuracy {model_accuracy}. Ready for deployment.")

# ---------------------------------------------------------
# 2. 'if-else' statement
# ---------------------------------------------------------
dataset_size = 800

if dataset_size > 1000:
    print("Sufficient data for training a deep neural network.")
else:
    print("Warning: Dataset might be too small. Consider data augmentation.")

# ---------------------------------------------------------
# 3. 'if-elif-else' chain
# ---------------------------------------------------------
algorithm = "random_forest"

if algorithm == "linear_regression":
    print("Using a simple linear model.")
elif algorithm == "decision_tree":
    print("Using a tree-based model.")
elif algorithm == "random_forest":
    print("Using an ensemble method.")
else:
    print("Algorithm not recognized in the standard pipeline.")

# ---------------------------------------------------------
# 4. Nested Conditionals
# ---------------------------------------------------------
is_training = True
epochs = 50

if is_training:
    print("Model is currently in training mode.")
    if epochs > 100:
        print("Long training session detected. Monitoring for overfitting.")
    else:
        print("Standard training session length.")
else:
    print("Model is in inference mode.")

# ---------------------------------------------------------
# 5. Conditional Expressions (Ternary Operator)
# ---------------------------------------------------------
gpu_available = True

# Syntax: [value_if_true] if [condition] else [value_if_false]
device = "cuda" if gpu_available else "cpu"
print(f"Executing tensor operations on: {device}")

# ---------------------------------------------------------
# 6. Conditionals with Logical Operators (and, or, not)
# ---------------------------------------------------------
learning_rate = 0.01
optimizer = "adam"
has_missing_values = False

# 'and' requires both to be True
if learning_rate < 0.1 and optimizer == "adam":
    print("Standard hyperparameter configuration selected.")

# 'or' requires at least one to be True
if optimizer == "sgd" or optimizer == "adam":
    print("Valid optimizer selected.")

# 'not' reverses the boolean value
if not has_missing_values:
    print("Data is clean. Proceeding to feature engineering.")

# ---------------------------------------------------------
# 7. Conditionals with Membership ('in') and Identity ('is')
# ---------------------------------------------------------
supported_metrics = ["accuracy", "precision", "recall", "f1_score"]
selected_metric = "f1_score"
current_model = None

# 'in' checks for membership in a sequence
if selected_metric in supported_metrics:
    print(f"Metric '{selected_metric}' is supported by the evaluation module.")

# 'is' checks for object identity (useful for checking against None)
if current_model is None:
    print("No model loaded into memory. Please initialize a model first.")

# ---------------------------------------------------------
# 8. Structural Pattern Matching (match-case) - Python 3.10+
# ---------------------------------------------------------
http_status_code = 404

match http_status_code:
    case 200:
        print("API Request successful: Data fetched.")
    case 401 | 403:
        # The '|' acts as an 'or' in match-case patterns
        print("API Request failed: Authentication/Authorization error.")
    case 404:
        print("API Request failed: Endpoint not found.")
    case 500:
        print("API Request failed: Internal server error.")
    case _:
        # The '_' acts as the default/wildcard case
        print(f"Unhandled status code: {http_status_code}")