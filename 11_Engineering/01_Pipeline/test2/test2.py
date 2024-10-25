#print("hello world")


class test:
    temp0 = "0"
    temp1 = "1"

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def test_concat(self):
        return self.a + self.b + self.c
    
    def test_concat_v2(self, temp = temp0):
        return self.a + self.b + temp