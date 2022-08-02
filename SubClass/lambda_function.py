square = lambda n: n*n

n=130
if (c:=square(n))%2 ==0:
    print(c)

for _ in [(i,j) for i in range(1, 4) for j in range(1, 4)]:
    #print(_.count(1))
    pass


class Person:
    '''
    Initialising Kevin 😂
    '''
    def __init__(self, *friends) -> None:
        self.phone_number = 123456789
        self.name="Kevin"
        self.friends=friends


class WorkingClass(Person):

    def return_info(self):
        return self.phone_number, self.name, self.friends

print(*WorkingClass("A", "B", "C").return_info())