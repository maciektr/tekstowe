from collections import defaultdict


class Regex:
    __DEFAULT_VAL = 0
    __WHITE_CHARS = [' ', '\t', '\n', '\r', '\f', '\v']
    __SPECIAL_CHARS = ['_']
    __EMPTY_PROD = 0

    def __init__(self, regex):
        self.transition = []
        self.transition_table(regex)

    def add_digits(self, i, old_k, k):
        for digit in range(0, 10):
            p = chr(digit + ord('0'))
            self.transition[i][p] = i + 1
            k = max(k, self.transition[old_k][p])
        return k

    def add_lower_chars(self, i, old_k, k):
        for char in range(ord('a'), ord('z') + 1):
            p = chr(char)
            self.transition[i][p] = i + 1
            k = max(k, self.transition[old_k][p])
        return k

    def add_upper_chars(self, i, old_k, k):
        for char in range(ord('A'), ord('Z') + 1):
            p = chr(char)
            self.transition[i][p] = i + 1
            k = max(k, self.transition[old_k][p])
        return k

    def add_white_chars(self, i, old_k, k):
        for char in Regex.__WHITE_CHARS:
            self.transition[i][char] = i + 1
            k = max(k, self.transition[old_k][char])
        return k

    def add_special(self, i, old_k, k):
        for char in Regex.__SPECIAL_CHARS:
            self.transition[i][char] = i + 1
            k = max(k, self.transition[old_k][char])
        return k

    def transition_table(self, pattern):
        self.transition = [defaultdict(lambda: Regex.__DEFAULT_VAL, {})]
        self.transition[0][pattern[0]] = 1

        k = 0
        self.transition.append(defaultdict(lambda: Regex.__DEFAULT_VAL, self.transition[k]))
        i = 1
        q = 1
        seen_i = 0
        while q < len(pattern): # - seen_i:
            add_next = True
            if q < len(pattern):
                if pattern[q] == '[':
                    # self.transition.append(defaultdict(lambda: Regex.__DEFAULT_VAL, self.transition[k]))
                    # i += 1
                    q += 1
                    old_k = k
                    k = self.transition[k][pattern[q]]
                    while pattern[q] != ']':
                        self.transition[i][pattern[q]] = i + 1
                        k = max(k, self.transition[old_k][pattern[q]])
                        q += 1
                elif pattern[q] == '\\':
                    self.transition.append(defaultdict(lambda: Regex.__DEFAULT_VAL, self.transition[k]))
                    q += 1
                    if pattern[q] == 'd':
                        old_k = k
                        k = self.add_digits(i, old_k, self.transition[k]['0'])
                        q += 1
                    elif pattern[q] == 'D':
                        old_k = k
                        k = self.add_lower_chars(i, old_k, self.transition[k]['a'])
                        k = self.add_upper_chars(i, old_k, k)
                        k = self.add_white_chars(i, old_k, k)
                        q += 1
                    elif pattern[q] == 's' or pattern[q] == 'W':
                        k = self.add_white_chars(i, k, self.transition[k][' '])
                        q += 1
                    elif pattern[q] == 'S':
                        old_k = k
                        k = self.add_lower_chars(i, old_k, self.transition[k]['a'])
                        k = self.add_upper_chars(i, old_k, k)
                        k = self.add_digits(i, old_k, k)
                        q += 1
                    elif pattern[q] == 'w':
                        old_k = k
                        k = self.add_special(i, old_k, self.transition[k]['_'])
                        q += 1
                elif pattern[q] == '*':
                    if pattern[q-1] == ']':
                        pass
                    elif pattern[q-1] == ')':
                        pass
                    else:
                        print('*', i)
                        self.transition[i-1][pattern[q - 1]] = i
                        self.transition[i-1][Regex.__EMPTY_PROD] = i
                        # self.transition.append(defaultdict(lambda: Regex.__DEFAULT_VAL, self.transition[k]))
                        self.transition[i][pattern[q-1]] = i
                        add_next = False
                        # i+=1

                        # self.transition[i][pattern[q-1]] = i
                        # self.transition[i][Regex.__EMPTY_PROD] = i + 1
                        # i -= 1
                    # q += 1
                elif pattern[q] == '+':
                    if pattern[q-1] == ']':
                        pass
                    elif pattern[q-1] == ')':
                        pass
                    else:
                        pass
                        # self.transition[i][pattern[q-1]] = i

                    # q += 1
                elif pattern[q] == '?':
                    if pattern[q - 1] == ']':
                        pass
                    elif pattern[q - 1] == ')':
                        pass
                    else:
                        pass
                        # self.transition[i][pattern[q - 1]] = i
                    # q += 1
                elif pattern[q] == '(':
                    pass
                else:
                    # self.transition.append(defaultdict(lambda: Regex.__DEFAULT_VAL, self.transition[k]))
                    # i += 1
                    # print('I', i, len(self.transition))
                    self.transition[i][pattern[q]] = i + 1
                    k = self.transition[k][pattern[q]]
            # else:
            if add_next:
                self.transition.append(defaultdict(lambda: Regex.__DEFAULT_VAL, self.transition[k]))
                i += 1
            q += 1

    def match(self, text):
        a = len(self.transition) - 1
        res = []

        # q = 0
        # for s in range(len(text)):
        #     if self.transition[q]['.'] != Regex.__DEFAULT_VAL:
        #         q = self.transition[q]['.']
        #     else:
        #         q = self.transition[q][text[s]]
        #     if q == a:
        #         res.append(s)

        # q = 0
        queue = []
        queue.append((0, 0))
        while len(queue) > 0:
            pos, state = queue[-1]
            queue.pop()
            q = state
            s = pos
            # for s in range(pos, len(text)):
            # print('Que', s, text[s], state)
            while s < len(text):
                # print('M', text[s], q)
                    # print("MATCHED")
                if self.transition[q][Regex.__EMPTY_PROD] != Regex.__DEFAULT_VAL:
                    # print("QUE append")
                    queue.append((s, self.transition[q][Regex.__EMPTY_PROD]))
                    # q = self.transition[q][Regex.__EMPTY_PROD]
                    # s -= 1
                if self.transition[q]['.'] != Regex.__DEFAULT_VAL:
                    q = self.transition[q]['.']
                else:
                    q = self.transition[q][text[s]]
                if q == a:
                    res.append(s)
                s += 1

        return list(set(res))


if __name__ == '__main__':
    # 'aba*f*de'
    r = Regex('ab*c*d')
    for t in r.transition:
        print(t)
    print(r.match('aabbbbbbcccccd'))
