"""
Exercise 3.11.2
"""
def print_right(txt: str):
    txt_length = len(txt)
    starting_col_index = 40 - txt_length
    print(" " * starting_col_index, txt)

"""
Exercise 3.11.3
"""
def triangle(txt: str, num: int):
    for i in range(num):
        print(txt * (i + 1))


"""
Exercise 3.11.4
"""
def rectangle(txt: str, w: int, h: int):
    for i in range(h):
        print(txt * 5)

"""
Exercise 3.11.5
"""
def bottle_verse(num: int):
    print(num, "bottles of beer on the wall")
    print(num, "bottles of beer")
    print("Take one down, pass it around")
    print(num - 1, "bottles of beer on the wall")


def main():
    """
    Exercise 3.11.2
    """
    print_right("Monty")
    print_right("Python's")
    print_right("Flying Circus")
    print()

    """
    Exercise 3.11.3
    """
    triangle("L", 5)
    print()

    """
    Exercise 3.11.4
    """
    rectangle("H", 5, 4)
    print()

    """
    Exercise 3.11.5
    """
    for n in range(99, 0, -1):
        bottle_verse(n)
        print()

if __name__ == "__main__":
    main()