def changeElementsClass(elements, classConstructor):
    lst = []
    for element in elements:
        lst.append(classConstructor(element))
    return lst