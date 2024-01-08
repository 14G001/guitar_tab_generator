from PyQt5.QtWidgets import QFileDialog

class FileRequest():
    def __init__(self,
                 text = "Drop file here",
                 requestFileMessage = "Select file",
                 fileTypes = [["All files", "*"]],
                 directory = "/"):
        self.text = text
        self.requestFileMessage = requestFileMessage
        self.fileTypes = fileTypes
        self.directory = directory

def requestFile(fileRequestData = FileRequest):
    admittedFiles = fileRequestData.fileTypes[0][0] + " (" + fileRequestData.fileTypes[0][1] + ")"
    for fileTypeCounter in range(1, len(fileRequestData.fileTypes)):
        admittedFiles += ";;" + fileRequestData.fileTypes[fileTypeCounter][0] + " (" + fileRequestData.fileTypes[fileTypeCounter][1] + ")"
    selectedFile = QFileDialog().getOpenFileName(
        caption = fileRequestData.requestFileMessage,
        directory = fileRequestData.directory,
        filter = admittedFiles)
    if selectedFile[0] == "":
        return None
    return selectedFile[0]