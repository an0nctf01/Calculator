import math
import time

print("Welcome to PyCalculator Made By An0nCTF")

run = input("Do you want to continue? (y/n): ")
if run.lower() != 'y':
    print("Exitting...")
    time.sleep(2)
    exit()  
else:
    run = True

# Calculator Class - Does basic arithmetic and solves equations first and second degree

class calc():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def eq1(self):
        a = float(input("Enter value for a: "))
        b = float(input("Enter value for b: "))
        if a == 0:
            print("No solution, 'a' cannot be zero.")
        else:
            x = -b / a
            print(f"The solution is x = {x}")
    def eq2(self):
        a = float(input("Enter value for a: "))
        b = float(input("Enter value for b: "))
        c = float(input("Enter value for c: "))
        D = b**2 - 4*a*c
        if D < 0:
            print("No Real Solutions")
        elif D == 0:
            x = -b / (2*a)
            print(f"One Real Solution: x = {x}")
        else:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            print(f"Two Real Solutions: x1 = {x1}, x2 = {x2}")
    def perform_calculation():

        if user_choice == 1:
            calc_instance = calc(0, 0)
            calc_instance.eq1()

        elif user_choice == 2:
            calc_instance = calc(0, 0)
            calc_instance.eq2()

        elif user_choice ==3:  
            a = float(input("Enter value for a: "))
            b = float(input("Enter value for b: "))
            operation = input("Select Operation (+ ,-,/,*,**,%,): ")
            if operation == "+":
                result = a + b
                print(f"The result of {a} + {b} = {result}")
            elif operation == "-":
                result = a - b
                print(f"The result of {a} - {b} = {result}")
            elif operation == "*":
                result = a * b
                print(f"The result of {a} * {b} = {result}")    
            elif operation == "/":
                if b != 0:
                    result = a / b
                    print(f"The result of {a} / {b} = {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            elif operation == "**":
                result = a ** b
                print(f"The result of {a} ** {b} = {result}")
            elif operation == "%":
                result = a % b
                print(f"The result of {a} % {b} = {result}")    

            else:
                print("Invalid Selection")
        else:
            print("Invalid Value - Exitting")
            time.sleep(2)
            exit()


print("1. Equation (ax+b=0) \n 2. Second Degree Equation (ax^2+bx+c=0) \n 3. Simple (a+b , a-b )")
user_choice = int(input("Select Option: "))
calc.perform_calculation()

#Made by An0nCTF 
#Feel Free to Contact me on Discord anonctf or GitHub An0nCTF

cont = input("Do you want to perform another calculation? (y/n): ")
if cont.lower() == 'n':
        print("Exitting...")
        time.sleep(2)
else:
    calc.perform_calculation()

