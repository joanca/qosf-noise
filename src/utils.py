from qiskit import QuantumCircuit
from numpy.random import choice


def apply_x_gate(circuit: QuantumCircuit, qubit_index: int):
    """Applies an X gate to the specified qubit in the circuit."""

    circuit.x(qubit_index)


def apply_y_gate(circuit: QuantumCircuit, qubit_index: int):
    """Applies an Y gate to the specified qubit in the circuit."""

    circuit.y(qubit_index)


def apply_z_gate(circuit: QuantumCircuit, qubit_index: int):
    """Applies an Y gate to the specified qubit in the circuit."""

    circuit.z(qubit_index)


def apply_i_gate(circuit: QuantumCircuit, qubit_index: int):
    """Applies an I gate to the specified qubit in the circuit.
       Knowing that X^2 = I, we can can say that applying twice the X gate, 
       we obtain the expected result, since that means that we revert the 
       previous X gate.
    """

    circuit.x(qubit_index)
    circuit.x(qubit_index)


def get_random_gate():
    return choice([apply_x_gate, apply_y_gate, apply_z_gate, apply_i_gate])
