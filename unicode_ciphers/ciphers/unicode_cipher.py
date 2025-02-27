import string as s
from unidecode import unidecode
from .base import Cipher, CipherArgError
from .utils import to_hexa
from .registry import registry

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

@registry.register(
    name="unicode_cipher",
    description="Rotating the 26 letters of the alphabet with a shift",
    fullname="Caesar Code"
)
class UnicodeCipher(Cipher):
    """
    Unicode Cipher: Rotating all the Unicode characters using a password and an additional shift
    :param string: string to encipher
    :param password: password to apply dynamic offset
    :param shift: shift must be between **-1114111** and **1114111**
    """
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

        for i_char in range(len(self.string)):
            char = self.string[i_char]
            self.result += chr((ord(char) + ord(self.password[i_char % self.password_len]) + self.shift % 1114111) % 1114111)

        return self.return_result()


    def decipher(self, string: str = '', password: str = '', shift: int = 0):
        self.result = ''
        self.check_input(password=password, string=string, shift=shift)

        for i_char in range(len(self.string)):
            char = self.string[i_char]
            self.result += chr((ord(char) - ord(self.password[i_char % self.password_len]) - self.shift % 1114111) % 1114111)

        return self.return_result()