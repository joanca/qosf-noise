# QOSF Cohort 10 - Task 2 Noise
This repository contains the code to solve the task 2 of the QOSF Cohort 10 application. 

To solve the problem I'm using the framework Qiskit, and the repository is divided in the following way:

- `src/`: contains the source code of the solution.

This is a high level description of each module inside `src/`:

```
src/
  decompose_basis.py // decompose a circuit into basis gates
  fourier_transform.py // implementation of the QFT and inverse QFT
  quantum_sum.py // quantum sum circuit
  noise.py // noise generator using Pauli operators
  plot.py // utils for plotting result
  run.py // applies noise to quantum sum and plots results
```

## Build Docker image
In order to be able to run this project easily, everything can be executed inside a Docker container, using an image 
that will be built the first time you run it or by using the following command:

> If you prefer to run the code in your own environment, you can (#virtual-env)[skip to the virtual environment] section below.

```
make build
```

This will build an image that have a Jupyter lab instance ready to run and all the Python dependencies that this project
requires. You can check the dependencies on the (requirements.txt)[requirements.txt] file.

## Run code and get plots
Using the following command you will execute the `run.py` script:

```
make run
```

You will see some results on your terminal and also the plots of the error and simulated result of the sum.

## Jupyter notebook
You can start the Jupyter lab server by running the following command:

```
make notebooks
```

After this, go to the following url to open the notebook: http://localhost:8889/lab/tree/src/noise.ipynb?token=1234
