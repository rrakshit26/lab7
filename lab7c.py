#!/usr/bin/env python3
# Student ID: rakshit

from lab7b import *

def time_to_sec(time):
    """Convert a time object to the total seconds since midnight."""
    return time.hour * 3600 + time.minute * 60 + time.second

def sec_to_time(seconds):
    """Convert total seconds since midnight into a Time object."""
    t = Time()
    t.hour, rem = divmod(seconds, 3600)
    t.minute, t.second = divmod(rem, 60)
    return t

def sum_times(t1, t2):
    """Add two time objects using seconds."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    """Modify a time object by adding seconds."""
    total_seconds = time_to_sec(time) + seconds
    total_seconds %= 86400  # Keep within one day
    updated_time = sec_to_time(total_seconds)
    time.hour, time.minute, time.second = updated_time.hour, updated_time.minute, updated_time.second

