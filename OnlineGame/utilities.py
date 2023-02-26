def read_pos(data):
    data_ = data.split(",")

    return int(data_[0]), int(data_[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])
