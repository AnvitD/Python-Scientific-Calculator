import math
import sys

def main():

    total = 0.0
    result = 0.0
    count = 0.0
    run = True


    while run:

        print(f"Current Result: {round(result,2)} \n")
        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average\n")

        while run:

            choice = int(input("Enter Menu Selection: "))

            if choice > 0 and choice <= 6:
                Foperand = float(input("Enter first operand: "))
                Soperand = float(input("Enter second operand: "))

                if choice == 1:
                    result = Foperand + Soperand
                    total = total + result
                    count = count + 1
                elif choice == 2:
                    result = Foperand - Soperand
                    total = total + result
                    count = count + 1 
                elif choice == 3:
                    result = Foperand * Soperand
                    total = total + result
                    count = count + 1 
                elif choice == 4: 
                    result = Foperand/Soperand
                    total = total + result
                    count = count + 1 
                elif choice == 5: 
                    result = Foperand**Soperand
                    total = total + result
                    count = count + 1
                elif choice == 6: 
                    result = math.log(Foperand, Soperand)
                    total = total + result
                    count = count + 1
                break
            
            elif choice == 0:

                print("Thanks for using this calculator. Goodbye!")
                sys.exit()
                
                

            elif choice == 7: 

                if count >= 1: 
                    out = total/count
                    print(f"Sum of calculations: {round(total, 2)}")
                    print(f"Number of calculations: {round(count, 2)}")
                    print(f"Average of calculations: {round(out, 2)}")
                else: 
                    print("Error: No calculations yet to average!")
                    pass
            else: 
                print("Error: Invalid selection!")
    


main()


              

             

 





