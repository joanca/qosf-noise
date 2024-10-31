from qiskit import QuantumCircuit

from noise import add_pauli_noise
from decompose_basis import decompose_into_basis
from quantum_sum import quantum_sum

circuit = QuantumCircuit(2)

circuit.h(1)

circuit.z(0)
print(circuit)

noisy_circuit = add_pauli_noise(circuit, 0.1, 0.8)

print(noisy_circuit)

decomposed_circuit = decompose_into_basis(circuit)

print(decomposed_circuit)

quantum_sum = quantum_sum(1, 3)

print(quantum_sum)
