class Lexem:
    def __init__(self,coordinate,type,code,value):
        self.code = code
        self.coordinate = coordinate
        self.type = type
        self.value = value
    def print(self):
        return f'{self.coordinate}        {self.type}        {self.code}        {self.value}'