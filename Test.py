import re

def arithmetic_arranger(problems, show_answer=False):
    row1, row2, row3, row4= '', '', '', ''

    for problem in problems:
        num1, num2 = re.findall('\d+', problem)
        operator = re.findall('[+-]', problem)[0]

        width = max(len(num1), len(num2)) + 2

        row1 += (num1.rjust(width))
        row2 += (operator + num2.rjust(width - 1))
        row3 += "-" * width
        row4 += str(eval(problem)).rjust(width)

        row1 += '    '
        row2 += '    '
        row3 += '    '
        row4 += '    '

    if show_answer:
        return '\n'.join([row1, row2, row3, row4])
    else:
        return '\n'.join([row1, row2, row3])

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
