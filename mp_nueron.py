def mp_neuron(inputs, weights, threshold):
    output = []
    for x in inputs:
        net_input = sum(i * w for i, w in zip(x, weights))
        output.append(1 if net_input >= threshold else 0)
    return output

# 1️⃣ AND Gate
and_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
and_weights = [1, 1]
and_threshold = 2
and_output = mp_neuron(and_inputs, and_weights, and_threshold)
print("AND Gate:", and_output)

# 2️⃣ OR Gate
or_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
or_weights = [1, 1]
or_threshold = 1
or_output = mp_neuron(or_inputs, or_weights, or_threshold)
print("OR Gate:", or_output)

# 3️⃣ NOT Gate (single input)
def not_gate(inputs):
    output = []
    for x in inputs:
        output.append(1 if x == 0 else 0)
    return output

not_inputs = [0, 1]
not_output = not_gate(not_inputs)
print("NOT Gate:", not_output)

# 4️⃣ XOR Gate (Just for visualization — not learnable by MP neuron)
def xor_gate(inputs):
    output = []
    for x in inputs:
        output.append(1 if x[0] != x[1] else 0)
    return output

xor_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
xor_output = xor_gate(xor_inputs)
print("XOR Gate:", xor_output)
