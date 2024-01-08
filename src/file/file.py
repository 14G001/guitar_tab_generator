from subprocess import run


def createFolder(folderPath, cwd = None):
    if cwd == None:
        return run(["mkdir", folderPath], shell = True, capture_output = True)
    return run(["mkdir", folderPath], cwd = cwd, shell = True, capture_output = True)

def getFile(dirCommandLine):
    if dirCommandLine[0].isdecimal() and dirCommandLine[21] != "<":
        return dirCommandLine[36:].replace("\\r", "")
    return None
def getFolder(dirCommandLine):
    if dirCommandLine[0].isdecimal() and dirCommandLine[21] == "<":
        return dirCommandLine[36:].replace("\\r", "")
    return None
def getElementsFromDirectory(directory, fileGetter):
    files = []
    command = run(["dir", ""], cwd = directory, shell = True, capture_output = True)
    for commandLine in str(command.stdout).split("\\n"):
        file = fileGetter(commandLine)
        if file != None:
            files.append(file)
    return files
def getFilesFromDirectory(directory):
    return getElementsFromDirectory(directory, getFile)
def getFoldersFromDirectory(directory):
    return getElementsFromDirectory(directory, getFolder)


def fileExist(filePath):
    pathDirs = filePath.split("\\")
    fileName = pathDirs[len(pathDirs) - 1]
    filePath = filePath.replace(fileName, "")
    pathFiles = getFilesFromDirectory(filePath)
    for file in pathFiles:
        if file == fileName:
            return True
    return False