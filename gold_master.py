import os

from PIL import Image


def calc_diff_from_gold(frame):
    opp_gold = 0.61833989
    ones = 0
    #print(frame.__str__().__len__())
    for x in frame.__str__():
            #all += 1
            if x == "1":
                ones += 1
    result = opp_gold - ones/frame.get_length()
    return abs(result)


def paint_gold(frame, folder_name):
    #print(frame)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    size = frame.get_length()**0.5
    size = int(size)  # TODO: co z takimi, ktore nie ładnie się dzielą?
    gold = Image.new("1", (size, size), color="black")
    bits = frame.__str__()
    pxls = gold.load()
    b_len = bits.__len__()
    for x in range(size*size - b_len):                # TODO: czy taki fix jest zgodny z ideologią?
        bits += "0"

    #print(bits)
    for x in range(gold.size[0]):
        for y in range(gold.size[1]):
            # print(x*img.size[0]+y)
            if bits[y * gold.size[0] + x] == "1":
                #print("jest 1 dla {} {} {}".format(x * gold.size[0] + y, x, y))
                pxls[x, y] = 0
            else:
                pxls[x, y] = 1

    # gold = gold.resize((128,128), Image.LINEAR)       # TODO: zrobić resize
    #gold.show()
    gold.save("{}/{}.BMP".format(folder_name,frame.__hash__()), "BMP")
