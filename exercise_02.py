"""
Exercise 2.11.3, Part 1
"""
import math

radius = 5      # radius in centimeters
volume = 4/3 * math.pi * math.pow(radius, 3)        # volume in cubic centimeters
print(f"Radius is {radius:.2f} centimeters and Volume is {volume:.2f} cubic centimeters")

"""
Exercise 2.11.3, Part 2
"""
import math

x = 42
trigonometry = math.cos(x) ** 2 + math.sin(x) ** 2

print(f"Trigonometry is {math.isclose(trigonometry, 1)} because the answer is {trigonometry}")

"""
Exercise 2.11.3, Part 3
"""
import math

print(math.e ** 2)
print(math.pow(math.e, 2))
print(math.exp(2))
