import sys
import os
from matplotlib import pyplot as plt
from datetime import datetime

def range_time(time_init, time_end, delta, steps=-1):
    temp_time = time_init()
    while temp_time < time_end:
        temp_time += delta
        steps -= 1



def plot_hours_day(users, range):
    pass
def plot_state(hours_a_day : dict):
    plt.plot(hours_a_day.keys(), hours_a_day.values())
    plt.show()

def store_by_day(usr):
    pass



