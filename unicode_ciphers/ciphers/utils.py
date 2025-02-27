from .registry import registry

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

class CipherClassNameError(Exception):
    def __init__(self):
        self.message = "Bad cipher class name."
        super().__init__(self.message)


def to_encipher(cipher_name: str, *args, **kwargs):
    cls = None

    for cipher in registry.ciphers:
        if cipher_name.lower() in [cipher['name'].lower(), cipher['fullname'].lower()]:
            cls = cipher['class']

    if cls is None:
        raise CipherClassNameError()

    return cls(*args, **kwargs).encipher()


def to_decipher(cipher_name: str, *args, **kwargs):
    cls = None

    for cipher in registry.ciphers:
        if cipher_name.lower() in [cipher['name'].lower(), cipher['fullname'].lower()]:
            cls = cipher['class']

    if cls is None:
        raise CipherClassNameError()

    return cls(*args, **kwargs).decipher()