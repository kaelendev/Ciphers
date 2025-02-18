def to_hexa(string: str, separator=None):
    string = str(string)
    result = ''
    for i in string:
        result+=hex(ord(i))
    if separator:
        result = result.replace("0x", separator)
    return result

def from_hexa(string: str, separator=None):
    result = ''
    for i in string.split(separator or "0x"):
        if i:
            result += chr(int(i, 16))
    return result