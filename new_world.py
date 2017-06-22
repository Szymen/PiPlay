import os

import sys
from math import pi

from Frame import Frame
import matplotlib.pyplot as plt
import gold_master as gold
from mpi4py import MPI
from pi_calculation import calc_pi
from new_calculation import getPiLeibniz

# usage:python new_world.py required_no_of_decimals_of_pi desired_size precision folder_for_pics

desired_size = int(sys.argv[2]) 
precision = float(sys.argv[3])
# file_name = sys.argv[1]
folder_for_pics = sys.argv[4]
chosen_pi_decimals = int(sys.argv[1])
print(chosen_pi_decimals)

comm = MPI.COMM_WORLD
world_size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    # pi_text = open(file_name, "r")
    pi_array = getPiLeibniz(chosen_pi_decimals)
    print(pi_array)
    pi_text = int(''.join(map(str, pi_array)))
    print(pi_text)
    dx = int(pi_text.__len__()/world_size) #TODO: TUTAJ SIĘ KRZACZY, BO INNE FORMATY
    data = list()
    if dx < desired_size:
        print("Desired frame size cant be bigger than calculating units.")
        exit()
    for x in range(world_size):
        begin = dx * x
        end = dx * (x + 1)
        if x != 0:
            begin -= desired_size - 1
        if x != world_size-1: # last one, numbered from 0
            end += desired_size - 1
        data.append(pi_text[begin:end])

else:
    data = None

data = comm.scatter(data, root = 0)
result = []


frame = Frame(desired_size)

for i in range(desired_size-1):     # pushing through empty frame place
    frame.data_push(data[i])

for i in range(desired_size-1, data.__len__()):
    frame.data_push(data[i])
    res = gold.calc_diff_from_gold(frame)
    result.append(res)
    if res < precision:
        gold.paint_gold(frame, folder_for_pics)


results = comm.gather((result, rank), root = 0)


if rank == 0:
    res_map = {}
    for x in results:
        res_map[x[1]] = x[0]

    #x = range(pi_text.__len__() + desired_size*world_size - world_size*2 + 2) # TODO: nie wiem ile generuje danych i czy nie jest za duzo
    y = []

    for i in range(world_size):
        for el in res_map[i]:
            y.append(el)

    x = range(y.__len__())
    plt.autoscale(enable=True)
    plt.plot(x, y)
    plt.savefig("mean_deviation_graph.png".format(), dpi = 300)
    plt.close()








