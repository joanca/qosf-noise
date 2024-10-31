from qiskit.circuit import QuantumCircuit, Instruction
from qiskit.circuit.library import HGate, CXGate, IGate, RZGate, SXGate, XGate
import numpy as np


def decompose_into_basis(circuit: QuantumCircuit):
    """
    Decomposes input circuit into the set of basis gates: {CX,ID,RZ,SX,X}

    Args:
        circuit: circuit to decompose (must be 1 or 2-qubit gates)

    Returns:
        the decomposed quantum circuit
    """

    decomposed_circuit = QuantumCircuit(circuit.qubits, circuit.clbits)

    for gate, qubits, clbits in circuit.data:
        if is_basis_gate(gate):
            decomposed_circuit.append(gate, qubits, clbits)

        elif isinstance(gate, HGate):
            # Decompose Hadamard gate
            decomposed_circuit.rz(np.pi/2, qubits[0])
            decomposed_circuit.sx(qubits[0])
            decomposed_circuit.rz(np.pi/2, qubits[0])

    return decomposed_circuit


def is_basis_gate(gate: Instruction):
    BASIS_SET = [CXGate, IGate, RZGate, SXGate, XGate]

    return any(isinstance(gate, base) for base in BASIS_SET)
