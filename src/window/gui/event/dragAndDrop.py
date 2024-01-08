def setAcceptDrops(element, value):
    element.setAcceptDrops(value)

def getEventURLs(event):
    urls = []
    if not event.mimeData().hasUrls() or len(event.mimeData().urls()) < 1:
        return urls
    for url in event.mimeData().urls():
        urls.append(url.toLocalFile())
    return urls
