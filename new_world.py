import sys

from Frame import Frame
import matplotlib.pyplot as plt
import gold_master as gold
from mpi4py import MPI
from new_calculation import returnOurPi

# usage:python new_world.py bottom_border_of_pi_digits top_border_of_pi_digits desired_size precision folder_for_pics

comm = MPI.COMM_WORLD
world_size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()


if sys.argv.__len__() == 6:
    desired_size = int(sys.argv[3])
    precision = float(sys.argv[4])
    folder_for_pics = sys.argv[5]

    top_pi_decimal = int(sys.argv[2])
    bottom_pi_decimal = int(sys.argv[1])
    own = True

elif sys.argv.__len__() == 5:
    file_name = sys.argv[1]
    desired_size = int(sys.argv[2])
    precision = float(sys.argv[3])
    folder_for_pics = sys.argv[4]
    own = False
else:
    if rank == 0:
        print("Usage when reads Pi from text:\n\t\
$mpiexec -n [num] python3 new_world.py Pi_file_name  frame_size precision folder_for_pics")
        print("Usage when want to calculate Pi by self:\n\t\
$mpiexec -n [num] python3 new_world.py bottom_border_of_pi_digits top_border_of_pi_digits frame_size precision folder_for_pics")
    sys.exit()


# print("top: %s", top_pi_decimal)
# print("bottom: %s", bottom_pi_decimal)
if rank == 0:

    if own:
        pi_text = returnOurPi(bottom_pi_decimal, top_pi_decimal)
    # print(pi_text)
    else:
        pi_text = open(file_name, "r")
        pi_text = pi_text.read().replace(".", "")

    dx = int(pi_text.__len__() / world_size)
    data = list()
    if dx < desired_size:
        print("Desired frame size cant be bigger than calculating units.")
        exit()
    for x in range(world_size):
        begin = dx * x
        end = dx * (x + 1)
        if x != 0:
            begin -= desired_size - 1
        if x != world_size - 1:  # last one, numbered from 0
            end += desired_size - 1
        data.append(pi_text[begin:end])

else:
    data = None

data = comm.scatter(data, root=0)
result = []

frame = Frame(desired_size)

for i in range(desired_size - 1):  # pushing through empty frame place
    frame.data_push(data[i])

for i in range(desired_size - 1, data.__len__()):
    frame.data_push(data[i])
    res = gold.calc_diff_from_gold(frame)
    result.append(res)
    if res < precision:
        gold.paint_gold(frame, folder_for_pics)

results = comm.gather((result, rank), root=0)

if rank == 0:
    res_map = {}
    for x in results:
        res_map[x[1]] = x[0]

    y = []

    for i in range(world_size):
        for el in res_map[i]:
            y.append(el)

    x = range(y.__len__())
    plt.autoscale(enable=True)
    plt.plot(x, y)
    plt.savefig("mean_deviation_graph.png".format(), dpi=300)
    plt.close()
