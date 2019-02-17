import os
import sys
from json import load, dump
from datetime import timedelta,datetime

def delete_olds():
    now = datetime.today()
    for t_file in (direct for direct in os.listdir(os.getcwd()) if direct.endswith(".json")):
        content = {}

        with open(t_file,'r') as json_file:
            content = load(json_file)

        with open(t_file, 'w') as json_file:
            nw_content = {}
            for i in content:
                print(datetime.strptime(content[i]['datetime'], "%d %b %Y, %I:%M:%S"),now - timedelta(days=30))
                if datetime.strptime(content[i]['datetime'], "%d %b %Y, %I:%M:%S") >= now - timedelta(days=30):
                    nw_content[i] = content[i]
            dump(nw_content, json_file, indent=4)


def get_time(user):
    content = {}
    with open(f"{user}.json", "r") as json_file:
        content = load(json_file)

    total = timedelta()
    for raw_data in content.values():
        print(raw_data)
        h, m = list(map(int, raw_data["elapsed"].split(':')))
        total += timedelta(minutes=m, hours=h)
    t_min = total.seconds // 60
    t_hou = t_min // 60

    return t_hou, t_min % 60


def main():
    os.chdir("./times")
    delete_olds()

    per_hour = float(sys.argv[1]) if len(sys.argv) > 1 else 2
    accums = {}
    users = []

    try:
        users.append(sys.argv[2])

        if not f"{users[0]}.json" in os.listdir():
            raise FileNotFoundError
    except IndexError:
        users = [user_file.split('.')[0] for user_file in os.listdir()]

    for user in users:
        t = get_time(user)
        accums[user] = (t, t[0] * per_hour + t[1] * per_hour / 60)

    for us in accums:
        print(us,':', accums[us][0][0], accums[us][0][1],"--> $"+str(accums[us][1]))


if __name__ == "__main__":
    main()