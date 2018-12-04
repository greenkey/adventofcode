from datetime import datetime, timedelta
from collections import defaultdict
import re

class Guard:
    def __init__(self, name):
        self.name = name
        self.sleeping = False
        self.total_minute_sleeping = 0
        self.minutes_stats = defaultdict(int)

    def handle_event(self, date, event_desc):
        if event_desc == 'falls asleep':
            self.falls_asleep(date)
        if event_desc == 'wakes up':
            self.wakes_up(date)

    def falls_asleep(self, date):
        self.sleeping = True
        self.sleep_start = date

    def wakes_up(self, date):
        time_asleep = date - self.sleep_start
        self.total_minute_sleeping += time_asleep.seconds / 60

        temp = self.sleep_start
        while temp < date:
            self.minutes_stats[temp.time()] += 1
            temp += timedelta(minutes=1)

        del self.sleep_start
        self.sleeping = False

    def get_most_sleepy_time(self):
        sleepy_minute = None
        times = 0
        for time, count in self.minutes_stats.items():
            if count > times:
                sleepy_minute = time
                times = count
        return sleepy_minute

class GuardList(list):
    def get_most_sleeper(self):
        slacker = self[0]
        for guard in self[1:]:
            if guard.total_minute_sleeping > slacker.total_minute_sleeping:
                slacker = guard
        return slacker

    def get_guard(self, name):
        for guard in self:
            if guard.name == name:
                return guard
        return Guard(name)

if __name__ == '__main__':
    # [1518-11-01 00:00] Guard #10 begins shift
    # [1518-11-01 00:05] falls asleep
    # [1518-11-01 00:25] wakes up

    mask = re.compile(r'^\[([0-9-]{10} [0-9:]{5})\] (.*)$')
    events = {}
    with open('input') as f:
        for line in f.readlines():
            date, desc = mask.findall(line)[0]
            events[datetime.fromisoformat(date)] = desc
            
    mask = re.compile(r'^Guard #([0-9]+) begins shift$')
    guards = GuardList()
    current_guard = None

    for date in sorted(events.keys()):
        desc = events[date]
        
        begin_shift = mask.findall(desc)
        if begin_shift:
            if current_guard:
                guards.append(current_guard)
            current_guard = guards.get_guard(int(begin_shift[0]))
        else:
            current_guard.handle_event(date, desc)

    slacker = guards.get_most_sleeper()
    time = slacker.get_most_sleepy_time()

    print(slacker.name * time.minute)
