import numpy as np
from itertools import permutations, combinations

def generate_gray_code(n):
    return n ^ (n >> 1)


def generate_index():
    index = []
    for i in range(2**4):
        gray_code = generate_gray_code(i)
        if i % 4 == 0:
            index.append([])
        index[-1].append(gray_code)

    for i in range(len(index)):
        if i % 2 != 0:
            index[i].reverse()
    return index

INDEX = np.array(generate_index())
KMAP_ARRAY = np.zeros((4, 4), dtype=int)
POWERS = [2**i for i in range(4, -1, -1)]

def generate_coordinates(array):
    coordinates = {}
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 1:
                coordinates[INDEX[i][j]] = (i, j)

    return coordinates

def display_kmap(coordinates):
    for i in range(4):
        for j in range(4):
            if (i, j) in coordinates:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
    print()

def generate_groups(coordinates: dict):
    coordinates = list(coordinates.values())
    print(coordinates, "\n\n\n")
    groups, visited = [], []
    for i in POWERS:
        for j in list(combinations(coordinates, i)):
            groups.append(list(j))
    max_check_num = max([len(i) for i in groups])
    groups = sorted(groups, key=lambda x: len(x), reverse=True)
    display_kmap(coordinates)
    
    return max_check_num



a = list(map(int, input("Enter min terms with space: ").split()))
for val in a:
    for i in range(len(INDEX)):
        for j in range(len(INDEX[i])):
            if INDEX[i][j] == val:
                KMAP_ARRAY[i][j] = 1

coordinates = generate_coordinates(KMAP_ARRAY)
print(generate_groups(coordinates))

    