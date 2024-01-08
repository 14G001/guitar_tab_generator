from window.gui.element.input.file.fileRequest import requestFile
from window.gui.style.text import getElementText, setElementText
from window.gui.event.dragAndDrop import getEventURLs
from window.gui.element.input.file.fileInput import GUIFileInput
from window.window.element.input.inputElement import InputElement
from window.window.element.input.file.validations.dropValidations import enteredFileMeetRequirements
from utils.classConverter import changeElementsClass


class FileInput(InputElement):
    def __init__(self, configName, elements, fileRequestData):
        self.elements = changeElementsClass(elements, GUIFileInput)
        self.fileRequestData = fileRequestData
        super().__init__(configName, self.elements, None, getElementText, setElementText)
        for element in self.elements:
            element.setEvents(self.onClick, self.dropCondition, self.onDrop)
    def onClick(self):
        selectedFile = requestFile(self.fileRequestData)
        if selectedFile == None:
            return
        self.onValidFile(selectedFile)
    def dropCondition(self, event) -> bool:
        return enteredFileMeetRequirements(event)
    def onDrop(self, event):
        self.onValidFile(getEventURLs(event)[0])
    def onValidFile(self, filePath):
        self.set(filePath)

