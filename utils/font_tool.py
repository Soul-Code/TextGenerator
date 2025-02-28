from fontTools.fontBuilder import TTFont

fonts = {}
cmaps = {}


def check(char, font_path):
    if font_path in cmaps:
        cmap = cmaps[font_path]
    else:
        font = TTFont(font_path)
        cmap = font.getBestCmap()
        cmaps[font_path] = cmap
        # fonts[font_path] = font
    if ord(char) in cmap:
        return True
    return False
    # utf8_char = char.encode("unicode_escape").decode('utf-8')
    # if utf8_char.startswith('\\u'):
    #     uc = "uni" + utf8_char[2:].upper()
    #     f = font.getGlyphSet().get(uc)
    #     if f and f.numberOfContours:
    #         return True
    #     else:
    #         return False
    # return True
