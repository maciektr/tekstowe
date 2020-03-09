def kmp(path, pattern):
    file = open(path,'r')
    res = []
    line_index = 0
    
    pi = prefix_function(pattern)
    for line in file:
        line_index+=1
        q = 0
        for i in range(len(line)):
            while(q > 0 and pattern[q] != line[i]):
                q = pi[q-1]
            if(pattern[q] == line[i]):
                q = q + 1
            if(q == len(pattern)):
                res.append((line_index,i))
                q = pi[q-1]
    return res

def prefix_function(pattern):
    pi = [0]
    k = 0
    for q in range(1, len(pattern)):
        while(k > 0 and pattern[k] != pattern[q]):
            k = pi[k-1]
        if(pattern[k] == pattern[q]):
            k = k + 1
        pi.append(k)
    return pi

if __name__=='__main__':
    # path='1997_714.txt' 
    # pattern='art'
 
    path='wikipedia-tail-kruszwil.txt'
    pattern='kruszwil'

    # path='a.txt'
    # pattern='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

    res = kmp(path, pattern)
    print('\n'.join(map(lambda x:'line: '+str(x[0])+'; index:'+str(x[1]),res)))
    print("Found "+str(len(res))+" matches")