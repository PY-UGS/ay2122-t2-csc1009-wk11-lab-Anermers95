from re import S
from sympy import public


class Calculator:
    
    def Adder(self):
        x = int(input("Input x: "))
        y = int(input("Input y: "))
        total = x + y
        return total
    
    def Subtractor(self):
        x = int(input("Input x: "))
        y = int(input("Input y: "))
        total = x - y
        return total
    
    def Multiplier(self):
        x = int(input("Input x: "))
        y = int(input("Input y: "))
        total = x * y
        return total
    
    def Divider(self):
        x = int(input("Input x: "))
        y = int(input("Input y: "))
        total = x / y
        return total
    
    def Clear():
        return 0

class ClockTime:
    hours = 0
    min = 0
    sec = 0
    
    def setHours(self):
        self.hours = input("Enter hours")
        
        
    def setMin(self):
         self.min = input("Enter mins")
        
    def setSec(self,input):
         self.sec = input("Enter sec")
    
    def setime(self):
        self.hours = input("Enter hours: ")
        self.min = input("Enter mins: ")
        self.sec = input("Enter sec: ")
        
    def showTime(self):
        print(self.hours + ":" + self.min + ":" + self.sec)
        
        
def main():
    c = Calculator();
    ct = ClockTime();
    
    print("Addition:")
    print(c.Adder());
    print("subtraction:")
    print(c.Subtractor());
    print("multiplication:")
    print(c.Multiplier());
    print("division:")
    print(c.Divider());
    print(c.Clear());
    
    ct.setime();
    ct.showTime();
    
    

if __name__ == '__main__':
    main()
    