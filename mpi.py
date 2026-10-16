**Openmp and mpi
1) Sudo apt update
2) Sudo apt install build-essentials
3) Sudo apt install openmpi-bin libopenmpi-dev
4) Gcc ---version
5) Mpicc --version
6) Mpirun --version
7) sudo apt install python3
8) Sudo apt install -y -q mpich
9) Sudo apt install python3-pip python3-venv -y
10) Python3 -m venv mpi-env
11) Source mpi-env/bin/activate
12) Python -m pip install --upgrade pip
13) Python -m pip install mpi4py
14) Python c “import mpi4py; print(mpi4py.__version__)”
15) Mpicc --version
16) Gcc -fopenmp --version
17) Mpi_hello.c
18) Mpicc mpi_hello.c -o mpi_hello
19) Mpirun --oversubscribe -np 4 ./mpi_hello
20) Nano hello.c
21) Gcc -fopenmp hello.c -o hello
22) ./hello
23) Nano reduction.c
24) Private.c
25) Firstprivate.c
26) Lastprivate.c
27) Critical.c