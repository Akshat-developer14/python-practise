# python_loops.py
# A complete reference for Python loops and iteration patterns

# ---------------------------------------------------------
# 1. The Standard 'for' Loop
# ---------------------------------------------------------
features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

# Iterating over a sequence (list)
for feature in features:
    print(f"Extracting and normalizing feature: {feature}")

# ---------------------------------------------------------
# 2. 'for' Loop with range()
# ---------------------------------------------------------
total_epochs = 5

# range(stop), range(start, stop), range(start, stop, step)
for epoch in range(1, total_epochs + 1):
    print(f"Training Epoch {epoch}/{total_epochs}...")

# ---------------------------------------------------------
# 3. The 'while' Loop
# ---------------------------------------------------------
# Loops as long as the condition remains True
current_loss = 1.5
target_loss = 0.5
iteration = 0

while current_loss > target_loss:
    iteration += 1
    current_loss -= 0.3  # Simulating gradient descent step
    print(f"Iteration {iteration}: Loss decreased to {current_loss:.2f}")

# ---------------------------------------------------------
# 4. Loop Control: 'break' (Early Stopping)
# ---------------------------------------------------------
# 'break' exits the loop completely
max_epochs = 100
validation_loss_history = [0.8, 0.75, 0.72, 0.70, 0.73, 0.75] # Loss went up!

for epoch in range(max_epochs):
    if epoch >= 4 and validation_loss_history[epoch] > validation_loss_history[epoch - 1]:
        print(f"Early stopping triggered at epoch {epoch}. Validation loss is increasing.")
        break

# ---------------------------------------------------------
# 5. Loop Control: 'continue' (Skipping Iterations)
# ---------------------------------------------------------
# 'continue' skips the rest of the current iteration and moves to the next
data_batch = ["valid_data", "corrupted_data", "valid_data", "missing_values", "valid_data"]

for batch in data_batch:
    if batch == "corrupted_data" or batch == "missing_values":
        print(f"Skipping bad batch: {batch}")
        continue
    print(f"Processing {batch} through the neural network.")

# ---------------------------------------------------------
# 6. Loop Control: 'pass' (Placeholder)
# ---------------------------------------------------------
# 'pass' does nothing. Useful as a placeholder for future code.
for item in features:
    # TODO: Implement feature scaling logic here later
    pass 

# ---------------------------------------------------------
# 7. The 'else' Clause in Loops
# ---------------------------------------------------------
# The 'else' block runs ONLY if the loop completes normally (no 'break' was hit)
training_interrupted = False

for step in range(3):
    if training_interrupted:
        print("Training was manually stopped.")
        break
    print(f"Processing step {step}...")
else:
    print("Success: Full training pipeline completed without interruptions.")

# ---------------------------------------------------------
# 8. Nested Loops (Grid Search Simulation)
# ---------------------------------------------------------
learning_rates = [0.01, 0.001]
batch_sizes = [32, 64]

print("Starting Hyperparameter Grid Search:")
for lr in learning_rates:
    for bs in batch_sizes:
        print(f"  -> Testing config: Learning Rate = {lr}, Batch Size = {bs}")

# ---------------------------------------------------------
# 9. Iterating with enumerate()
# ---------------------------------------------------------
# enumerate() gives you both the index and the value simultaneously
models = ["LogisticRegression", "RandomForest", "XGBoost"]

for index, model_name in enumerate(models, start=1):
    print(f"Model {index}: {model_name}")

# ---------------------------------------------------------
# 10. Iterating with zip()
# ---------------------------------------------------------
# zip() lets you iterate over multiple sequences in parallel
y_true = [1, 0, 1, 1]
y_pred = [0.9, 0.1, 0.8, 0.4]

for true_val, pred_val in zip(y_true, y_pred):
    prediction = 1 if pred_val > 0.5 else 0
    correct = "Correct" if prediction == true_val else "Wrong"
    print(f"Actual: {true_val} | Predicted: {prediction} | Result: {correct}")

# ---------------------------------------------------------
# 11. Comprehensions (Pythonic one-liner loops)
# ---------------------------------------------------------
# List Comprehension: concise way to create lists using a loop
raw_pixels = [255, 128, 0, 64]
normalized_pixels = [pixel / 255.0 for pixel in raw_pixels]
print(f"Normalized pixels: {normalized_pixels}")

# Dictionary Comprehension: concise way to create dictionaries
feature_importance = {"age": 0.25, "income": 0.45, "education": 0.30}
# Filtering out low importance features via loop comprehension
high_importance = {k: v for k, v in feature_importance.items() if v > 0.25}
print(f"Top features: {high_importance}")