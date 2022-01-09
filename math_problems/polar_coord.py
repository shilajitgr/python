"""
Input Format:

A single line containing the complex number z. Note: complex() function can be used in python to convert the
input as a complex number.

Constraints:
Given number is a valid complex number


Output Format

Output two lines:
The first line should contain the value of r, which sqrt(real^2 + imag^2).
The second line should contain the value of phase.
"""

import cmath
import math

cmplx = complex(input())
r = math.sqrt(cmplx.real**2 + cmplx.imag**2)
phase = cmath.phase(cmplx)

print(r)
print(phase)