#!/usr/bin/env python3
# Student ID: rakshit

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_sec(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def __add__(self, t2):
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

def sec_to_time(seconds):
    t = Time()
    t.hour, rem = divmod(seconds, 3600)
    t.minute, t.second = divmod(rem, 60)
    return t
