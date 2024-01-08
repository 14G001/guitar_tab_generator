from PyQt5.QtWidgets import QColorDialog


def requestColor() -> tuple:
    selectedColor = QColorDialog.getColor() # TODO: add title param (translated)
    if not selectedColor.isValid():
        return None
    return (selectedColor.red(), selectedColor.green(), selectedColor.blue())
