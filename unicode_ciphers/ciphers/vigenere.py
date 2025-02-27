import string as s
from unidecode import unidecode
from .base import Cipher, CipherArgError
from .registry import registry

class VigenereArgError(CipherArgError):
    def __init__(self, message=None, code=None):
        self.message = message
        self.exceptions_code = {
            1: "No argument 'string' provided",
        }
        if code:
            self.message = self.exceptions_code.get(code)

        super().__init__(self.message)

    def __str__(self):
        return f"VigenereArgError: {self.message}"


@registry.register(
    name="vigenere",
    description="The Vigenère cipher is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher",
    fullname="Vigenere Cipher"
)
class Vigenere(Cipher):
    def __init__(self, string: str = '', password: str = ''):
        """
        The Vigenère cipher is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher
        :param password: password to apply dynamic offset
        :param string: string to encipher
        """
        super().__init__(string, password=password)
        self.upper = s.ascii_uppercase
        self.lower = s.ascii_lowercase
        self.description = "Rotation with Password"
        self.password = password

    def password_offset(self, password_index: int):
        password_char = unidecode(self.password[password_index % len(self.password)])
        if password_char in self.upper:
            return self.upper.index(password_char)
        elif password_char in self.lower:
            return self.lower.index(password_char)
        else:
            return 0

    def check_input(self, string: str = '', password: str = ''):
        if string:
            self.string = string
        if not self.string:
            raise VigenereArgError(code=1)
        if password:
            self.password = password
        self.password = unidecode(self.password)
        self.string = unidecode(self.string)

    def encipher(self, string: str = '', password: str = ''):
        self.result = ''
        self.check_input(string=string, password=password)

        for i_char in range(len(self.string)):
            char = self.string[i_char]
            if char.lower() not in self.lower:
                self.result += char
            else:
                i_password = self.password_offset(i_char)
                if char in self.lower:
                    self.result += self.lower[
                    (self.lower.index(char) + i_password) % len(self.lower)]
                elif char in self.upper:
                    self.result += self.upper[
                    (self.upper.index(char) + i_password) % len(self.upper)]

        return self.return_result()

    def decipher(self, string: str = '', password: str = ''):
        self.result = ''
        self.check_input(string=string, password=password)

        for i_char in range(len(self.string)):
            char = self.string[i_char]
            if char.lower() not in self.lower:
                self.result += char
            else:
                i_password = self.password_offset(i_char)
                if char in self.lower:
                    self.result += self.lower[
                    (self.lower.index(char) - i_password) % len(self.lower)]
                elif char in self.upper:
                    self.result += self.upper[
                    (self.upper.index(char) - i_password) % len(self.upper)]

        return self.return_result()
