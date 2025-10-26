import math
import re
import sys
if sys.argv[1:] == []:
    print("Enter a quadratic equation that equals 0 (syntax is as follows: ax^2+bx+c):")
    quad_eq = input()
else:
    quad_eq = sys.argv[1:][0] 

quad_eq = re.split(r'(\W)', quad_eq)
a_neg = (quad_eq[1] == '-')

if a_neg == True:
    a = (quad_eq[1] + quad_eq[2].replace('x',''))
    b = ((quad_eq[5] + quad_eq[6].replace('x','').replace('+','')))
    c = int((quad_eq[7] + quad_eq[8]).replace('+',''))
else:
    a = (quad_eq[0].replace('x',''))
    b = ((quad_eq[3] + quad_eq[4].replace('x','')).replace('+',''))
    c = int((quad_eq[5] + quad_eq[6]).replace('+',''))

if a == "-":
    a = -1
elif a == "":
    a = 1
else: 
    a = int(a)

if b == "-":
    b = -1
elif b == "":
    b = 1
else:
    b = int(b)

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("Delta is negative, no solutions are possible.")
    exit()
elif delta == 0:
    solution = (-b) / (2 * a)
    print(solution)
else:
    solution_1 = ((-b) + math.sqrt(delta)) / (2 * a)
    solution_2 = ((-b) - math.sqrt(delta)) / (2 * a)
    print(solution_1, "or", solution_2)
