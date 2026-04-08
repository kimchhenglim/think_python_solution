import math

"""
Exercise 6.12.2
"""
def hypotenuse(a: float, b: float) -> float:
    c: float = math.sqrt(a ** 2 + b ** 2)
    return c

"""
Exercise 6.12.3
"""
def is_between(x, y, z) -> float:
    if x < y < z:
        return True

    return False

"""
Exercise 6.12.4
"""
def ackermann(m, n) -> float:
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and m > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
    
    return 0

"""
Exercise 6.12.5
"""
def gcd(a, b) -> float:
    remainder = a % b
    if remainder > 0:
        return gcd(b, remainder)
    else:
        return b

def main():
    """
    Exercise 6.12.2
    """
    print(f"Hypotenuse of a = 10, b = 15 so c = {hypotenuse(10, 15):.2f}")

    """
    Exercise 6.12.3
    """
    x = 15
    y = 11
    z = 10
    print("Between (", x, ",", y, ",", z, "):", is_between(15, 11, 10))

    """
    Exercise 6.12.4
    """
    m = 1
    n = 2
    print("Ackerman (", m, ",", n, "):", ackermann(1, 2)) # m = 5 and n = 5 lead to recursive too depth

    """
    Exrcise 6.12.5
    """
    a = 48
    b = 18
    print("GCD (", a, ",", b, "):", gcd(48, 18))


if __name__ == "__main__":
    main()