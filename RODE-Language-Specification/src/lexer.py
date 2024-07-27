import re

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, {self.line}, {self.column})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_char = ''
        self.current_line = 1
        self.current_column = 0
        self.advance()

    def advance(self):
        if self.current_column < len(self.source_code):
            self.current_char = self.source_code[self.current_column]
            self.current_column += 1
        else:
            self.current_char = None

    def tokenize(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
            elif self.current_char.isalpha():
                self.tokens.append(self.make_identifier())
            elif self.current_char.isdigit():
                self.tokens.append(self.make_number())
            elif self.current_char == '"':
                self.tokens.append(self.make_string())
            elif self.current_char == '+':
                self.tokens.append(Token('PLUS', '+', self.current_line, self.current_column))
                self.advance()
            elif self.current_char == '=':
                self.tokens.append(Token('EQUAL', '=', self.current_line, self.current_column))
                self.advance()
            elif self.current_char in '-*/()':
                self.tokens.append(Token('SYMBOL', self.current_char, self.current_line, self.current_column))
                self.advance()
            else:
                self.error()
        return self.tokens

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            if self.current_char == '\n':
                self.current_line += 1
            self.advance()

    def make_identifier(self):
        start_pos = self.current_column - 1
        identifier = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            identifier += self.current_char
            self.advance()
        return Token('IDENTIFIER', identifier, self.current_line, start_pos)

    def make_number(self):
        start_pos = self.current_column - 1
        number = ''
        while self.current_char is not None and self.current_char.isdigit():
            number += self.current_char
            self.advance()
        return Token('NUMBER', number, self.current_line, start_pos)

    def make_string(self):
        self.advance()  # Skip the opening quote
        start_pos = self.current_column - 1
        string = ''
        while self.current
