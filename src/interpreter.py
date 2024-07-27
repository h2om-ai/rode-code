# Importing necessary classes
from parser import Num, BinOp, Parser
from lexer import Lexer

class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def visit(self, node):
        if isinstance(node, Num):
            return self.visit_Num(node)
        elif isinstance(node, BinOp):
            return self.visit_BinOp(node)

    def visit_Num(self, node):
        return int(node.value)

    def visit_BinOp(self, node):
        if node.op.type == 'PLUS':
            return self.visit(node.left) + self.visit(node.right)

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)

# Example usage
if __name__ == '__main__':
    source_code = '3 + 5 + 2'
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    interpreter = Interpreter(parser)
    result = interpreter.interpret()
    print(result)
