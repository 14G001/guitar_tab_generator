from window.gui.element.input.file.fileRequest import FileRequest
from window.window.element.input.file.fileInput import FileInput

class TabsFileInput(FileInput):
    def __init__(self, configName, elements):
        super().__init__(configName, elements,
            FileRequest(
                text = "Drop tabs file here",
                requestFileMessage = "Select tabs file",
                fileTypes = (("All files", "*"), ("Tab", "*.tab"), ("Txt", "*.txt"))
                # TODO: buscar directorio principal
            ))