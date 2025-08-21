class test:
    def __init__(self, x, y):
        self.a = x * 2
        self.b = y * 3

    def t2(self):
        return f"{self.a} and {self.b}" 
    

c = test("Hello ","World ")
print(c.a , c.b, c.t2() )