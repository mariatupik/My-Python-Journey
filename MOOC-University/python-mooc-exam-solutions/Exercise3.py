from fractions import Fraction

def convert_to_fraction(fraction: str):
    fraction_parts = fraction.split("/")
    numerator = int(fraction_parts[0])
    denominator = int(fraction_parts[1])
    return Fraction(numerator, denominator)

def fraction_calculator(calculation: str):
    parts = calculation.split()
    if len(parts) == 1:
        return str(convert_to_fraction(parts[0]))
    
    f1 = convert_to_fraction(parts[0])
    f2 = convert_to_fraction(parts[2])
    op = parts[1]

    if op == "+": return str(f1 + f2)
    elif op == "-": return str(f1 - f2)
    elif op == "*": return str(f1 * f2)

if __name__ == "__main__":
    calc = "1/2 + 3/4"
    print(f"Result of {calc}: {fraction_calculator(calc)}")