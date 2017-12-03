import tty
import termios
import sys
import json
import os
import RPi.GPIO as GPIO


def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def create_bfd():
    # from pprint import pprint
    btn_filename_dict = json.load(open('btn.conf'))
    # pprint(key_filename_dict)
    return btn_filename_dict


def create_ppd():
    btn_pin_dict = json.load(open('pin_btn.conf'))
    return btn_pin_dict


def callback_play_sound(pin):
    if pin == 6:
        os.system("aplay -q " + "samples/handclap.wav" + '&')
        # os.system("sudo python3 gpioOUT.py " + str(btn_pin_dict[key]) + " " + str(0.1) + " &")
    if pin == 13:
        os.system("aplay -q " + "samples/cl_hihat.wav" + '&')
        # os.system("sudo python3 gpioOUT.py " + str(btn_pin_dict[key]) + " " + str(0.1) + " &")
    if pin == 19:
        os.system("aplay -q " + "samples/hightom.wav" + '&')
        # os.system("sudo python3 gpioOUT.py " + str(btn_pin_dict[key]) + " " + str(0.1) + " &")
    if pin == 26:
        os.system("aplay -q " + "samples/cowbell.wav" + '&')
        # os.system("sudo python3 gpioOUT.py " + str(btn_pin_dict[key]) + " " + str(0.1) + " &")


def main():
    GPIO.cleanup()
    setup_gpio()
    GPIO.setwarnings(False)
    os.system('stty -echo')
    GPIO.add_event_detect(6, GPIO.RISING, callback=callback_play_sound, bouncetime=100)
    GPIO.add_event_detect(13, GPIO.RISING, callback=callback_play_sound, bouncetime=100)
    GPIO.add_event_detect(19, GPIO.RISING, callback=callback_play_sound, bouncetime=100)
    GPIO.add_event_detect(26, GPIO.RISING, callback=callback_play_sound, bouncetime=100)
    try:
        while  True:
            pass
    except KeyboardInterrupt:  # trap a CTRL+C keyboard interrupt
        GPIO.cleanup()


main()
