def naive(path, pattern):
    file = open(path,'r')
    res = []
    line_index = 0
    for line in file:
        line_index+=1
        for i in range(len(line) - len(pattern) +1):
            if line[i:i+len(pattern)]==pattern:
                res.append((line_index,i))
    
    return res

if __name__=='__main__':
    # path='1997_714.txt' 
    # pattern='art'
 
    path='wikipedia-tail-kruszwil.txt'
    pattern='kruszwil'

    # path='a.txt'
    # pattern='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

    res = naive(path, pattern)
    print('\n'.join(map(lambda x:'line: '+str(x[0])+'; index:'+str(x[1]),res)))
    print("Found "+str(len(res))+" matches")