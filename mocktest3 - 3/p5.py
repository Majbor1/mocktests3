import math

class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def m1(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        elif self.x == 0 or self.y == 0:
            return 0
        
    def m2(self, a, b):
        if a > 0 and b > 0 and self.m1() == 1:
            return True
        elif a < 0 and b > 0 and self.m1() == 2:
            return True
        elif a < 0 and b < 0 and self.m1() == 3:
            return True
        elif a > 0 and b < 0 and self.m1() == 4:
            return True
        elif (a == 0 or b == 0) and self.m1() == 0:
            return True
        else:
            return False
        
    def m3(self, a, b):
        distance = math.sqrt((self.x-a)**2 + (self.y-b)**2)

        if distance > 5:
            return True
        else: 
            return False
        
def main():
    p = C(2, 3)  
    print(p.m1())
    print(p.m2(7, 4)) 
    print(p.m3(8, 5)) 


if __name__ == "__main__":
    main()