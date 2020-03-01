def mirror(text):
    r=reverse(text)
    mirrored=text+r
    return mirrored


def reverse(text):
    rever=""
    for char in (text):
        rever=char+rever
    return rever
      