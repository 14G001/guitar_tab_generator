from window.gui.style.style import getElementProperty, setElementProperty
from utils.color import strColorToRGB


CSS_COLOR_PROPERTY_NAME = "background-color"
CSS_RGB_COLOR_PREFIX =    "rgb"


def getElementColor(element) -> tuple:
    color = getElementProperty(element, CSS_COLOR_PROPERTY_NAME)
    if color == None:
        return color
    return strColorToRGB(color.replace(CSS_RGB_COLOR_PREFIX, ""))
    
def setElementColor(element, value = tuple):
    setElementProperty(element, CSS_COLOR_PROPERTY_NAME, CSS_RGB_COLOR_PREFIX + str(value))