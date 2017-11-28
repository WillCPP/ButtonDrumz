import tty
import termios
import sys
import json
import os


def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def create_kfd():
    # from pprint import pprint
    key_filename_dict = json.load(open('def.conf'))
    # pprint(key_filename_dict)
    return key_filename_dict


def main():
    os.system('stty -echo')
    key_filename_dict = create_kfd()
    loop = True
    while loop:
        ch = get_char()
        for key in key_filename_dict:
            if ch == key:
                os.system("aplay -q " + key_filename_dict[key] + '&')
                break
        # print('You pressed', ch)
        if ch == '/':
            loop = False
            print('Exiting program...')
            for key in key_filename_dict:
                os.system("aplay -q " + key_filename_dict[key])
            os.system('stty echo')


main()
