import sys, re

v_NONE = 0
v_INFO = 1
v_DEBUG = 2
log_print_condition = None
def log(log_level,s):
    if log_level <= verbosity:
        if log_print_condition:
            if log_print_condition(s):
                print(s)
        else:
            print(s)


class BotSystem():

    def __init__(self):
        self.bots = dict()

    def get_bot(self,bot_name):
        if bot_name not in self.bots:
            self.bots[bot_name] = Bot(bot_name)
        return self.bots[bot_name]


    def execute(self,s):
        log(v_INFO, "Executing: {}".format(s))
        if "goes" in s:
            (value, bot_name) = re.search("value ([0-9]+) goes to ([a-z]+ [0-9]+)", s).groups()
            log(v_DEBUG, "value {} goes to {}".format(value,bot_name))
            self.get_bot(bot_name).take_val(value)
        elif "gives" in s:
            (bot_name,gives_low,gives_high) = re.search("([a-z]+ [0-9]+) gives low to ([a-z]+ [0-9]+) and high to ([a-z]+ [0-9]+)", s).groups()
            log(v_DEBUG, "{} gives low to {} and high to {}".format(bot_name,gives_low,gives_high))
            self.get_bot(bot_name).set_rules(low=gives_low, high=gives_high)

        for new_action in self.get_bot(bot_name).next_actions():
            self.execute(new_action)

    def print_me(self):
        ret = ""
        for bot in sorted(self.bots.values()):
            ret += "\n{}: {} - h->{} - l->{}".format(bot.name, bot.values, bot.high_to, bot.low_to)
        return ret

class Bot():

    def __init__(self,name):
        self.name = name
        self.values = list()
        self.low_to = ""
        self.high_to = ""

    def __lt__(self,other):
        return int(self.name.split()[1]) < int(other.name.split()[1])

    def take_val(self,value):
        log(v_DEBUG, "{}: taking value {}".format(self.name,value))
        self.values.append(int(value))
        return self

    def set_rules(self,low,high):
        log(v_DEBUG, "{}: I'll give low to {} and high to {}".format(self.name,low,high))
        self.low_to = low
        self.high_to = high
        return self

    def next_actions(self):
        log(v_DEBUG,"{}: I have {} values, I'll give low to {} and high to {}".format(self.name,len(self.values),self.low_to,self.high_to))
        if len(self.values) == 2:
            log(v_INFO, "{}: evaluating values: {}".format(self.name, self.values))
            if self.low_to != "":
                yield "value {} goes to {}".format(min(self.values),self.low_to)
            if self.high_to != "":
                yield "value {} goes to {}".format(max(self.values),self.high_to)
        else:
            log(v_DEBUG, "{}: I don't have enough values".format(self.name))

bs = BotSystem()
verbosity = v_INFO

def log_print_condition(s):
    import re
    return re.search("evaluating values: \[(61|17), (61|17)\]", s)

with open(sys.argv[1],'r') as f:
    for l in f:
        bs.execute(l.strip())
