from window.window.element.input.file.fileInput import FileInput

class FileInputCheckBox(FileInput):
    def __init__(self, configName, elements, elementsToCheck, fileRequestData):
        super().__init__(configName, elements, fileRequestData)
        self.elementsToCheck = elementsToCheck
    def onValidFile(self, filePath):
        super().onValidFile(filePath)
        if self.elementsToCheck[0].get() == False:
            for element in self.elementsToCheck:
                element.click()