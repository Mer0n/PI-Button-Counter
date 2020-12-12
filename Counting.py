#! /usr/bin/python

import RPi.GPIO as GPIO
import time

BUTTON1 = 17
BUTTON2 = 25
DELAY = 100
TIMEOUT = 10
YELLOW = 27
GREEN = 22
RED = 18
num = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

def button1_pressed(channel):
    global num
    num = num + 1
    if_odd(num)
    if_even(num)
    if_power_of_two(num)
    print(num)

def button2_pressed(channel):
    global num
    num = 0
    if_even(num) 
    # GPIO.output(GREEN, 0)
    if_odd(num) # Use here?
    if_power_of_two(num) 
    print(num)


def if_odd(num):
    global RED
    if num % 2 == 1:  # Odd
        GPIO.output(RED, 1) # 1 means on
    elif num % 2 == 0: # Even
        GPIO.output(RED, 0) # 0 means off


def if_even(num):
    global GREEN
    if num % 2 == 1:  # Odd
        GPIO.output(GREEN, 0)
    elif num % 2 == 0: # Even
        GPIO.output(GREEN, 1)


def if_power_of_two(num):
    global YELLOW
    if (num & (num - 1) == 0):
        GPIO.output(YELLOW, 1)
    elif (num & (num - 1) != 0):
        GPIO.output(YELLOW, 0)

GPIO.setup(BUTTON1, GPIO.IN)
GPIO.add_event_detect(BUTTON1, GPIO.RISING, callback = button1_pressed, bouncetime = DELAY)
GPIO.setup(BUTTON2, GPIO.IN)
GPIO.add_event_detect(BUTTON2, GPIO.RISING, callback = button2_pressed, bouncetime = DELAY)
time.sleep(TIMEOUT)
GPIO.cleanup()