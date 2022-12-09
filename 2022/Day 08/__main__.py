def countPerimiter(data):
    rowCount = 0
    treeCount = 0
    for line in data:
        treeList = list(line.replace('\n', ''))

        if(rowCount == 0):
            for tree in treeList:
                treeCount += 1
        elif(rowCount == (rowTotal - 1)):
            for tree in treeList:
                treeCount += 1
        else:
            rowLength = len(treeList)
            treeNumber = 0
            for tree in treeList:
                if(treeNumber == 0):
                    treeCount += 1
                elif(treeNumber == (rowLength - 1)):
                    treeCount += 1
                treeNumber += 1

        rowCount += 1

    return treeCount

def evaluateAbove(tree, row, column, data):
    counter = row
    visible = 0 
    check = 0
    while counter > 0:
        dataRow = (counter - 1) if counter != 0 else 0
        if(int(tree) < int(data[dataRow][column])):
            visible = 0
        elif(int(tree) == int(data[dataRow][column])):
            visible = 0
        elif(visible == 0 and check > 0):
            visible = 0
        else:
            visible = 1
            
        check += 1
        counter -= 1

    return visible

def evaluateBelow(tree, row, column, data):
    counter = row
    visible = 0 
    check = 0
    while counter < (len(data[row]) - 1):
        dataRow = (counter + 1)
        if(int(tree) < int(data[dataRow][column])):
            visible = 0
        elif(int(tree) == int(data[dataRow][column])):
            visible = 0
        elif(visible == 0 and check > 0):
            visible = 0
        else:
            visible = 1
        
        check += 1
        counter += 1

    return visible

def evaluateLeft(tree, row, column, data):
    counter = column
    visible = 0 
    check = 0
    while counter > 0:
        dataColumn = (counter - 1) if counter != 0 else 0
        if(int(tree) < int(data[row][dataColumn])):
            visible = 0
        elif(int(tree) == int(data[row][dataColumn])):
            visible = 0
        elif(visible == 0 and check > 0):
            visible = 0
        else:
            visible = 1
        
        check += 1
        counter -= 1

    return visible

def evaluateRight(tree, row, column, data):
    counter = column
    visible = 0 
    check = 0
    while counter < (len(data[row]) - 1):
        dataColumn = (counter + 1)
        if(int(tree) < int(data[row][dataColumn])):
            visible = 0
        elif(int(tree) == int(data[row][dataColumn])):
            visible = 0
        elif(visible == 0 and check > 0):
            visible = 0
        else:
            visible = 1
        
        check += 1
        counter += 1

    return visible

try:
    test_file = open("./data.txt", "r")
    lines = test_file.readlines()

    rowTotal = 0
    treesVisible = 0
    rowNumber = 0
    rows = []

    for line in lines:
        trees = list(line.replace('\n', ''))
        print(trees)
        rows.append(trees)
        rowTotal += 1

    perimiter = countPerimiter(lines)

    treesVisible += perimiter

    for row in rows:
        columnNumber = 0

        for tree in row:
            isVisible = 0

            if(rowNumber == 0):
                columnNumber += 1
                continue
            elif(rowNumber == (len(rows) - 1)):
                columnNumber += 1
                continue
            else:
                if(columnNumber == 0):
                    columnNumber += 1
                    continue
                elif(columnNumber == (len(row) - 1)):
                    columnNumber += 1
                    continue
                else:

                    isVisible = (evaluateAbove(tree, rowNumber, columnNumber, rows) + evaluateBelow(tree, rowNumber, columnNumber, rows) + evaluateLeft(tree, rowNumber, columnNumber, rows) + evaluateRight(tree, rowNumber, columnNumber, rows))
                    
                    if(isVisible > 0):
                        treesVisible += 1 

                columnNumber += 1

        rowNumber += 1
    print(treesVisible)

except FileNotFoundError:
    print("file not found")