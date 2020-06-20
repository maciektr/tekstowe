from parser import Parser


class State:
    def __init__(self, final=False):
        self.final = final
        self.transitions = {}
        self.epsilon_transitions = []

    def add_epsilon_transition(self, to):
        self.epsilon_transitions.append(to)

    def add_transition(self, to, symbol):
        self.transitions[symbol] = to

    def walk_eps(self, seen=None):
        if seen is None:
            seen = set()

        if len(self.epsilon_transitions) == 0:
            return [self]

        result = []
        for state in self.epsilon_transitions:
            if state not in seen:
                seen.add(state)
                result.extend(state.walk_eps(seen))

        return result


class Nfa:
    def __init__(self, start: State, end: State):
        self.start = start
        self.end = end

    @staticmethod
    def from_epsilon():
        start = State(final=False)
        end = State(final=True)
        start.add_epsilon_transition(end)
        return Nfa(start, end)

    @staticmethod
    def from_symbol(symbol):
        start = State(final=False)
        end = State(final=True)
        start.add_transition(end, symbol)
        return Nfa(start, end)

    @staticmethod
    def from_postfix(postfix_expr: str):
        if postfix_expr == '':
            return Nfa.from_epsilon()

        stack = []
        for token in postfix_expr:
            if token == '*':
                stack.append(stack.pop().closure())
            elif token == '+':
                stack.append(stack.pop().one_or_more_closure())
            elif token == '?':
                stack.append(stack.pop().maybe())
            elif token == '|':
                right = stack.pop()
                left = stack.pop()
                stack.append(left.union(right))
            elif token == Parser.CONCAT_OP:
                right = stack.pop()
                left = stack.pop()
                stack.append(left.concat(right))
            else:
                stack.append(Nfa.from_symbol(token))

        return stack.pop()

    def concat(self, second: 'Nfa'):
        self.end.add_epsilon_transition(second.start)
        self.end.final = False
        return Nfa(self.start, second.end)

    def union(self, second: 'Nfa'):
        start = State(final=False)
        start.add_epsilon_transition(self.start)
        start.add_epsilon_transition(second.start)

        end = State(final=True)
        self.end.add_epsilon_transition(end)
        self.end.final = False
        second.end.add_epsilon_transition(end)
        second.end.final = False

        return Nfa(start, end)

    def padding(self):
        start = State(final=False)
        end = State(final=True)

        start.add_epsilon_transition(self.start)
        self.end.add_epsilon_transition(end)
        self.end.final = False

        return Nfa(start, end)

    def one_or_more_closure(self):
        nfa = self.padding()
        self.end.add_epsilon_transition(self.start)
        return nfa

    def closure(self):
        nfa = self.one_or_more_closure()
        nfa.start.add_epsilon_transition(nfa.end)
        return nfa

    def maybe(self):
        nfa = self.padding()
        nfa.start.add_epsilon_transition(nfa.end)
        return nfa
