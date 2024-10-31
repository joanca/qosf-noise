from qiskit import QuantumCircuit, QuantumRegister
import numpy as np


def qft(circuit: QuantumCircuit, register: QuantumRegister) -> QuantumCircuit:
    """
    Applies the Quantum Fourier Transform (QFT) to a quantum circuit.

    Args:
        circuit: The quantum circuit to apply QFT to.
        num_qubits: The number of qubits in the circuit.
    """

    num_qubits_register = len(register)

    for i in range(num_qubits_register):
        # applying the Hadamard gate to each qubit starting from the
        # least significant qubit
        circuit.h(register[num_qubits_register - i - 1])

        # apply controlled rotations to qubits on the right of the j-th qubit
        for j in range(i + 1, num_qubits_register):
            angle_denominator = (2 ** (j - i + 1))
            angle = 2 * np.pi / angle_denominator

            control = register[num_qubits_register - j - 1]
            target = register[num_qubits_register - i - 1]

            circuit.crz(angle, control, target)

    return circuit


def apply_inverse_qft(circuit: QuantumCircuit, register: QuantumRegister) -> QuantumCircuit:
    """
    Applies the Inverse Quantum Fourier Transform (QFT) to a quantum circuit.

    Args:
        circuit: The quantum circuit to apply the inverse QFT to.
        num_qubits: The number of qubits in the circuit.
    """

    num_qubits_register = len(register)

    for i in range(num_qubits_register):
        for j in range(i):
            angle_denominator = (2 ** ((num_qubits_register - j) -
                                       (num_qubits_register - i - 1)))
            angle = -(2 * np.pi) / angle_denominator

            control = register[j]
            target = register[i]

            circuit.crz(angle, control, target)

        # applying the Hadamard gate to each qubit starting from the
        # most significant qubit
        circuit.h(i)

    return circuit
