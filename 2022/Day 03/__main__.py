def letterValue(letter):
    value = 0
    
    if(ord(letter) >= ord('a')):
        value = (ord(letter) - ord('a')) + 1
    else:
        value = (ord(letter) - ord('A')) + 27
    
    return value

try:
    test_file = open("./challenge.txt", "r")
    lines = test_file.readlines()
    itemValue = 0
    elves = []

    for line in lines:
        text = line.replace('\n', '')
        half = (text.__len__()/2)
        elf = set(text)
        elves.append(elf)

        bag1 = set(text[:int(half)])
        bag2 = set(text[int(half):])

        sameItem = bag1.intersection(bag2)

        for letter in sameItem:
            value = letterValue(letter)

        itemValue += value
    print("Items Value: " + str(itemValue))

    groups = (elves.__len__() / 3)
    groupCount = 0
    groupValue = 0
    elfGroup = 0
    
    while groupCount < groups:
        elfBag1 = elves[elfGroup]
        elfBag2 = elves[elfGroup + 1]
        elfBag3 = elves[elfGroup + 2]

        elfGroup += 3

        groupItem = elfBag1.intersection(elfBag2, elfBag3)

        for letter in groupItem:
            value = letterValue(letter)

        groupValue += value            
        groupCount += 1

    print("Groups Value: " + str(groupValue))

except FileNotFoundError:
    print("file not found")