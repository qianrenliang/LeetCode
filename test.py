#coding:utf-8
import math


def get_hz(ticks):
    # not durations
    hz = 1.0 / (ticks * 6 *(10**-9))
    khz = hz / 1000.0
    print "Hz is %.4f Hz\nkHz is %.3f kHz" % (hz, khz)
    return 0


def get_distance(fz, t):
    tick = 0
    if fz == 1:
        tick = 83
    elif fz == 2:
        tick = 42
    elif fz == 3:
        tick = 28
    elif fz == 0.5:
    	tick = 166
    ticks = tick*t*2
    distance = 1500*100*6*ticks*(10**-9)
    print "Distance is %.4f cm" % distance
    return 0


if __name__ == "__main__":
    # ticks = int(raw_input("print Your ticks:\n"))
    get_hz(8332511)
    # get_distance(1,10)




