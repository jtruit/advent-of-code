def rangeValue(text, upper):

    if(upper == True):
        elfUpperRange = text.split("-")[1]
        value = (int(elfUpperRange) + 1)
    else:
        elfLowerRange = text.split("-")[0]
        value = int(elfLowerRange)
    return value

try:
    test_file = open("./challenge.txt", "r")
    lines = test_file.readlines()

    count = 0
    wholeRange = 0
    overlapRange = 0    

    for line in lines:
        elf = line.split(",")[0]
        me = line.split(",")[1]

        x = range(rangeValue(elf, False), rangeValue(elf, True))
        y = range(rangeValue(me, False), rangeValue(me, True))
        xs = set(x)
        ys = set(y)
        overlap = xs.intersection(ys) 

        if(overlap == xs):
            wholeRange += 1
            overlapRange += 1
        elif(overlap == ys):
            wholeRange += 1
            overlapRange += 1
        elif(len(overlap)):
            overlapRange += 1

        count += 1
    print("Contained Ranges: " + str(wholeRange))
    print("Overlapped Ranges: " + str(overlapRange))

except FileNotFoundError:
    print("file not found")