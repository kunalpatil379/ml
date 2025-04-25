def hebbian_learning(inputs, targets, gate_name):
    print(f"\n=== Training {gate_name.upper()} Gate ===")
    weights = [0] * 3  # [w1, w2, bias]
    eta = 1

    for idx, (x, y) in enumerate(zip(inputs, targets)):
        print(f"\nSample {idx+1}: Input: {x}, Target: {y}")
        for i in range(3):
            weights[i] += eta * x[i] * y
        print(f"Updated Weights: {weights}")
    
    return weights

# Training data in bipolar format (-1, +1)
# x1, x2, bias (bias = +1)
inputs = [
    [-1, -1, 1],
    [-1, +1, 1],
    [+1, -1, 1],
    [+1, +1, 1]
]

# Targets in bipolar (-1 = false, +1 = true)
targets_and = [-1, -1, -1, +1]
targets_or  = [-1, +1, +1, +1]
targets_xor = [-1, +1, +1, -1]

# Train
weights_and = hebbian_learning(inputs, targets_and, "AND")
weights_or  = hebbian_learning(inputs, targets_or, "OR")
weights_xor = hebbian_learning(inputs, targets_xor, "XOR")

# Final Weights Summary
print("\n=== Final Weights Summary ===")
print(f"AND Gate Weights: {weights_and}")
print(f"OR  Gate Weights: {weights_or}")
print(f"XOR Gate Weights: {weights_xor} (should fail due to non-linearity)")
