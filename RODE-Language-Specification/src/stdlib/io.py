def print_output(output):
    print(output)

def read_input(prompt=""):
    return input(prompt)

# Example usage
if __name__ == '__main__':
    print_output("Hello, World!")
    user_input = read_input("Enter something: ")
    print_output(f"You entered: {user_input}")
