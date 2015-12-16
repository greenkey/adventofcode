import hashlib, re


class MFCSAM():
    compounds = ["children", "cats", "samoyeds", "pomeranians", "akitas", "vizslas", "goldfish", "trees", "cars", "perfumes"]

    def put(self,what):
        if what == "wrapping from the gift":
            obj = {
                "children": 3,
                "cats": 7,
                "samoyeds": 2,
                "pomeranians": 3,
                "akitas": 0,
                "vizslas": 0,
                "goldfish": 5,
                "trees": 3,
                "cars": 2,
                "perfumes": 1
            }
        else:
            obj = dict()
            for c in self.compounds:
                obj[c] = re.search("([0-9])", hashlib.sha512(c + what).hexdigest()).group(1)
        return obj

class AuntList():
    def __init__(self):
        self.al = dict()
        pass

    def getFromFile(self,filename):
        with open(filename, "r") as aunt_list:
            for aunt in aunt_list:
                #Sue 1: children: 1, cars: 8, vizslas: 7
                (name,compounds) = re.search("(Sue [0-9]*):(.*)",aunt).groups()
                self.al[name] = dict()
                for c in compounds.split(","):
                    c = c.split(":")
                    self.al[name][c[0].strip()] = int(c[1].strip())

    def matchCompounds(self,comps,MFCSAM_type='new_retroencabulator'):
        match = list()
        for aunt_name,aunt_comps in self.al.items():
            right_aunt = True
            for comp in comps.keys():
                try:
                    if MFCSAM_type == 'new_retroencabulator':
                        if aunt_comps[comp] != comps[comp]:
                            right_aunt = False
                            break
                    elif MFCSAM_type == 'old_retroencabulator':
                        if comp in ('cats','trees'):
                            if aunt_comps[comp] <= comps[comp]:
                                right_aunt = False
                                break
                        elif comp in ('pomeranians','goldfish'):
                            if aunt_comps[comp] >= comps[comp]:
                                right_aunt = False
                                break
                        elif aunt_comps[comp] != comps[comp]:
                            right_aunt = False
                            break
                except:
                    pass
            if right_aunt:
                match.append(aunt_name)
        return match

if __name__ == "__main__":
    machine = MFCSAM()
    compounds = machine.put("wrapping from the gift")

    aunt_list = AuntList()
    aunt_list.getFromFile("aunts.input")

    print("Which Sue got you the gift: {}".format(aunt_list.matchCompounds(compounds)))

