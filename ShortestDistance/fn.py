from typing import Set, Tuple, List

def reverse_gen(l: List):
    return [i[::-1] for i in l]

class Pointer:
    def __init__(self, MAP: Set[tuple]):
        self.MAP = MAP

    def point(self, location: Tuple[int, int], f: Tuple[int, int] = None):
        return self.filter_points({i for i in self.MAP if location in i and f not in i}, location=location)

    def filter_points(
        self, 
        roads: Set[Tuple[Tuple[int, int], Tuple[int, int]]], 
        location: Tuple[int, int] = None
    ):
        directions: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()
        for i in roads:
            if location == i[0]:
                directions.add((location, i[1]))
            elif location == i[1]:
                directions.add((location, i[0]))
        return directions

def decider(
    directions: set, 
    location: Tuple[int, int], 
    to_location: Tuple[int, int]
):
    for road in directions:
        direction = road[1]
        print(to_location[0], direction[0], location[0])
        if to_location[0] < location[0]:
            if direction[0] < location[0]:
                return road
        elif to_location[0] > location[0]:
            if direction[0] > location[0]:
                return road
        elif to_location[1] < location[1]:
            if direction[1] < location[1]:
                return road
        elif to_location[1] > location[1]:
            if direction[1] > location[1]:
                return road

        
        