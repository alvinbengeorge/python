# function(1, 2, 3, 4, 5)
# function1(name="Alvin", age=10)

def function(*args):
    print(args)

def function1(**kwargs):
    print(kwargs)

function(1, 2, 3, 4, 5)
function1(name="Alvin", age=10)

def func(year, *args, **kwargs):
    print(year)

def new_print(values, kwargs: dict):
    print(values, kwargs)
    print(*values, **kwargs)

control = {
    'sep': "-",
    'end': ')'
}

new_print((1, 2, 3, 4), kwargs=control)