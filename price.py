import os
import sys
from json import load, dump
from datetime import timedelta

path_prefix = "times/"

def get_time(user):
    content = {}
    print(f"{path_prefix}{user}.json")
    with open(f"{path_prefix}{user}.json", "r") as json_file:
        content = load(json_file)

    total = timedelta()
    for raw_data in content.values():
        print(raw_data)
        h, m, _ = list(map(int, raw_data["elapsed"].split(':')))
        total += timedelta(minutes=m, hours=h)
    t_min = total.seconds // 60
    t_hou = t_min // 60

    return t_hou, t_min % 60


def main():
    # os.chdir("/times")

    per_hour = float(sys.argv[1]) if len(sys.argv) > 1 else 2
    accums = {}
    users = []

    try:
        users.append(sys.argv[2])

        if not f"{path_prefix}{users[0]}.json" in os.listdir():
            raise FileNotFoundError
    except IndexError:
        users = [user_file.split('.')[0] for user_file in os.listdir("./times")]

    for user in users:
        t = get_time(user)
        accums[user] = (f'{t[0]}:{t[1]}', f"${(t[0] * per_hour + t[1] * per_hour / 60)}")

    for us in accums:
        print(f"{us} ---> {accums[us]}")


if __name__ == "__main__":
    main()