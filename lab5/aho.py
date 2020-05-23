from collections import defaultdict


class AhoCorasick:
    __FAIL = -1

    def __init__(self, patterns):
        self.transition = None
        self.output = defaultdict(lambda: set(), {})
        self.transition_table(patterns)

    def create_fail(self):
        fail = defaultdict(lambda: self.__FAIL, {})
        queue = []

        for key, val in dict(self.transition[0]).items():
            if val != self.__FAIL:
                queue.append(val)
                fail[val] = 0

        self.transition[0] = defaultdict(lambda: 0, self.transition[0])

        while len(queue) > 0:
            t = queue.pop(0)
            for key, val in dict(self.transition[t]).items():
                if val != self.__FAIL:
                    queue.append(val)
                    st = fail[t]
                    while self.transition[st][key] == self.__FAIL:
                        st = fail[st]
                    fail[val] = self.transition[st][key]
                    self.output[val] |= self.output[self.transition[st][key]]

        for key, val in dict(fail).items():
            for _key, _val in dict(self.transition[val]).items():
                if _key not in self.transition[key].keys():
                    self.transition[key][_key] = _val
            self.transition[key] = defaultdict(lambda: val, dict(self.transition[key]))

    def transition_table(self, patterns):
        self.transition = [defaultdict(lambda: self.__FAIL, {})]

        for pattern in patterns:
            k = 0
            for q in range(0, len(pattern)):
                if not self.transition[k][pattern[q]] == self.__FAIL:
                    k = self.transition[k][pattern[q]]
                else:
                    self.transition.append(defaultdict(lambda: self.__FAIL, {}))  # self.transition[k]))
                    self.transition[k][pattern[q]] = len(self.transition) - 1
                    k = self.transition[k][pattern[q]]
                if q == len(pattern) - 1:
                    self.output[k].add(''.join(pattern))

        # print(list(map(lambda x: dict(x), self.transition)))
        self.create_fail()
        # print(list(map(lambda x: dict(x), self.transition)))
        return self.transition


if __name__ == '__main__':
    pass
