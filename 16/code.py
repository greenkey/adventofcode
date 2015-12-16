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
