def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero")

# Example usage
if __name__ == '__main__':
    print(add(2, 3))
    print(subtract(5, 2))
    print(multiply(3, 4))
    print(divide(10, 2))
