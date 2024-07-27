class MemoryManager:
    def __init__(self):
        self.memory = {}

    def allocate(self, name, value):
        self.memory[name] = value

    def deallocate(self, name):
        if name in self.memory:
            del self.memory[name]

    def get(self, name):
        return self.memory.get(name, None)

# Example usage
if __name__ == '__main__':
    mem = MemoryManager()
    mem.allocate("x", 42)
    print(mem.get("x"))
    mem.deallocate("x")
    print(mem.get("x"))
