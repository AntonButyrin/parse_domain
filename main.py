with open('text.txt', 'r') as f:
    lines = f.readlines()

threshold = 15000
fileID = 0
counter = 0
while fileID < len(lines) / float(threshold):
    with open('fileNo' + str(fileID) + '.txt', 'w') as currentFile:
        for currentLine in lines[threshold * fileID:threshold * (fileID + 1)]:
            currentFile.write(currentLine)
        fileID += 1
        counter += 1
        print(counter)
