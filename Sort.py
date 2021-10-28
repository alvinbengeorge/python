class Sort:
    def __init__(self, li):
        self.li = li
        self.len = len(li)

    def bubble(self):
        li = self.li
        for i in range(self.len):
            for j in range(self.len-i-1):
                if li[j]>li[j+1]:
                    li[j], li[j+1] = li[j+1], li[j]
        return li
    def insertion(self):
        li = self.li
        for i in range(1, self.len):
            j = i - 1
            while j>=0 and li[i]<li[j]:
                li[j+1] = li[j]
            else:
                li[j+1] = li[i]
        return li
