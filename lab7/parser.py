class Parser:
    CONCAT_OP = '^' # chr(6)
    MATCH_ALL_OP = '.'
    __OPERATORS = ['|', '*', '+', '?', CONCAT_OP]
    __PRECEDENCE = {
        '|': 0,
        CONCAT_OP: 1,
        '*': 2,
        '+': 2,
        '?': 2,
    }
    __WHITE_CHARS = [' ', '\t', '\n', '\r', '\f', '\v']

    @staticmethod
    def parse_regex(regex: str, verbose=False):
        preproc = Parser.preprocessing(regex)
        if verbose:
            print('Preprocessed regex:', preproc)
        postfix = Parser.to_postfix(preproc)
        return postfix

    @staticmethod
    def preprocessing(regex: str):
        operators = set(Parser.__OPERATORS + [')'])
        no_concat_past = {'|', '('}
        result = ''
        i = 0
        while i < len(regex):
            token = regex[i]
            if token == '[':
                result += Parser.CONCAT_OP + '('
                k = i + 1
                group = []
                while k < len(regex) and regex[k] != ']':
                    if regex[k] == '-':
                        group.extend(Parser.chars_between(regex[k-1], regex[k+1]))
                    else:
                        group.append(regex[k])
                    k += 1
                result += '|'.join(group)
                result += ')'
                i = k
            elif token == '\\':
                result += Parser.CONCAT_OP + '(' + '|'.join(Parser.add_group_by_symbol(regex[i + 1])) + ')'
                i += 1
            else:
                if i > 0 and token not in operators and regex[i - 1] not in no_concat_past:
                    result += Parser.CONCAT_OP
                result += token
            i += 1
        return result

    @staticmethod
    def to_postfix(expression: str):
        result = []
        operator_stack = []

        for token in expression:
            if token in Parser.__OPERATORS:
                while (len(operator_stack) > 0
                       and operator_stack[-1] != '('
                       and Parser.__PRECEDENCE[operator_stack[-1]] >= Parser.__PRECEDENCE[token]
                ):
                    result.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack[-1] != '(':
                    result.append(operator_stack.pop())
                operator_stack.pop()
            else:
                result.append(token)

        result.extend(reversed(operator_stack))
        return ''.join(result)

    @staticmethod
    def chars_between(low, high):
        return [chr(x) for x in range(ord(low) + 1, ord(high))]

    @staticmethod
    def add_group_by_symbol(symbol):
        if symbol == 'd':
            # Match digit
            return Parser.chars_between('0', '9') + ['0', '9']

        if symbol == 's':
            # Match whitespace
            return Parser.__WHITE_CHARS

        if symbol == 'w':
            # Match word symbols
            return Parser.chars_between('a', 'z') + \
                   Parser.chars_between('A', 'Z') + \
                   Parser.chars_between('0', '9') + \
                   ['a', 'z', 'A', 'Z', '0', '9']

        if symbol == 'c':
            # Match alphabetical
            return Parser.chars_between('a', 'z') + \
                   Parser.chars_between('A', 'Z') + \
                   ['a', 'z', 'A', 'Z']
