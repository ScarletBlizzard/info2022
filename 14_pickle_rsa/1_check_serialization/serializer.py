import pickle
from collections import deque

#data = open("test", "w") # TypeError: cannot pickle '_io.TextIOWrapper' object
data = iter(range(10)) # OK
data = print # OK
def example_func():
    pass
data = example_func # OK
#data = lambda x: x**2 # _pickle.PicklingError: Can't pickle <function <lambda> at 0x7f53f4aff430>: attribute lookup <lambda> on __main__ failed
class ExampleCls:
    pass
data = ExampleCls # OK
data = deque # OK

with open('data.pickle', 'wb') as f:
    # Сериализация словаря data с использованием
    # последней доступной версии протокола.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
