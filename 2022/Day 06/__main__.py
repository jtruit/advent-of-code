def findMarker(file, x):
    counter = 0

    for counter in range(0, (len(file) - x )):

        charSet = set(file[counter:(counter + x)])

        if(len(charSet) == x):

            return (counter + x)
try:
    test_file = open("./challenge.txt", "r")
    file = test_file.read()

    print("Start of Packet Marker found after " + str(findMarker(file, 4)) + " characters")   
    print("Start of Message Marker found after " + str(findMarker(file, 14)) + " characters")   

except FileNotFoundError:
    print("file not found")