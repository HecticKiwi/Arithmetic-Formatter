import re

def arithmetic_arranger(problems, show_answer=False):
    row1, row2, row3, row4= '', '', '', ''

    for problem in problems:
        num1, num2 = re.findall('\d+', problem)
        try:   
            operator = re.findall('[+-]', problem)[0]
        except:
            return "Error: Operator must be '+' or '-'."

        if len(problems) > 5:
            return "Error: Too many problems."
        elif not row1.isnumeric() and row2.isnumeric():
            return "Error: Numbers must only contain digits."
        elif len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

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
        arranged_problems = '\n'.join([row1, row2, row3, row4])
    else:
        arranged_problems = '\n'.join([row1, row2, row3])
    
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
