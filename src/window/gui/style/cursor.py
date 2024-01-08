from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt


CURSOR_POINTER = 0


def setCursor(element, cursorType):
    cursor = None
    if cursorType == CURSOR_POINTER: cursor = Qt.PointingHandCursor
    element.setCursor(QCursor(cursor))
