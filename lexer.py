from lexem import Lexem

class Lexer:
    def __init__(self,file):
        self.file = file
        self.symbol = self.file.read(1)
        self.indefinite = 'indefinite'
        self.identifier = 'identifier'
        self.reserved_word = 'reserved_word'
        self.integer = 'integer'
        self.line = 1
        self.col = 1
        self.reserved = ["array", "asm", "begin", "case", "const", "constructor", "destructor", "do",
                            "downto", "else", "end", "exports", "file", "for", "function", "goto", "if", "implementation",
                            "in", "inherited", "inline", "interface", "label", "library", "nil", "object",
                             "of", "packed", "procedure", "program", "record", "repeat", "set", "shl", "shr",
                            "string", "then", "to", "type", "unit", "until", "uses", "var", "while", "with", "xor", "abs", "arctan", "boolean", "char", "cos", "dispose", "eof", "eoln", "exp",
                            "false", "get", "input", "integer", "ln", "maxint", "new", "output",
                            "pack", "page", "pred", "put", "read", "readln", "real", "reset", "rewrite",
                            "sin", "sqr", "sqrt", "succ", "text", "true", "unpack", "write", "writeln"]
        self.buffer = ''
        self.coordinates = []
        self.state = self.indefinite
        self.space = [' ','\n','\t','\0','\r']

    def save_coordinates(self):
        self.coordinates = [self.line, self.col]

    def add_buffer(self, val):
        self.buffer += val

    def clear_buffer(self):
        self.buffer = ''

    def next(self):
        self.clear_buffer()
        while self.symbol or self.buffer:
            if self.state == self.indefinite:
                if self.space.count(self.symbol):

                    if self.symbol == '\n':
                        self.line += 1
                        self.col = 0
                    self.getsymbol()

                elif self.symbol.isalpha():
                    self.add_buffer(self.symbol)
                    self.state = self.identifier
                    self.save_coordinates()
                    self.getsymbol()

                elif self.symbol.isdigit():
                    self.add_buffer(self.symbol)
                    self.state = self.integer
                    self.save_coordinates()
                    self.getsymbol()
            elif self.state == self.integer:

                if self.symbol.isdigit():
                    self.add_buffer(self.symbol)
                    self.getsymbol()

                else:
                    self.state = self.indefinite
                    return Lexem(self.coordinates, self.integer, self.buffer,int(self.buffer))

            elif self.state == self.identifier:
                if self.symbol.isalpha() or self.symbol.isdigit() or self.symbol == '_':
                    self.add_buffer(self.symbol)
                    self.getsymbol()

                else:
                    self.state = self.indefinite
                    if self.reserved.count(self.buffer):
                        return Lexem(self.coordinates, self.reserved_word, self.buffer, self.buffer)

                    else:
                        return Lexem(self.coordinates, self.identifier, self.buffer, self.buffer)

    def getsymbol(self):
        self.symbol = self.file.read(1)
        self.col += 1