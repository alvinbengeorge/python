from typing import List

def safe_get(l: list, index: int):
    if len(l)>index:
        return l[index]
    return None

dsb_str = lambda l: [i[0] for i in l]

class Table:
    def __init__(self, l: List[tuple], describe: List[str] = []):
        count = 0 
        self.LIST = l
        if describe:
            for _ in describe:
                setattr(self, _, safe_get(l, count))
                count+=1
        else:
            self.TABLE = l

    def __list__(self):
        return self.LIST

