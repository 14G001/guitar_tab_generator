from window.gui.element.toolTip import setElementToolTip
from utils.colors import MEDIUM_GREY, WHITE


STYLE = """
padding: 0 25px 0 0;
margin: 0 25px 0 0;
text-align: center;
background-color: rgb""" + str(MEDIUM_GREY) + """;
color: rgb""" + str(WHITE) + """;
"""


def setWarningToolTip(element, message):
    setElementToolTip(element, "<div style='" + STYLE + "'>" + message + "</div>")