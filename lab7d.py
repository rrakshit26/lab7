#!/usr/bin/env python3
# Student ID: rakshit

class Time:
    """Simple object type for time of the day."""
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for the Time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def valid_time(self):
        """Check if the time object's attributes are valid."""
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def format_time(self):
        """Return the time object as a formatted string."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        """Convert the time object to total seconds since midnight."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def change_time(self, seconds):
        """Modify a time object by adding seconds."""
        total_seconds = self.time_to_sec() + seconds
        updated_time = sec_to_time(total_seconds % 86400)
        self.hour, self.minute, self.second = updated_time.hour, updated_time.minute, updated_time.second

    def sum_times(self, t2):
        """Add two time objects and return a new time object."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)


def sec_to_time(seconds):
    """Convert total seconds since midnight to a Time object."""
    t = Time()
    t.hour, rem = divmod(seconds, 3600)
    t.minute, t.second = divmod(rem, 60)
    return t
