# TODO import psyco speeds up - rumors, not checked
from mpi4py import MPI


size = MPI.COMM_WORLD.Get_size()
rank =  MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

print("Rank_{}: Hello World!".format(rank))

