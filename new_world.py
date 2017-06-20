

import matplotlib.pyplot as plt

from mpi4py import MPI


def paint_gold(frame):
    channels = 1
    size = frame.__len__()


    if size == 16:
        pass

    print ("GOLD FRAME!"+str(frame))


def calc_diff_from_gold(frame):
    opp_gold = 0.61833989
    len = 0
    ones = 0

    for part in frame:
        for x in part:
            len += 1
            if x == "1":
                ones += 1
    result = opp_gold - ones/len
    return result


def data_to_bin(data):
    binary_vals = {
        0: "0000",
        1: "0001",
        2: "0010",
        3: "0011",
        4: "0100",
        5: "0101",
        6: "0110",
        7: "0111",
        8: "1000",
        9: "1001"}
    return binary_vals[int(data)]


def frame_push( frame, data):
    for x in range(1,frame.__len__()):
        frame[x-1] = frame[x]
    frame[-1] = data


file_name = "10000.txt"
comm = MPI.COMM_WORLD
world_size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:

    pi_text = open(file_name, "r")
    pi_text = pi_text.read().replace(".", "")
    dx = int(pi_text.__len__()/world_size)
    data = list()
    for x in range(world_size):
        data.append(pi_text[dx*x: dx*(x+1)])

else:
    data = None

data = comm.scatter(data, root = 0)
result4 = []        # TODO: o roznych dlugosciach
result16 = []

frame4 =[[],[],[],[]]
frame16 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for data_pack in data:
    frame_push(frame4, data_to_bin(data_pack))
    frame_push(frame16, data_to_bin(data_pack))
    res = calc_diff_from_gold(frame4)
    result4.append(res)
    if res < 0.1:  # TODO: mozna zadac prog dokladnosci
        paint_gold(frame4)
    res = calc_diff_from_gold(frame16)
    result16.append(res)
    if res < 0.1:
        paint_gold(frame16)

results_4 = comm.gather((result4, rank), root = 0)
results_16 = comm.gather((result16,rank), root = 0)

if rank == 0:
    res_map_16 = {}
    res_map_4 = {}
    for x in results_4:
        res_map_4[x[1]] = x[0]
    for x in results_16:
        res_map_16[x[1]] = x[0]

    x = range(pi_text.__len__())
    y = []
    for i in range(world_size):
        for el in res_map_4[i]:
            y.append(el)

    plt.autoscale(enable = True)
    plt.plot(x, y)
    plt.savefig("Mean deviation_from_{}.png".format(file_name), dpi = 300)
    plt.close()








