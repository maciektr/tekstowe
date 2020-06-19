class Parser:
    __CONCAT_OP = '.'
    __OPERATORS = [".", "|", "*"]
    __PRECEDENCE = {
        "|": 0,
        ".": 1,
        "*": 2,
    }

    @staticmethod
    def parse_regex(regex: str):
        return Parser.to_postfix(Parser.preprocessing(regex))

    @staticmethod
    def preprocessing(regex: str):
        # print('regex', regex)
        operators = set(Parser.__OPERATORS + [')'])
        no_concat_past = {'|', '('}
        result = ''
        i = 0
        while i < len(regex):
            token = regex[i]
            if token in operators:
                result += token
            elif token == '[':
                result += Parser.__CONCAT_OP
                result += '('
                k = i + 1
                while k < len(regex) and regex[k] != ']':
                    k += 1
                result += '|'.join(list(regex[i + 1:k]))
                result += ')'
                i = k
            elif token == '\\':
                pass
            else:
                if i != 0 and regex[i - 1] not in no_concat_past:
                    result += Parser.__CONCAT_OP
                result += token
            i += 1
        # print('pre', result)
        return result

    @staticmethod
    def to_postfix(expression: str):
        # https://en.wikipedia.org/wiki/Shunting-yard_algorithm
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
