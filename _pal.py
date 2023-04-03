def _pal(inword):
    word = str(inword)
    if word[:] == word[::-1]:
        return "true"
    else:
        return "false"

print(_pal(""))