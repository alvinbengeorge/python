import matplotlib.pyplot as plt
import numpy as np

class Map:    
    '''
    Used for generating and plotting map
    '''
    def __init__(self):
        self.AREA = (101,101)
        x_range = range(0, self.AREA[0], 20)
        y_range = range(0, self.AREA[1], 20)
        ROADS = []
        for x in x_range:
            for y in y_range:
                ROADS.append(((x, y), (x+20, y)))
                ROADS.append(((x, y), (x, y+20)))
                ROADS.append(((x, y), (x, y-20)))
                ROADS.append(((x, y), (x-20, y)))
        self.ROADS = list(set(ROADS))

    def plot(self, points: list = []):
        _, ax = plt.subplots()
        ax.set(title="PATH")
        for i in points if points else self.ROADS:
            x , y = [], []
            for j in i:
                x.append(j[0])
                y.append(j[1])
            ax.plot(*map(np.array, (x,y)))
        plt.show()