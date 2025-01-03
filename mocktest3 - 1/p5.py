class C:
    def __init__(self, counter):
        self.counter = counter
    
    def m1(self):
        return self.counter
    
    def m2(self):
        self.counter += 1

    def m3(self):
        self.counter -= 1
    
    def m4(self, n):
        self.n = n
        self.counter += n

    def __str__(self):
        return f'{self.counter}'

def main():
    c = C(5)
    print(c.m1())
    c.m2()
    print(c.m1())
    c.m4(-8)
    print(c.m1())
    c.m3()
    print(c.m1())
    c.m4(10)
    print(c.m1())
    print(c.__str__())

if __name__ == "__main__":
    main()
