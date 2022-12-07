class File:
    def __init__(self, details):
        self.name = details[1]
        self.size = details[0]

class Directory:
    def __init__(self, name, parent):
        self.files = []
        self.children = []
        self.name = name
        self.parent = parent

    def create_child(self, name):
        childDirectory = Directory(name, self)
        self.children.append(childDirectory)

        return childDirectory

    def create_file(self, details):
        file = File(details)
        self.files.append(file)

    def getSize(self):
        directorySize = 0

        for file in self.files:
            directorySize += int(file.size)

        for child in self.children:
            directorySize += child.getSize()

        return directorySize
try:
    test_file = open("./challenge.txt", "r")
    lines = test_file.readlines()

    totalSize = 0
    directories = []
    directorySizes = []
    root = Directory('/', '')
    directories.append(root)
    currentDirectory = root

    for line in lines:
        command = line.split()

        if(command[0] == '$'):
            if(command[1] == 'cd'):                
                if(command[2] == '..'):
                    currentDirectory = currentDirectory.parent    
                elif(command[2] == '/'):
                    currentDirectory = root
                else:
                    currentDirectory = currentDirectory.create_child(command[2])
                    directories.append(currentDirectory)
            elif(command[1] == 'ls'):
                continue
        elif(command[0] == 'dir'):
            currentDirectory.create_child(command[1])
        else:
            currentDirectory.create_file(command)

    for directory in directories:
        size = directory.getSize()
        directorySizes.append(size)

        if(size < 100000):
            totalSize += size

    print('Total Size: ' + str(totalSize))

    directorySizes.sort()
    neededSpace = 30000000
    availableSpace = 70000000 - root.getSize()
    deleteSpace = neededSpace - availableSpace
    selectedSizes = []

    for size in directorySizes:
        if(size > deleteSpace):
            selectedSizes.append(size)
    
    selectedSizes.sort
    print('Delete Size: ' + str(selectedSizes[0]))


except FileNotFoundError:
    print("file not found")