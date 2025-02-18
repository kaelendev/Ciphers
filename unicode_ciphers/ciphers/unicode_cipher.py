import string as s
from unidecode import unidecode
from .base import Cipher, CipherArgError
from .utils import to_hexa


class UnicodeCipherArgError(CipherArgError):
    def __init__(self, message=None, code=None):
        self.message = message
        self.exceptions_code = {
            1: "No argument 'string' provided",
            2: "Argument 'shift' must not exceed 1114111",
        }
        if code:
            self.message = self.exceptions_code.get(code)

        super().__init__(self.message)

    def __str__(self):
        return f"UnicodeCipherArgError: {self.message}"

class UnicodeCipher(Cipher):
    def __init__(self, string: str = '', password: str = '', shift: int = 0):
        super().__init__(string, password=password, shift=shift)
        self.int_result = ''
        self.password_len = len(password)
        self.password = password
        self.shift = shift

        if shift > 1114111:
            raise UnicodeCipherArgError(code=2)

    def __hex__(self):
        return to_hexa(self.result)

    def check_input(self, string: str = '', shift: int = 0, password: str = ''):
        if string:
            self.string = string
        if shift:
            self.shift = shift
        if shift > 1114111:
            raise UnicodeCipherArgError(code=2)
        if password:
            self.password = password
        if not self.string:
            raise UnicodeCipherArgError(code=1)

    def encipher(self, string: str = '', password: str = '', shift: int = 0):
        self.result = ''
        self.check_input(password=password, string=string, shift=shift)

        for char in self.string:
            self.result += chr((ord(char) + ord(self.password[self.string.index(char) % self.password_len])) + self.shift % 1114111)

        return self.return_result()


    def decipher(self, string: str = '', password: str = '', shift: int = 0):
        self.result = ''
        self.check_input(password=password, string=string, shift=shift)

        for char in self.string:
            self.result += chr((ord(char) - ord(self.password[self.string.index(char) % self.password_len])) - self.shift % 1114111)


        return self.return_result()