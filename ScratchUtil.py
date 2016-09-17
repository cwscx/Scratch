import ImageUtil


def simpleImplementation(imgPath, threshold, saveFileName):
    img = ImageUtil.read_image(imgPath)

    width = len(img)
    length = len(img[0])

    for w in xrange(width):
        for l in xrange(length):
            if w == width - 1 or l == length - 1:
                continue

            diff = abs(int(img[w][l]) - int(img[w + 1][l + 1]))
            if diff >= threshold:
                img[w][l] = 0
            else:
                img[w][l] = 255

    if saveFileName == "" or saveFileName is None:
        ImageUtil.display_image(img)
    else:
        ImageUtil.save_image(img, saveFileName)
