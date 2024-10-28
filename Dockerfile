FROM quay.io/jupyter/base-notebook

RUN pip install qiskit pyscf matplotlib pylatexenc lithops lithopscloud

RUN echo "echo \"\n🔆 Welcome to the Qiskit Docker\"\n" >>~/.bashrc 
RUN echo "echo \"\n🚀 This is the minimum elements to run Qiskit \n\n \"" >>~/.bashrc 

CMD jupyter lab --no-browser --ip=0.0.0.0
