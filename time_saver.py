import sys
import os
from json import dump, load
from datetime import datetime, time, timedelta

path_prefix = "times/"

def format_timedelta(timed: timedelta):
    _minutes = timed.seconds // 60
    _hours = _minutes // 60
    return f"{_hours}:{_minutes % 60}:{timed.seconds % 60}"

def save_time(user, time_init, elapsed):
    cur_info = {}
    if isinstance(elapsed, timedelta):
        elapsed = format_timedelta(elapsed)
    if isinstance(elapsed, int):
        elapsed = f"{elapsed // 60}:{elapsed % 60}:0"

    cur_info["datetime"] = time_init.strftime("%d %b %Y, %I:%M:%S")
    cur_info["elapsed"] = elapsed

    content = {}
    if os.path.isfile(f"{path_prefix}{user}.json"):
        # File exists
        with open(f"{path_prefix}{user}.json", 'r') as json_file:
            content = load(json_file)
        content[datetime.today().__hash__()] = cur_info

        with open(f"{path_prefix}{user}.json", 'w') as json_file:
            dump(content, json_file, indent=4)
    else:
        # Create file
        content[datetime.today().__hash__()] = cur_info
        with open(f"{path_prefix}{user}.json", 'a+') as json_file:
            dump(content, json_file, indent=4)

class Chronometer:
    def __init__(self, user):
        self.user = user
        self.cur_start = timedelta(seconds=0)
        self.cur_stop = timedelta(seconds=0)
        self.is_running = False

    def start(self):
        if self.is_running:
            return
        self.is_running = True
        self.cur_start = datetime.today()
        self.cur_stop = None

    def stop(self):
        if not self.is_running:
            return
        self.is_running = False
        self.cur_stop = datetime.today()

    def resume(self):
        self.start()

    @property
    def elapsed(self):
        if self.is_running:
            return datetime.today() - self.cur_start
        return self.cur_stop - self.cur_start


def prepare_env():
    if not os.path.exists("times"):
        os.mkdir("times")
    os.chdir(".\\times")

def show_state(chrono : Chronometer):
    print(f"Time: {chrono.elapsed}")

def main(user):
    answer = None
    chrono = Chronometer(user)

    chrono.start()
    print("\nCHRONO is running...")
    print("\n CHRONO ->\nr : to resume.\nc : to stop.\np : to pause.\n")

    while answer != 'c':
        answer = input()
        if answer is 'h':
            print("\n CHRONO ->\nr : to resume.\nc : to stop.\np : to pause.\n")
        elif answer is 'p':
            chrono.stop()
        elif answer is 'r':
            chrono.resume()
        show_state(chrono)

    print(f"Time: {chrono.elapsed}")
    chrono.stop()


if __name__ == "__main__":
    # prepare_env()

    user = "None"
    try:
        user = sys.argv[1]
    except:
        pass

    main(user)
