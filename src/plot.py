from matplotlib import colormaps
import matplotlib.pyplot as plt


class PlotAxis():
    def __init__(self, data: list, label: str):
        self.data = data
        self.label = label


def plot_results(x_axis: PlotAxis, y_axis: PlotAxis, file_name: str):
    colors = [colormaps["Blues"], colormaps["Reds"], colormaps["Purples"]]
    num_circuits = len(y_axis['data'])

    for i in range(num_circuits):
        print("#####")
        print('X: ', x_axis['data'])
        print('Y: ', y_axis['data'][i])
        print("#####")

        plt.figure(i)
        plt.plot(x_axis['data'], y_axis['data'][i],
                 marker="o", color=colors[i](80+20))

        plt.grid(True)
        plt.xlabel(x_axis['label'])
        plt.ylabel(y_axis['label'])

        # plt.legend(["n=1", "n=2", "n=3", "n=4", "n=5"])
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
