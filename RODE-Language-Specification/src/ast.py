class ASTNode:
    """Base class for all AST nodes."""
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

class Var(ASTNode):
    def __init__(self, name):
        self.name = name

class Assign(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Print(ASTNode):
    def __init__(self, expr):
        self.expr = expr

# Example usage
if __name__ == '__main__':
    # Example of creating an AST for "x = 42"
    variable = Var("x")
    number = Num(token=Token(type="NUMBER", value=42, line=1, column=1))
    assign = Assign(left=variable, op="=", right=number)
    print(assign)
