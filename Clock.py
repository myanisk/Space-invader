clok_time = 0

def clock(timer):
    global clock_time
    clock_time +=1


t = Timer(4, freq=10)
t.callback(clock)