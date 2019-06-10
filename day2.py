def flipAndInvertImage(img):
    for raw in img:
        raw.reverse()
        for n, i in enumerate(raw):
            if i  == 1:
                raw[n] = 0
            if i == 0:
                raw[n] = 1
    return img
