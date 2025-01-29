def delete_dubles(text):
    if not text:
        return text
    symb = [text[0]]
    for i in range(1, len(text)):
        if text[i] != symb[-1]:
            symb.append(text[i])
    return ''.join(symb)
