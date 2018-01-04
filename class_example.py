class Test1():
    def Test2(self):
        a = 100*2
        return a
    def Test3(self):
        b = self.Test2() * 500
        return b

if __name__ == '__main__':
    c = Test1()
    print (c.Test2())
    print (c.Test3())
