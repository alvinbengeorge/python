from fn import Pointer, reverse_gen, decider
from Map import Map
from typing import List, Set, Tuple

MAP: Map = Map()
journey: List[Tuple[int, int]] = []
COMPLETED_JOURNEY: bool = False

point = Set[Tuple[Tuple[int, int], Tuple[int, int]]]
m: point = set(MAP.ROADS+reverse_gen(MAP.ROADS))
p: Pointer = Pointer(m)

starting_location = tuple(map(int, input("Enter from: ").strip().split(",")))
ending_location = tuple(map(int, input("Enter to  :").strip().split(",")))
print(starting_location, ending_location)



current_location = starting_location
while not COMPLETED_JOURNEY:
    directions = p.point(
        current_location,
        journey[-1] if not len(journey) < 1 else None
    )
    to_point = decider(directions, current_location, ending_location)
    current_location = to_point[1]
    journey.append(to_point)
    if to_point[1] == ending_location:
        print("Done")
        COMPLETED_JOURNEY = True

MAP.plot(journey)