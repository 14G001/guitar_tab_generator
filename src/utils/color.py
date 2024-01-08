def strColorToRGB(strColor):
    rgbColor = []
    for color in strColor.replace("(", "").replace(")", "").split(","):
        rgbColor.append(int(color))
    return tuple(rgbColor)