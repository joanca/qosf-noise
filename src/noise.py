from qiskit.circuit.library import XGate, YGate, ZGate
from qiskit import QuantumCircuit
from qiskit.circuit import CircuitInstruction
from numpy.random import rand, choice


def add_pauli_noise(circuit: QuantumCircuit, a: float, b: float):
    """
    Adds Pauli noise to a given quantum circuit.

    Args:
        circuit: The quantum circuit to add noise to.
        a: Probability of applying a Pauli operator on a 1 qubit gate
        b: Probability of applying a Pauli operator on a 2 qubit gate

    Returns:
        The quantum circuit with added Pauli noise.
    """

    noisy_circuit = circuit.copy()

    for gate in circuit.data:
        gate: CircuitInstruction
        noisy_circuit.append(gate)

        random_number = rand()

        if gate.is_controlled_gate():
            if random_number < b:
                noisy_circuit.append(get_random_gate(), gate.qubits)

        else:
            if random_number < a:
                noisy_circuit.append(get_random_gate(), gate.qubits)

    return noisy_circuit


def get_random_gate():
    random_number = choice([0, 1, 2])
    gates = [XGate(), YGate(), ZGate()]

    return gates[random_number]
