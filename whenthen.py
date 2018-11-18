def whenthen(fn):
    cashe = {}
    def fract(*args, **kwargs):
        check()
        for key in cashe.keys():
            if key(*args, **kwargs):
                return cashe[key](*args, **kwargs)
        return fn(*args, **kwargs)    
    
    def when(fn):
        cashe[fn] = ''
        global buff, k
        k += 1
        buff = fn
        return fract
    
    def then(fn):
        cashe[buff] = fn
        global k
        k -= 1
        check()
        return fract
    
    def check():
        if k != 0:
            raise SyntaxError
        
    fract.when = when
    fract.then = then
    
    return fract
