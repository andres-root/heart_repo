from collections import OrderedDict

def hearth_beat():
    mem = OrderedDict()
    archive = open('./diego_data-1-s2.txt', 'r')
    new_archive = archive.readlines()
    x = new_archive.split(',')
    for d in x:
        try:
            mem[d] = mem[d] + 1
        except:
            mem[d] = 1
    return mem
