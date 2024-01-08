def getElementSize(element):
    size = element.size()
    return (size.width(), size.height())
def setElementSize(element, value):
    element.resize(value[0], value[1])
def getElementMinimumSize(element):
    size = element.minimumSize()
    return (size.width(), size.height())
def setElementMinimumSize(element, value):
    element.setMinimumSize(value[0], value[1])
def getElementMaximumSize(element):
    size = element.maximumSize()
    return (size.width(), size.height())
def setElementMaximumSize(element, value):
    element.setMaximumSize(value[0], value[1])
def copyElementSize(element, elementToGetSize):
    setElementMinimumSize(element, getElementMinimumSize(elementToGetSize))
    setElementMaximumSize(element, getElementMaximumSize(elementToGetSize))
    setElementSize(element, getElementSize(elementToGetSize))