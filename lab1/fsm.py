from collections import defaultdict
import re

def transition_table(pattern):
    result = []
    result.append(defaultdict(lambda :0, {}))
    result[0][pattern[0]] = 1

    k = 0
    for q in range(1,len(pattern)+1):
        result.append(defaultdict(lambda :0, result[k]))
        if q < len(pattern):
            result[q][pattern[q]] = q+1
            k =result[k][pattern[q]]
    return result

def fsm(path, pattern):
    transition = transition_table(pattern)
    a = len(transition) -1

    res = []
    file = open(path,'r')
    line_index = 0
    for line in file:
        q=0
        for s in range(len(line)):
            q = transition[q][line[s]]
            if q==a:
                res.append((line_index, s))
    return res

if __name__=='__main__':
    # path='1997_714.txt' 
    # pattern='art'
 
    path='wikipedia-tail-kruszwil.txt'
    pattern='kruszwil'

    # path='ab.txt'
    # pattern='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB'

    res = fsm(path, pattern)
    print('\n'.join(map(lambda x:'line: '+str(x[0])+'; index:'+str(x[1]),res)))
    print("Found "+str(len(res))+" matches")