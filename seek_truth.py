# TODO import psyco speeds up - rumors, not checked
from mpi4py import MPI

def bailey_borwein_Plouffe(n):
    nth_digit = ( 1/pow(16, n) ) * \
        (

            (4 / (8*n + 1) ) -
            (2 / (8*n + 4) ) -
            (1 / (8*n + 5) ) -
            (1 / (8*n + 6) )
        )

    return nth_digit


def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(1000):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


digits = make_pi()
pi_list = []
my_array = []

for i in make_pi():
    my_array.append(str(i))

my_array = my_array[:1] + ['.'] + my_array[1:]
big_string = "".join(my_array)
print ("here is a big string:\n {}".format(big_string))

for i in range(10):
    print ("{0} : {1}".format(i,bailey_borwein_Plouffe(i)))

#size = MPI.COMM_WORLD.Get_size()
#rank =  MPI.COMM_WORLD.Get_rank()
#name = MPI.Get_processor_name()

#print("Rank_{}: Hello World!".format(rank))

#if rank == 0:

