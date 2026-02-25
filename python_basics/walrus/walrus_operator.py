# python_walrus_operator.py
# A reference for the Assignment Expression (Walrus Operator :=) introduced in Python 3.8

# ---------------------------------------------------------
# 1. Streamlining 'if' Statements
# ---------------------------------------------------------
# The walrus operator allows you to calculate, assign, and check a condition in one line.
model_name = "Deep_Convolutional_Neural_Network_Model"

# Without Walrus:
# n = len(model_name)
# if n > 20: ...

# With Walrus:
if (n := len(model_name)) > 20:
    print(f"Model name is quite long ({n} characters).")

# ---------------------------------------------------------
# 2. Simplifying 'while' Loops (Interactive Input)
# ---------------------------------------------------------
# Eliminates the need to prompt the user before the loop and again inside the loop.
print("--- Training Log ---")
# Prompts for input, assigns it to 'batch_status', and checks if it's 'stop'
while (batch_status := input("Enter batch status (or 'stop' to end): ")) != "stop":
    print(f"Recorded: {batch_status}")

# ---------------------------------------------------------
# 3. Efficiency in List Comprehensions
# ---------------------------------------------------------
import math

def calculate_complex_metric(x):
    # Simulating a heavy calculation on a data point
    return math.sqrt(x) * 2.5

raw_scores = [10, 25, 3, 49, 1]

# We want to keep scores where the calculated metric is > 10, 
# and we want to store that calculated metric (not the raw score).
# The walrus prevents us from calling calculate_complex_metric(s) twice.

high_metrics = [metric_val for s in raw_scores if (metric_val := calculate_complex_metric(s)) > 10]
print(f"Filtered High Metrics: {high_metrics}")

# ---------------------------------------------------------
# 4. Reading Data or Files in Chunks
# ---------------------------------------------------------
# Useful for processing large datasets or logs that don't fit in memory.
# Note: This is a structural example; requires an actual file to run.

# with open("training_log.txt", "r") as log_file:
#     # Reads 1024 bytes, assigns to 'chunk', and continues as long as chunk is not empty
#     while (chunk := log_file.read(1024)):
#         print(f"Processing chunk of size: {len(chunk)} bytes")

# ---------------------------------------------------------
# 5. Filtering and Capturing Regex Matches
# ---------------------------------------------------------
import re

text_data = "Error: Validation loss spiked at epoch 42."
pattern = r"epoch (\d+)"

# Assigns the regex match object to 'match' and checks if it's valid in one go
if (match := re.search(pattern, text_data)) is not None:
    print(f"Anomaly detected at epoch number: {match.group(1)}")