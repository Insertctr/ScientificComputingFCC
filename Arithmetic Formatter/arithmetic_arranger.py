def arithmetic_arranger(problems, bi= False):
    #function that receives a list of strings that are arithmetic problems 
    arranged_problems = ""
    operator = ""
    firstNumber = ""
    secondNumber = ""
    lines = ""
    result = ""

    #Situations that will return an error:If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
    if len(problems) > 5:
        return "Too many problems."



    
    #Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
    #Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits
    if len(firstNumber) > 4 and len(secondNumber) > 4:
        return "Error: Numbers cannot be more than four digits."
    else:
          return "Error: Numbers must only contain digits."

    #The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
    if operator == '*' or operator == '/':
        return "Error: Operator must be '+' or '-'."



    #There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).







    #If the user supplied the correct format of problems, the conversion you return will follow these rules:





    #There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).






    #Numbers should be right-aligned.





    #There should be four spaces between each problem.





    #There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
    




    return arranged_problems


def arithmetic_arranger(problems, val=False):
    arranged_problems = ''
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    # list of all operations in str format
    operations = list(map(lambda x: x.split()[1], problems))
    if set(operations) != {'+', '-'} and len(set(operations)) != 2:
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems

    numbers = []  # list of all operands in str format
    for i in problems:
        p = i.split()
        numbers.extend([p[0], p[2]])

    if not all(map(lambda x: x.isdigit(), numbers)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems

    if not all(map(lambda x: len(x) < 5, numbers)):
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems

    top_row = ''
    dashes = ''
    values = list(map(lambda x: eval(x), problems))
    solutions = ''
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i+1])) + 2
        top_row += numbers[i].rjust(space_width)
        dashes += '-' * space_width
        solutions += str(values[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    bottom_row = ''
    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        bottom_row += operations[i // 2]
        bottom_row += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            bottom_row += ' ' * 4

    if val:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))
    return arranged_problems

