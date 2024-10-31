from matplotlib import colormaps
import matplotlib.pyplot as plt
import random


class PlotAxis():
    def __init__(self, data: list, label: str):
        self.data = data
        self.label = label


def plot_results(x_axis: PlotAxis, y_axis: PlotAxis, file_name: str):
    num_circuits = len(y_axis['data'])

    color_names = list(colormaps)
    random.shuffle(color_names)

    color_names = color_names[:num_circuits]

    colors = [colormaps[name] for name in color_names]

    for i in range(num_circuits):
        plt.figure(file_name + str(i))
        plt.plot(x_axis['data'], y_axis['data'][i],
                 marker="o", color=colors[i](100))

        plt.grid(True)
        plt.xlabel(x_axis['label'])
        plt.ylabel(y_axis['label'])

        plt.savefig('plots/' + file_name + '-' + str(i) + '.png')


def plot_error(results: list[list], probabilities: list[list]):
    error_results = []

    for result in results:
        errors = []
        for value in result:
            errors.append(value['error'])

        error_results.append(errors)

    y_axis = {
        'data': error_results,
        'label': 'Error'
    }

    x_axis = {
        'data': probabilities,
        'label': 'Noise probability'
    }

    return plot_results(x_axis, y_axis, 'plot_error')


def plot_simulation_results(results: list[list], probabilities: list[list]):
    simulation_results = []

    for result in results:
        real = []

        for value in result:
            real.append(value['result'])

        simulation_results.append(real)

    y_axis = {
        'data': simulation_results,
        'label': 'Result'
    }

    x_axis = {
        'data': probabilities,
        'label': 'Noise probability'
    }

    return plot_results(x_axis, y_axis, 'plot_result')
