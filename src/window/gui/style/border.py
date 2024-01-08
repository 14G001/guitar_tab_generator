from window.gui.style.style import setElementProperty


CSS_BORDER_PROPERTY_NAME = "border"


def removeElementBorder(element):
    setElementProperty(element, CSS_BORDER_PROPERTY_NAME, "none")

def setElementBorder(element, sizePX, color):
    setElementProperty(element, CSS_BORDER_PROPERTY_NAME, str(sizePX) + "px solid rgb" + str(color))

