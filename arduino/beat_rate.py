
def beat_rate(data):
    c = 0
    beats = data.split(',')
    for d in beats:
        if d == '1022':
            c = c +1
    return c/2


data = '1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1021,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1022,1022,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1021,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1022,1022,1023,1023,1023,1023,1023,1023,1023,1023,1021,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1021,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1022,1023,1022,1022,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1022,1023,1021,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1021,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1022,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1022,1022,1023,1023,1023,1023,1023,1022,1022,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1021,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1022,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1022,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1021,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1021,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1021,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1021,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1023,1022,1023,1022,1022,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1022,1022,1023,1023,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1022,1023,1022,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1023,1023,1023,1022,1022,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1021,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1021,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1022,1023,1023,1023,1023,1023,1022,1023,1022,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1022,1023,1023,1023,1023,1022,1023,1022,1023,1022,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1021,1023,1023,1023,1023,1023,1023,1022,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1022,1023,1023,1023,1023,1022,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023'

print beat_rate(data)