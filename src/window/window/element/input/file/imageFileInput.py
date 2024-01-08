from window.gui.element.input.file.fileRequest import FileRequest
from window.window.element.input.file.fileInputCheckBox import FileInputCheckBox

class ImageFileInput(FileInputCheckBox):
    def __init__(self, configName, elements, elementsToCheck):
        super().__init__(configName, elements, elementsToCheck,
            FileRequest(
                text = "Drop image file here",
                requestFileMessage = "Select image file",
                fileTypes = (("All files", "*"), ("PNG", "*.png"), ("JPG", "*.jpg"))
                # TODO: buscar directorio principal
            ))