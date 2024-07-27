class Runtime:
    def __init__(self):
        self.global_scope = {}

    def execute(self, command):
        exec(command, self.global_scope)

# Example usage
if __name__ == '__main__':
    runtime = Runtime()
    runtime.execute('x = 42')
    runtime.execute('print(x)')
