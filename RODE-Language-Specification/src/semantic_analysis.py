class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name, self.generic_visit)
        return method(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')

    def visit_Num(self, node):
        return int(node.value)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.op == '+':
            return left + right
        else:
            raise Exception(f'Unsupported operator {node.op}')

    def visit_Var(self, node):
        if node.name not in self.symbol_table:
            raise Exception(f'Variable {node.name} not declared')
        return self.symbol_table[node.name]

    def visit_Assign(self, node):
        var_name = node.left.name
        var_value = self.visit(node.right)
        self.symbol_table[var_name] = var_value

    def visit_Print(self, node):
        value = self.visit(node.expr)
        print(value)

# Example usage
if __name__ == '__main__':
    from ast import Num, BinOp, Var, Assign, Print

    # Example of creating an AST for "x = 42; print(x + 8)"
    variable = Var("x")
    number = Num(token=Token(type="NUMBER", value=42, line=1, column=1))
    assign = Assign(left=variable, op="=", right=number)
    expr = BinOp(left=variable, op='+', right=Num(token=Token(type="NUMBER", value=8, line=1, column=1)))
    print_stmt = Print(expr=expr)

    analyzer = SemanticAnalyzer()
    analyzer.visit(assign)
    analyzer.visit(print_stmt)
