from collections import defaultdict

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

if __name__=='__main__':
    transition_table(input())