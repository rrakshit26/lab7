#!/usr/bin/env python3
# Student ID: rakshit

from lab7a import *

def change_time(time, seconds):
    """Modify a time object by adding or subtracting seconds."""
    time.second += seconds

    # Handle overflow for seconds
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.second < 0:
        time.second += 60
        time.minute -= 1

    # Handle overflow for minutes
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    # Ensure time stays valid
    time.hour %= 24
