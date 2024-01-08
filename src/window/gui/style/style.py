def getElementStyle(element):
    return element.styleSheet()
def setElementStyle(element, style):
    element.setStyleSheet(style)
def getElementProperty(element, propertyToFind):
    for property in getElementStyle(element).split(";"):
        if propertyToFind + ":" in property:
            return property.split(":")[1].strip()
    return None
def setElementProperty(element, propertyToSet, value):
    for property in getElementStyle(element).split(";"):
        if propertyToSet + ":" in property:
            setElementStyle(element, getElementStyle(element).replace(property, propertyToSet + ":" + value))
            return
    setElementStyle(element, propertyToSet + ":" + value + ";" + getElementStyle(element))