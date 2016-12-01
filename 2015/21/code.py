import re
from copy import deepcopy

class Game():

    def __init__(self):
        pass

    def setStoreItems(self,fromFile):
        self.store = list()
        with open(fromFile, "r") as inputFile:
            currentCategory = None
            for line in inputFile:
                try:
                    (what,cost,damage,armor) = re.match("^(.*) ([^ ]*) ([^ ]*) ([^ ]*)$",line.strip()).groups()
                    if what[-1] == ":":
                        currentCategory = what[:-1]
                    else:
                        self.store.append({
                            'category': currentCategory,
                            'name': what,
                            'cost': int(cost),
                            'damage': int(damage),
                            'armor': int(armor)
                        })
                except:
                    pass

    def createCharacter(self,name,fromFile=None,hitPoints=0,damage=0,armor=0):
        c = {
            'name':name,
            'Hit Points':hitPoints,
            'Damage':damage,
            'Armor':armor
        }
        if fromFile is not None:
            with open(fromFile, "r") as inputFile:
                for line in inputFile:
                    (k,v) = line.strip().split(": ")
                    c[k] = int(v)
        return c

    def fight(self,c1,c2):
        while True:
            #first turn c1 --> c2
            self.attack(c1,c2)
            if c2['Hit Points'] <= 0:
                return c1
            #second turn c2 --> c1
            self.attack(c2,c1)
            if c1['Hit Points'] <= 0:
                return c2
    def attack(self,c1,c2):
        damage = c1['Damage'] - c2['Armor']
        if damage < 1:
            damage = 1
        c2['Hit Points'] -= damage
        #print("{} hit {} by {}".format(c1['name'],c2['name'],damage))
        #print("{} hit points: {}".format(c2['name'],c2['Hit Points']))

class MyGame(Game):
    def equipmentCombinations(self,sortedBy=None):
        ec = list()
        weapons = list(filter(lambda w: w['category']=='Weapons', self.store))
        armors = list(filter(lambda a: a['category']=='Armor', self.store))
        armors.append({
            'category': 'Armor',
            'name': 'no armor',
            'cost': 0,
            'damage': 0,
            'armor': 0
        })
        rings = list(filter(lambda r: r['category']=='Rings', self.store))
        rings.append({
            'category': 'Rings',
            'name': 'no ring',
            'cost': 0,
            'damage': 0,
            'armor': 0
        })
        for w in weapons:
            #print(w['name'])
            for a in armors:
                #print(a['name'])
                for r1 in rings:
                    #print(r1['name'])
                    ec.append({
                        'cost': w['cost']+a['cost']+r1['cost'],
                        'damage': w['damage']+a['damage']+r1['damage'],
                        'armor': w['armor']+a['armor']+r1['armor']
                    })
                    for r2 in rings:
                        if r2['name'] == r1['name'] or r2['name'] == 'no ring':
                            ec.append({
                                'cost': w['cost']+a['cost']+r1['cost']+r2['cost'],
                                'damage': w['damage']+a['damage']+r1['damage']+r2['damage'],
                                'armor': w['armor']+a['armor']+r1['armor']+r2['armor']
                            })


        if sortedBy is not None:
            return sorted(ec, key=lambda c: c['cost'])
        else:
            return ec

if __name__ == "__main__":

    game = MyGame()

    game.setStoreItems(fromFile='itemCosts.txt')
    #print(game.store)

    boss = game.createCharacter(name='boss',fromFile='boss.txt')
    #print(boss)

    ec = game.equipmentCombinations(sortedBy="cost")

    for eq in ec:
        #print(eq)
        c = game.createCharacter(name='me',hitPoints=100,damage=eq['damage'],armor=eq['armor'])
        #print(c)
        #print(boss)

        winner = game.fight(c,deepcopy(boss))
        #print(winner)

        if winner['name'] == c['name']:
            print("Minimum cost for win: {}".format(eq['cost']))
            break