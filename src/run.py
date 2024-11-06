from qiskit import QuantumCircuit
from qiskit.result import Counts
from qiskit_aer import AerSimulator
import numpy as np
from numpy.random import choice
from typing import List

from noise import add_pauli_noise
from quantum_sum import decomposed_quantum_sum
from plot import plot_error, plot_simulation_results

SIMULATOR = AerSimulator(method='statevector')

NUM_CIRCUITS_SIMULATE = 5
FIVE = 5
NUMBERS_TO_SUM = [0, 1, 5, 7, 10, 15]


def run_simulation(circuits: List[QuantumCircuit]) -> List[Counts]:
    job = SIMULATOR.run(circuits, shots=1024)

    result = job.result()
    counts = result.get_counts()

    return counts


def prepare_simulation_circuits(circuit: QuantumCircuit, a: float, b: float) -> List[QuantumCircuit]:
    noisy_circuits = []

    for i in range(NUM_CIRCUITS_SIMULATE):
        prob_a = choice([a, b])
        prob_b = choice([a, b])

        noisy_circuit = add_pauli_noise(circuit, prob_a, prob_b)
        noisy_circuit.measure_all()

        noisy_circuits.append(noisy_circuit)

    return noisy_circuits


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
            most_frequest_result_binary = simulation_counts[i].most_frequent().replace(" ", "")
            simulation_result = int(most_frequest_result_binary, base=2)

            simulation_result = {
                'error': int(np.abs(simulation_result - real_value)),
                'result': simulation_result,
                'real': real_value
            }

            results[i].append(simulation_result)

    return results


def main():
    for NUMBER in range(len(NUMBERS_TO_SUM)):
        real_value = NUMBER + FIVE

        probabilities_to_add_noise = np.arange(0, 1, 0.1)
        decomposed_sum_circuit = decomposed_quantum_sum(NUMBER, FIVE)

        results = get_simulation_results(
            decomposed_sum_circuit,
            probabilities_to_add_noise,
            real_value
        )

        plot_simulation_results(results, probabilities_to_add_noise)
        plot_error(results, probabilities_to_add_noise)


if __name__ == "__main__":
    main()
