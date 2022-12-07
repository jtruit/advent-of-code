try:
    test_file = open("./challenge.txt", "r")
    lines = test_file.readlines()

    #Test
    # stack1part1 = ['N', 'Z']
    # stack2part1 = ['D', 'C', 'M']
    # stack3part1 = ['P']

    # stack1part2 = ['N', 'Z']
    # stack2part2 = ['D', 'C', 'M']
    # stack3part2 = ['P']

    stack1part1 = ['W','T','H','P','J','C','F']
    stack2part1 = ['H','B','J','Z','F','V','R','G']
    stack3part1 = ['R','T','P','H']
    stack4part1 = ['T','H','P','N','S','Z']
    stack5part1 = ['D','C','J','H','Z','F','V','N']
    stack6part1 = ['Z','D','W','F','G','M','P']
    stack7part1 = ['P','D','J','S','W','Z','V','M']
    stack8part1 = ['S','D','N']
    stack9part1 = ['M','F','S','Z','D']

    stack1part2 = ['W','T','H','P','J','C','F']
    stack2part2 = ['H','B','J','Z','F','V','R','G']
    stack3part2 = ['R','T','P','H']
    stack4part2 = ['T','H','P','N','S','Z']
    stack5part2 = ['D','C','J','H','Z','F','V','N']
    stack6part2 = ['Z','D','W','F','G','M','P']
    stack7part2 = ['P','D','J','S','W','Z','V','M']
    stack8part2 = ['S','D','N']
    stack9part2 = ['M','F','S','Z','D']

    for line in lines:
        line = line.replace('move', '')
        line = line.replace('from', '')
        line = line.replace('to', '')

        instructions = line.split()
        moveCount = 0

        while(moveCount < int(instructions[0])):

            match instructions[1]:
                case "1":
                    movingCrate = stack1part1.pop(0)
                case "2":
                    movingCrate = stack2part1.pop(0)
                case "3":
                    movingCrate = stack3part1.pop(0)
                case "4":
                    movingCrate = stack4part1.pop(0)
                case "5":
                    movingCrate = stack5part1.pop(0)
                case "6":
                    movingCrate = stack6part1.pop(0)
                case "7":
                    movingCrate = stack7part1.pop(0)
                case "8":
                    movingCrate = stack8part1.pop(0)
                case "9":
                    movingCrate = stack9part1.pop(0)

            match instructions[2]:
                case "1":
                    stack1part1.insert(0, movingCrate)
                case "2":
                    stack2part1.insert(0, movingCrate)
                case "3":
                    stack3part1.insert(0, movingCrate)
                case "4":
                    stack4part1.insert(0, movingCrate)
                case "5":
                    stack5part1.insert(0, movingCrate)
                case "6":
                    stack6part1.insert(0, movingCrate)
                case "7":
                    stack7part1.insert(0, movingCrate)
                case "8":
                    stack8part1.insert(0, movingCrate)
                case "9":
                    stack9part1.insert(0, movingCrate)

            moveCount += 1  
            
    
    print('Final Stacks Part 1:')
    print(stack1part1)
    print(stack2part1)
    print(stack3part1)
    print(stack4part1)
    print(stack5part1)
    print(stack6part1)
    print(stack7part1)
    print(stack8part1)
    print(stack9part1)

    for line in lines:
        line = line.replace('move', '')
        line = line.replace('from', '')
        line = line.replace('to', '')

        instructions = line.split()
        moveCount = 0

        while(moveCount < int(instructions[0])):

            match instructions[1]:
                case "1":
                    movingCrate = stack1part2.pop(0)
                case "2":
                    movingCrate = stack2part2.pop(0)
                case "3":
                    movingCrate = stack3part2.pop(0)
                case "4":
                    movingCrate = stack4part2.pop(0)
                case "5":
                    movingCrate = stack5part2.pop(0)
                case "6":
                    movingCrate = stack6part2.pop(0)
                case "7":
                    movingCrate = stack7part2.pop(0)
                case "8":
                    movingCrate = stack8part2.pop(0)
                case "9":
                    movingCrate = stack9part2.pop(0)

            match instructions[2]:
                case "1":
                    stack1part2.insert(moveCount, movingCrate)
                case "2":
                    stack2part2.insert(moveCount, movingCrate)
                case "3":
                    stack3part2.insert(moveCount, movingCrate)
                case "4":
                    stack4part2.insert(moveCount, movingCrate)
                case "5":
                    stack5part2.insert(moveCount, movingCrate)
                case "6":
                    stack6part2.insert(moveCount, movingCrate)
                case "7":
                    stack7part2.insert(moveCount, movingCrate)
                case "8":
                    stack8part2.insert(moveCount, movingCrate)
                case "9":
                    stack9part2.insert(moveCount, movingCrate)
            
            moveCount += 1
    
    print('Final Stacks Part 2:')
    print(stack1part2)
    print(stack2part2)
    print(stack3part2)
    print(stack4part2)
    print(stack5part2)
    print(stack6part2)
    print(stack7part2)
    print(stack8part2)
    print(stack9part2)

except FileNotFoundError:
    print("file not found")