import sys
import os
from matplotlib import pyplot as plt
from datetime import datetime

def plot_state(hours_a_day : dict):
    plt.plot(hours_a_day.keys(), hours_a_day.values())
    plt.show()

def store_by_day(usr):
    pass


