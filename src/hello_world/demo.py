"""
    Dynamical Typing
"""

a = 5
print(type(a))
a = 5.0
print(type(a))
a = '5'
print(type(a))

print(type(print))

def func(a):
    return(a * 5)
print(type(func))

print(func(5))
print(func('Hello'))
print(func('Na') + ' Batman!')



"""
    Basic Data Types
"""

my_dict = {'key': 1, 'x': 'string'}
print(my_dict['key'])

a = 'hello'
a.upper() # methods do not modify the object itself
print(a)

b = a.upper()
print(a, b)
print(a[2])

a = [3, 2, 1]
b = a
print(id(a), id(b))

b.sort()
print(a)

# Attention when using mutable default arguments, as they are kept in memory
def func(x=[]):
    x.append('world!')
    print(x)

a = ['hello']
func(a)
func(a)

func()
func()



"""
    Using Iterators
"""

# Iterate over string and print out  unicode representation.
s = 'HELLO'
for c in s:
    print(f'{c}={ord(c)}')

# Define an iterator with the yield keyword and manually step through it. 
def my_iter(num):
    c = num
    for ind in range(num-1, 0, -1):
        print(f'Now at {ind=}')
        c *= ind
        yield c

g = my_iter(20)
x = next(g)
print(f'{x=}')

try: 
    x = next(g) # returns StopIteration if the end is reached
except StopIteration as e:
    print(e)
else:
    print('No exception raised')
finally:
    print('This bit is always executed')


"""
    Decorators
"""

FUNCS = {}

def register(func):
    """Decorator to store functions in a dictionary"""
    FUNCS[func.__name__] = func
    return func

@register
def add(a, b):
    return a + b

@register
def sub(a, b):
    return a - b


def say_hello(func):
    """Decorator that prints hello when calling the function"""
    def hello_func(*args, **kwargs):
        print('hello!')
        return func(*args, **kwargs)
    
    return hello_func

@register
@say_hello
def mul(a, b):
    return a * b

c = mul(2, 3)
print(c)

print(FUNCS)