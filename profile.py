import inspect
import time
from types import FunctionType

def tmp(fn, klass_name=''):
    def arbaiten(*args, **kwargs):
        start_time = time.clock()
        print("'{}.{}' started".format(klass_name, fn.__name__))
        fn(*args, **kwargs)
        print("'{}.{}' finished in {}s".format(klass_name, fn.__name__, round(time.clock() - start_time, 2)))
    return arbaiten
    
def profile(klass):
    if isinstance(klass, FunctionType):
        return tmp(klass)
    for attr_name in inspect.getmembers(klass, predicate=inspect.isfunction):
        attr = getattr(klass, attr_name[0])
        setattr(klass, attr_name[0], tmp(attr, klass.__name__))
    return klass
