win = None


def setWindow(window):
    global win
    win = window
def getWindow():
    return win
def getWindowInputs():
    return win.inputElements