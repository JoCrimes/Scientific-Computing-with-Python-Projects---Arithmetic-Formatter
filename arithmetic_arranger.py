def arithmetic_arranger(problems,solution=False):
    # Returns the problems arranged vertically as described in the readme.txt
    import string
    arranged_problems = ''
    top = []
    bottom = []
    operand = []
    line = []
    answers = []
    topStr = ''
    bottomStr = ''
    operandStr = ''
    answersStr = ''
    lineStr = ''
    pad = '    '    # 4 spaces required between problems
    # Check the number of problems. Max of 5.
    numProblems = (len(problems))
    if numProblems > 5:
        #raise Exception
        return 'Error: Too many problems.'
    # Split the problems into the lists: top, operand and bottom
    for p in problems:
        #answers =
        #print(str(p))
        temp = p.split(' ')
        #print(temp[0])
        top.append(temp[0])
        operand.append(temp[1])
        bottom.append(temp[2])
    #print(top)
    #print(operand)
    #print(bottom)
    # Calculate the answers to the problems and store in answers
    for i, sign in enumerate(operand):
        try:
            A = int(top[i])
            B = int(bottom[i])
        except ValueError:
            return "Error: Numbers must only contain digits."
        if sign == '+':
            C = A+B
            answers.append(C)
        elif sign == '-':
            C = A-B
            answers.append(C)
        else:
            #answers.append('Err')
            return "Error: Operator must be '+' or '-'."
    
    # Find out if the top or bottom has more digits in order to decide how to pad the top and bottom lines
    for i in range(numProblems):
        if (len(top[i]) > 4) or (len(bottom[i]) > 4):
            return "Error: Numbers cannot be more than four digits."
        elif (len(top[i]) > len(bottom[i])):
            #print('Top is bigger')
            #diff = len(top[i])
            #print(str(diff))
            bottom[i] = bottom[i].rjust(len(top[i]))
            bottom[i] = operand[i]+' '+bottom[i]
            #bottom[i] = bottom[i].rjust(len(top[i]))
            top[i] = top[i].rjust(len(bottom[i]))
            answers[i] = str(answers[i])
            answers[i] = answers[i].rjust(len(bottom[i]))
        elif (len(top[i]) <= len(bottom[i])):
            #print('Bottom is bigger')
            bottom[i] = operand[i]+' '+bottom[i]
            top[i] = top[i].rjust(len(bottom[i]))
            #top[i] = top[i].rjust(len(bottom[i]))
            answers[i] = str(answers[i])
            answers[i] = answers[i].rjust(len(bottom[i]))
        # Make the lines for under the second row
        lines = ''
        #print('Test: ' +str(range(len(bottom[i]))))
        for j in range(len(bottom[i])):
            lines += '-'
        #print(lines)
        #print(str(i))
        line.append(lines)

    # Arrange the problems
    for i in range(numProblems):
        topStr += top[i]+pad
        bottomStr += bottom[i]+pad
        lineStr += line[i]+pad
        answersStr += str(answers[i])+pad
    # cut pad off the strings!
    topStr = topStr[0:len(topStr)-len(pad)]
    bottomStr = bottomStr[0:len(bottomStr)-len(pad)]
    lineStr = lineStr[0:len(lineStr)-len(pad)]
    answersStr = answersStr[0:len(answersStr)-len(pad)]
    #print('Solution: '+str(solution))
    #print('Top: '+str(len(topStr)))
    #print('Bottom: '+str(len(bottomStr)))
    #print('Lines: '+str(len(lineStr)))
    #print('Answer: '+str(len(answersStr)))
    if (solution is True):    
        arranged_problems = topStr+'\n'+bottomStr+'\n'+lineStr+'\n'+answersStr
    else:
        arranged_problems = topStr+'\n'+bottomStr+'\n'+lineStr
    return arranged_problems