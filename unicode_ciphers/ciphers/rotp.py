import string as s
from unidecode import unidecode
from .base import Cipher, CipherArgError


class ROTPArgError(CipherArgError):
    def __init__(self, message=None, code=None):
        self.message = message
        self.exceptions_code = {
            1: "No argument 'string' provided",
        }
        if code:
            self.message = self.exceptions_code.get(code)

        super().__init__(self.message)

    def __str__(self):
        return f"ROTPArgError: {self.message}"

class ROTP(Cipher):
    def __init__(self, string: str = '', password: str = ''):
        """
        ROTP (Rotation with Password) is an encryption algorithm (custom cipher) that uses a password to apply a dynamic shift to each character in the input string.
        :param password: password to apply dynamic offset
        :param string: string to encipher
        """
        super().__init__(string, password=password)
        self.description = "Rotation with Password"
        self.password = password

    def check_input(self, string: str = '', password: str = ''):
        if string:
            self.string = string
        if not self.string:
            raise ROTPArgError(code=1)
        if password:
            self.password = password
        self.password = unidecode(self.password)

    def encipher(self, string: str = '', password: str = ''):
        self.result = ''
        self.check_input(string=string, password=password)

        for char in unidecode(self.string):
            if char not in s.printable:
                self.result += char
            else:
                password_char = unidecode(self.password[unidecode(self.string).index(char) % len(self.password)])
                self.result += s.printable[
                    (s.printable.index(char) + s.printable.index(password_char)) % len(s.printable)]
        return self.return_result()

    def decipher(self, string: str = '', password: str = ''):
        self.result = ''
        self.check_input(string=string, password=password)

        for char in unidecode(self.string):
            if char not in s.printable:
                self.result += char
            else:
                password_char = unidecode(self.password[unidecode(self.string).index(char) % len(self.password)])
                self.result += s.printable[
                    (s.printable.index(char) - s.printable.index(password_char)) % len(s.printable)]
        return self.return_result()