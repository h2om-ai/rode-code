class ASTNode:
    pass

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(ASTNode):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]

    def parse(self):
        return self.expr()

    def factor(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self.advance()
            return Num(token)
        self.error()

    def term(self):
        node = self.factor()
        while self.current_token.type == 'PLUS':
            token = self.current_token
            self.advance()
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token.type == 'PLUS':
            token = self.current_token
            self.advance()
            node = BinOp(left=node, op=token, right=self.term())
        return node

    def error(self):
        raise Exception('Invalid syntax')

# Example usage
if __name__ == '__main__':
    from lexer import Lexer

    source_code = '3 + 5 + 2'
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)
