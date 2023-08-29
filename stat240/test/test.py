p_1_5 = 0.1  # probability for numbers 1 through 5
p_6 = 0.5  # probability for number 6

# Expected value calculation
expected_value = sum([i * p_1_5 for i in range(1, 6)]) + 6 * p_6

# Round to 1 decimal place
expected_value_rounded = round(expected_value, 1)

print(expected_value_rounded)