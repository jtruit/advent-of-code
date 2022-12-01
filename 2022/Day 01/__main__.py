try:
    test_file = open("./challenge.txt", "r")
    lines = test_file.readlines()

    elfList = []
    count = 1
    calories = 0

    for line in lines:
        if line in ['\n', '\r\n']:
            elfList.append(calories)
            count += 1
            calories = 0
        else:
            elfCals = int(line)
            calories += elfCals
    else:
        elfList.append(calories)

    print("Max Calories: " + str(max(elfList)))

    sortedElfList = sorted(elfList, key=int, reverse=True)

    top3 = 0
    loop = 0

    while loop < 3:
        top3 += sortedElfList[loop]
        loop += 1
    
    print("Top 3 Calories: " + str(top3))

except FileNotFoundError:
    print("file not found")