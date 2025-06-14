def resta(*parNums:float)->float:
    res=0
    for item in parNums:
        res-=item
        
    return res


def suma(*parNums:float)->float:
    res=0
    for item in parNums:
        res+=item

    return res

def multiplica(*parNums:float)->float:
    res=1
    for item in parNums:
        res*=item

    return res

def divicion(parNum:float, parNum2 :float)-> float:
    res = parNum/parNum2
    residuo= parNum % parNum2

    return res, residuo