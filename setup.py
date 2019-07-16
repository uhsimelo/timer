from os import system, chdir
from sys import platform


if __name__ == '__main__':
    system("rm -r build/")
    system("rm -r dist/")
    system("rm -r WorkTime*")

    command = ''    
    if platform.startswith('win'):
        command = 'pyinstaller main.py --name WorkTime --noconsole'
    else:
        command = 'pyinstaller main.py -i ./../statics/clock_select.png --name WorkTime --noupx'
    system(command)
