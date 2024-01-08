from window.gui.event.dragAndDrop import getEventURLs

def enteredFileMeetRequirements(event):
    numberOfURLs = len(getEventURLs(event))
    if numberOfURLs < 1 or numberOfURLs > 1:
        return False
    return True