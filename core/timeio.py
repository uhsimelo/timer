from datetime import datetime
from os.path import isfile 
from json import dump, load

from config import PATH_FILES

from .errors import BadFormatError
from .delta_time import DeltaTime
from .utils import createpath_ifnotexist

class TimeSaverIO:
    def __init__(self, name, per_hour = 2):
        self.name = name
        self.change = per_hour
        self.total_time = None
        self.cur_time = DeltaTime(0 , 0, 0)
        self.__load_time()
        self.set_initial_time()

    def __load_time(self):
        content = None
        total = DeltaTime()
        if isfile(f'{PATH_FILES}{self.name}.json'):
            with open(f'{PATH_FILES}{self.name}.json', 'r') as json_file:
                content = load(json_file)
            if isinstance(content, dict):
                content = list(content.values())
            for raw_data in content:
                h, m, s = list(map(int, raw_data['elapsed'].split(':')))
                total.h += h
                total.m += m
                total.s += s

        self.total_time = total

    def set_initial_time(self, _datetime=None):
        self.__initial_time = _datetime if _datetime else datetime.now()

    def save_time(self, time_elapsed: DeltaTime):
        assert isinstance(time_elapsed, DeltaTime)
        
        createpath_ifnotexist(PATH_FILES)
       
        unsaved_info = {
            'datetime': self.__initial_time.strftime('%d %b %Y, %I:%M:%S'),
            'elapsed': str(time_elapsed),
        }

        content = []
        if isfile(f'{PATH_FILES}{self.name}.json'):
            try:
                with open(f'{PATH_FILES}{self.name}.json', 'r') as json_file:
                    content = load(json_file)
                if isinstance(content, dict):
                    content = list(content.values())
                    print(content)
                assert isinstance(content, list)
            except Exception:
                raise BadFormatError

        content.append(unsaved_info)
        with open(f'{PATH_FILES}{self.name}.json', 'w') as json_file:
            dump(content, json_file, indent=4)
        
        self.set_initial_time()
        self.total_time += time_elapsed
    
    def get_money_status(self, delta_time = None):
        total_money = self.total_time.h * self.change
        total_money += self.total_time.m / 60 * self.change
        total_money += self.total_time.s / 3600 * self.change

        if delta_time:
            money = delta_time.h * self.change
            money += delta_time.m / 60 * self.change
            money += delta_time.s / 3600 * self.change
            return total_money, money
        return total_money

