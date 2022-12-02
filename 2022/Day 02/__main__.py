try:
    test_file = open("./challenge.txt", "r")
    lines = test_file.readlines()

    totalScore = 0
    totalScore2 = 0

    elf = [x.split()[0] for x in lines]
    me = [x.split()[1] for x in lines]

    elfCount = 0
    meCount = 0
    rounds = me.__len__()

    meThrows = []
        
    for x in me:
        meScore = me[meCount]

        match meScore:
            case "X":
                meThrows.append(1)
            case "Y":
                meThrows.append(2)
            case "Z":
                meThrows.append(3)
            case _ :
                print("Could not throw anything")
        
        meCount += 1

    x = 0
    while x < rounds:
        roundScore = meThrows[x]
        game = elf[x] + me[x]

        match game:
            case "AX":
                roundScore += 3
            case "BX":
                roundScore += 0
            case "CX":
                roundScore += 6
            case "AY":
                roundScore += 6
            case "BY":
                roundScore += 3
            case "CY":
                roundScore += 0
            case "AZ":
                roundScore += 0
            case "BZ":
                roundScore += 6
            case "CZ":
                roundScore += 3

        x += 1
        totalScore += roundScore

    print("Total Score: " + str(totalScore))

    y = 0
    while y < rounds:
        roundScore = 0
        game = elf[y] + me[y]

        match game:
            case "AX":
                roundScore += 3
            case "BX":
                roundScore += 1
            case "CX":
                roundScore += 2
            case "AY":
                roundScore += 4
            case "BY":
                roundScore += 5
            case "CY":
                roundScore += 6
            case "AZ":
                roundScore += 8
            case "BZ":
                roundScore += 9
            case "CZ":
                roundScore += 7
        y += 1
        totalScore2 += roundScore

    print("Actual Score: " + str(totalScore2))

except FileNotFoundError:
    print("file not found")