from collections import MutableMapping
import os
        
class DirDict(MutableMapping):
    def __init__(self, path=''):
        if path != '':
            self.path = path + '/'
        else:
            self.path = path
    
    def __getitem__(self, key):
        try:
            f = open(self.path + key)
            tmp = ''
            for line in f:
                tmp += line
        except:
            raise KeyError
        return tmp
    
    def __setitem__(self, key, value):
        f = open(self.path + key, 'w')
        value = str(value)
        f.write(value)
        f.close()
        
    def __iter__(self):
        for i in os.listdir():
            yield i
        
    def __len__(self):
        return len(os.listdir())
    
    def __repr__(self):
        return "DirDict"
        
    def __delitem__(self, key):
        os.remove(key)
