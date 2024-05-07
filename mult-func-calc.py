import sympy as sp

def solve_proportion():
    a = float(input("Enter the first term of the proportion (a): "))
    b = float(input("Enter the second term of the proportion (b): "))
    c = float(input("Enter the third term of the proportion (c): "))
    x = sp.symbols('x')
    proportion = sp.Eq(a/b, c/x)
    solution = sp.solve(proportion, x)
    print(f"The value of x is: {solution[0]}")

def solve_for_x_in_equation():
    lhs_input = input("Enter the left-hand side of the equation (e.g., 2*x + 3): ")
    rhs_input = input("Enter the right-hand side of the equation (e.g., 15): ")
    x = sp.symbols('x')
    lhs = sp.sympify(lhs_input)
    rhs = sp.sympify(rhs_input)
    equation = sp.Eq(lhs, rhs)
    solution = sp.solve(equation, x)
    print(f"The solution is x = {solution}")
solve_for_x_in_equation()


def factor_square_roots():
    number = int(input("Enter the number to factor the square root of: "))
    result = sp.sqrt(number)
    print(f"The factored square root is: {result}")

def decimal_to_fraction_percent():
    decimal = float(input("Enter a decimal number: "))
    fraction = sp.Rational(decimal).limit_denominator()
    percent = decimal * 100
    print(f"Fraction: {fraction}")
    print(f"Percent: {percent}%")

def fraction_to_decimal_percent():
    numerator = int(input("Enter the numerator of the fraction: "))
    denominator = int(input("Enter the denominator of the fraction: "))
    decimal = numerator / denominator
    percent = decimal * 100
    print(f"Decimal: {decimal}")
    print(f"Percent: {percent}%")

def percent_to_decimal_fraction():
    percent = float(input("Enter a percentage: "))
    decimal = percent / 100
    fraction = sp.Rational(decimal).limit_denominator()
    print(f"Decimal: {decimal}")
    print(f"Fraction: {fraction}")

def main():
    while True:
        print("\nMulti-Function Calculator")
        print("1. Solve Proportions")
        print("2. Solve for x in Equations")
        print("3. Factor Square Roots")
        print("4. Convert Decimals to Fractions and Percents")
        print("5. Convert Fractions to Decimals and Percents")
        print("6. Convert Percents to Decimals and Fractions")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '0':
            break
        elif choice == '1':
            solve_proportion()
        elif choice == '2':
            solve_for_x_in_equation()
        elif choice == '3':
            factor_square_roots()
        elif choice == '4':
            decimal_to_fraction_percent()
        elif choice == '5':
            fraction_to_decimal_percent()
        elif choice == '6':
            percent_to_decimal_fraction()
        else:
            print("Invalid choice. Please enter a number from 0 to 6.")

if __name__ == "__main__":
    main()