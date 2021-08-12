import re

def arithmetic_arranger(problems):
    row1, row2 = '', ''

    for problem in problems:
        num1, num2 = re.findall('\d+', problem)
        row1 += (f'{num1:>5}')
        operator = re.findall('[+-]', problem)[0]
        row2 += (f'{operator} + " " + {num2:4}')

        return row1, row2

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
