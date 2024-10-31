from qiskit import QuantumCircuit
from numpy.random import choice

from utils import get_random_gate


def add_pauli_noise(circuit: QuantumCircuit, a: float, b: float):
    """
    Adds Pauli noise to a given quantum circuit.

    Args:
        circuit: The quantum circuit to add noise to.
        a: Probability of Pauli noise after a one-qubit gate.
        b: Probability of Pauli noise after a two-qubit gate.

    Returns:
        The quantum circuit with added Pauli noise.
    """

    noisy_circuit = circuit.copy()

    for gate in circuit.data:
        gate_index = circuit.data.index(gate)

        if len(gate.qubits) == 2:  # Two-qubit gate
            if choice([True, False], p=[b, 1-b]):
                pauli_gate = get_random_gate()

                pauli_gate(noisy_circuit, gate_index)

        else:  # One-qubit gate
            if choice([True, False], p=[a, 1-a]):
                pauli_gate = get_random_gate()

                pauli_gate(noisy_circuit, gate_index)

    return noisy_circuit
