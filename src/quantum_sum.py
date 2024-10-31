from qiskit import QuantumCircuit
import numpy as np

from fourier_transform import apply_qft, apply_inverse_qft


def quantum_sum(a: int, b: int) -> QuantumCircuit:
    # Determine the number of qubits required
    num_qubits = max(a.bit_length(), b.bit_length())

    circuit = QuantumCircuit(2*num_qubits+1, num_qubits+1)

    # Encode the numbers
    for i in range(num_qubits):
        if (a >> i) & 1:
            circuit.x(i)
        if (b >> i) & 1:
            circuit.x(i+num_qubits)

    # Apply Hadamard gates to the first register
    circuit.h(range(num_qubits))

    # Apply QFT to the first register
    apply_qft(circuit, range(num_qubits))

    # Controlled rotations for addition
    for i in range(num_qubits):
        circuit.crz(np.pi / 2**(num_qubits-i), num_qubits, i)

    # Apply inverse QFT to the first register
    apply_inverse_qft(circuit, range(num_qubits))

    # Measure the result
    circuit.measure(range(num_qubits), range(num_qubits))

    return circuit
