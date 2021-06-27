from lexer import Lexer

def start_compiler(path):
    file = open(path,'r',encoding='utf-8')
    lexer = Lexer(file)
    l = lexer.next().print()
    print(l)
    l = lexer.next().print()
    print(l)
    l = lexer.next().print()
    print(l)
    l = lexer.next().print()
    print(l)
    l = lexer.next().print()
    print(l)
    l = lexer.next().print()
    print(l)
if __name__ == '__main__':
    start_compiler('new.txt')

