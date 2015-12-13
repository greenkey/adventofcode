import re

inputMask = "([\w]+) would ([\w]+) ([0-9]+) happiness units by sitting next to ([\w]+)."

class Attendees():
    def __init__(self):
        self.people = dict()

    def addPotentialHappiness(self,who,pe,otherPerson):
        if who not in self.people:
            self.people[who] = Person(who)
        self.people[who].addPE(otherPerson,pe)

    def findTableConfigurations(self):
        keys = list(self.people.keys())
        return map(lambda x: keys[:1] + x, permutations(keys[1:]) )

    def totalPE(self,conf):
        tpe = 0
        for i in range(len(conf)):
            name = conf[i]
            name_r = conf[(i+1) % len(conf)]
            name_l = conf[(i-1) % len(conf)]
            tpe += self.people[name].peWith(name_l)
            tpe += self.people[name].peWith(name_r)
        return tpe

    def findGreatestHappiness(self):
        greatestHappiness = 0
        for c in self.findTableConfigurations():
            actualPE = self.totalPE(c)
            if actualPE > greatestHappiness:
                greatestHappiness = actualPE
        return greatestHappiness

    def addNeutralAttendant(self,name):
        currentAttendees = list(self.people.keys())
        for ca in currentAttendees:
            self.addPotentialHappiness(name,0,ca)
            self.addPotentialHappiness(ca,0,name)

class Person():
    def __init__(self,name):
        self.name = name
        self.pe = dict()

    def addPE(self,other,pe):
        self.pe[other] = pe

    def peWith(self,other):
        return self.pe[other]

def permutations(listObj):
    if len(listObj) <= 1:
        return [listObj]
    else:
        perm = list()
        for el in listObj:
            nl = listObj[:]
            nl.remove(el)
            for p in permutations( nl ):
                perm.append( [el] + p )
        return perm


if __name__ == "__main__":
    # get all potential happiness
    attendees = Attendees()
    with open("input", "r") as pe_list:
        for pe_desc in pe_list:
            m = re.search(inputMask, pe_desc)
            (who, peSign, pe, otherPerson) = m.groups()
            pe = int(pe)
            if peSign == "lose":
                pe = -pe
            attendees.addPotentialHappiness(who=who, pe=pe, otherPerson=otherPerson)

    print("total change in happiness: {}".format(attendees.findGreatestHappiness()))

    attendees.addNeutralAttendant("me")
    print("total change in happiness with me: {}".format(attendees.findGreatestHappiness()))
