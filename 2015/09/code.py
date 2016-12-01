import sys

# create the graph

class Node:
    def __init__(self,name):
        self.name = name
        self.trips = dict()

    def add_trip(self,destination,distance):
        self.trips[distance] = destination

class Map:
    def __init__(self):
        self.map = dict()

    def add_trip(self,city_from, city_to, distance):
        if city_from not in self.map:
            self.map[city_from] = Node(city_from)
        self.map[city_from].add_trip(city_to, distance.strip())

        if city_to not in self.map:
            self.map[city_to] = Node(city_to)
        self.map[city_to].add_trip(city_from, distance.strip())

    def find_shortest(self,city_from,cities_list):
        trips = self.map[city_from].trips
        shortest = sys.maxint * len(cities_list)
        longest = 0
        for d in trips.keys():
            if trips[d] in cities_list:
                cl = cities_list[:]
                cl.remove(trips[d])
                (s,l) = map(lambda x: int(d) + x, self.find_shortest(trips[d], cl))
                if s < shortest:
                    shortest = s
                if l > longest:
                    longest = l
        return (shortest, longest)





m = Map()
with open("input", "r") as trips:
    for trip in trips:
        (city_from, x, city_to, x, distance) = trip.split(" ")
        m.add_trip(city_from, city_to, distance)

shortest = sys.maxint
longest = 0
for city in m.map:
    cities_list = m.map.keys()
    cities_list.remove(city)
    (short_trip,long_trip) = m.find_shortest(city,cities_list)
    if short_trip < shortest:
        shortest = short_trip
    if long_trip > longest:
        longest = long_trip
print("Shortest: {}\nLongest: {}".format(shortest,longest))