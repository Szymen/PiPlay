from builtins import Exception


def digit_to_bin(data):
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


class Frame:

    def __init__(self, size):
            self.size = size
            self.data = [""]*size

    def __str__(self):
        return "".join(self.data)

    def data_push(self, data_to_add):
        for x in range(1, self.data.__len__()):
            self.data[x - 1] = self.data[x]
        self.data[-1] = digit_to_bin(data_to_add)

    def get_length(self):
        return self.data.__len__()*4