# Author: ChatGPT
# Description: 
#   This script averages multiple IR signals, detects errors based on pulse count and the largest variances,
#   and outputs the result in a format suitable for inclusion in a JSON file.
#   To use:
#     1. Paste the sample data captured from the receiver (receiver/code.py).
#     2. Press Enter twice to signal the termination of the input data.
#     3. Enter a name for the resulting data to be used in the JSON format.

import re

print("Paste your input (end with an empty line):")
lines = []
while True:
    try:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    except EOFError:
        break

input_text = "\n".join(lines)

# Find all "Heard X Pulses" blocks
matches = re.findall(r'Heard (\d+) Pulses: \[([^\]]+)\]', input_text)

if not matches:
    print("No valid pulse entries found.")
    exit()

# Determine base length from the first match
base_length = int(matches[0][0])
print(f"Detected base pulse count: {base_length}")

pulses = []
for idx, (count_str, pulse_str) in enumerate(matches):
    pulse_values = list(map(int, pulse_str.split(',')))
    if len(pulse_values) != base_length:
        print(f"Error: Entry {idx + 1} has {len(pulse_values)} pulses, expected {base_length}.")
        exit()
    pulses.append(pulse_values)

# Compute average per index and find variances
averaged = []
max_variance = []

for i in range(base_length):
    col = [p[i] for p in pulses]
    avg = round(sum(col) / len(col))
    variances = [abs(p[i] - avg) for p in pulses]
    max_variance.append((i, max(variances)))  # Store index and max variance

# Sort max variance by value, descending, and get the top 3
top_variances = sorted(max_variance, key=lambda x: x[1], reverse=True)[:3]

# Display top 3 largest variances
print("\nTop 3 largest variances (index:variance):")
for idx, var in top_variances:
    print(f"[{idx}: {var}]")

# Compute the average for each pulse index
averaged = [
    round(sum(p[i] for p in pulses) / len(pulses))
    for i in range(base_length)
]

# Prompt for name
name = input("\nEnter a name for this signal: ").strip()

# Output final result
print(f'\n    "{name}": [{", ".join(map(str, averaged))}],')
