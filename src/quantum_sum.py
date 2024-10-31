
from qiskit import QuantumCircuit, QuantumRegister
import numpy as np


def quantum_sum(a: int, b: int):
    return a + b


def apply_qft(circuit: QuantumCircuit, num_qubits: int):
    """
    Applies the Quantum Fourier Transform (QFT) to a quantum circuit.

    Args:
        circuit: The quantum circuit to apply QFT to.
        num_qubits: The number of qubits in the circuit.
    """

    # check if the number of qubits is valid
    if num_qubits <= 0:
        raise ValueError("Number of qubits must be positive.")

    # create control registers for CU1 gates
    ctrl_registers = [QuantumRegister(i) for i in range(num_qubits - 1, 0, -1)]
    num_registers = len(ctrl_registers)

    # apply Hadamard gates to each qubit
    for i in range(num_qubits):
        circuit.h(i)

    # apply controlled rotations to qubits on the right of the j-th qubit
    for j in range(num_qubits):
        for k in range(j + 1, num_registers):
            angle = 2 * np.pi / (2**(k - j + 1))

            control = ctrl_registers[num_registers - k - 1]
            target = ctrl_registers[num_registers - j - 1]

            circuit.crz(angle, control, target)

    return circuit
