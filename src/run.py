from qiskit import QuantumCircuit
from qiskit.result import Counts
from qiskit_aer import AerSimulator
import numpy as np
from typing import List

from noise import add_pauli_noise
from quantum_sum import decomposed_quantum_sum
from plot import plot_error

SIMULATOR = AerSimulator(method='statevector')

NUM_CIRCUITS_SIMULATE = 3
ONE = 1
NUMBERS_TO_SUM = [0, 2, 4, 8, 16]


def run_simulation(circuits: List[QuantumCircuit]) -> List[Counts]:
    job = SIMULATOR.run(circuits)

    result = job.result()
    counts = result.get_counts()

    return counts


def prepare_simulation_circuits(circuit: QuantumCircuit, a: float, b: float) -> List[QuantumCircuit]:
    noisy_circuit_1 = add_pauli_noise(circuit, a, b)
    noisy_circuit_2 = add_pauli_noise(circuit, b, a)
    noisy_circuit_3 = add_pauli_noise(circuit, a, a)

    # measuring all circuits before running simulation
    noisy_circuit_1.measure_all()
    noisy_circuit_2.measure_all()
    noisy_circuit_3.measure_all()

    return [noisy_circuit_1, noisy_circuit_2, noisy_circuit_3]


def get_simulation_results(
    circuit: QuantumCircuit,
    probabilities: List[float],
    real_value: int
) -> List[List]:
    results = [[] for x in range(NUM_CIRCUITS_SIMULATE)]

    for probability in probabilities:
        circuits_to_simulate = prepare_simulation_circuits(
            circuit, probability, 0)

        simulation_counts = run_simulation(circuits_to_simulate)

        for i in range(NUM_CIRCUITS_SIMULATE):
            most_frequest_result_binary = simulation_counts[i].most_frequent()
            simulation_result = int(most_frequest_result_binary, base=2)

            simulation_result = {
                'error': int(np.abs(simulation_result - real_value)),
                'result': simulation_result,
                'real': real_value
            }

            results[i].append(simulation_result)

    return results


if __name__ == "__main__":
    for NUMBER in range(len(NUMBERS_TO_SUM)):
        real_value = NUMBER + ONE

        probabilities_to_add_noise = np.arange(0, 1, 0.1)
        decomposed_sum_circuit = decomposed_quantum_sum(NUMBER, ONE)

        print('probabilities: ', probabilities_to_add_noise)

        results = get_simulation_results(
            decomposed_sum_circuit,
            probabilities_to_add_noise,
            real_value
        )

        plot_error(results, probabilities_to_add_noise)
