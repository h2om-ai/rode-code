# RODE Language Specification

Welcome to the RODE Language Specification project. This project includes a lexer, parser, and interpreter for the RODE programming language.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Lexer](#lexer)
   - [Parser](#parser)
   - [Interpreter](#interpreter)
4. [Examples](#examples)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

This project implements a simple lexer, parser, and interpreter for the RODE programming language. The language supports basic arithmetic operations and variable assignments.

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/h2om-ai/rode-code.git
cd rode-code

Usage
Lexer
The lexer (or lexical analyzer) converts the source code into a list of tokens. Each token represents a meaningful unit in the code, such as keywords, identifiers, or operators.

Example Usage
To run the lexer on a sample source code, use the following command:

python src/lexer.py

Code
Here is an example of how to use the lexer:

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
            elif self.current_char == '\"':
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
        while self.current_char is not None and self.current_char != '\"':
            string += self.current_char
            self.advance()
        self.advance()  # Skip the closing quote
        return Token('STRING', string, self.current_line, start_pos)

    def error(self):
        raise Exception(f"Illegal character '{self.current_char}' at line {self.current_line}")

# Example usage
if __name__ == '__main__':
    source_code = 'let x = 42 + 8'
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    print(tokens)

Parser
The parser analyzes the list of tokens generated by the lexer and builds an abstract syntax tree (AST). The AST represents the syntactic structure of the source code.

Example Usage
To run the parser on a sample source code, use the following command:

python src/parser.py

Code
Here is an example of how to use the parser:

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

Interpreter
The interpreter evaluates the abstract syntax tree (AST) generated by the parser and produces the result of the computation.

Example Usage
To run the interpreter on a sample source code, use the following command:

python src/interpreter.py

Code
Here is an example of how to use the interpreter:

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

Examples
You can find more example programs in the examples directory. To run an example, use the following command:

python src/interpreter.py examples/hello_world.rode

# Contributing to RODE Language Specification

We welcome contributions to the RODE Language Specification project! To get started, please read the following guidelines.

## How to Contribute

1. **Fork the Repository**

   Fork the [repository](https://github.com/h2om-ai/rode-code) on GitHub.

2. **Clone Your Fork**

   Clone your forked repository to your local machine:

   ```bash
   git clone https://github.com/your-username/rode-code.git
   cd rode-code

