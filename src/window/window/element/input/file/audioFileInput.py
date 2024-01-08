from window.gui.element.input.file.fileRequest import FileRequest
from window.window.element.input.file.fileInputCheckBox import FileInputCheckBox

class AudioFileInput(FileInputCheckBox):
    def __init__(self, configName, elements, elementsToCheck):
        super().__init__(configName, elements, elementsToCheck,
            FileRequest(
                text = "Drop audio file here",
                requestFileMessage = "Select audio file",
                fileTypes = (("All files", "*"), ("WAV", "*.wav"), ("MP3", "*.mp3"))
                # TODO: buscar directorio principal
            ))
        