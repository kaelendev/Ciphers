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
        self.description = "Vigenere Cipher"
        self.password = password

    def password_offset(self, password_index: int):
        password_char = unidecode(self.password[password_index % len(self.password)])
        if password_char in self.upper:
            return self.upper.index(password_char)
        elif password_char in self.lower:
            return self.lower.index(password_char)
        else:
            return 0

    def process_input(self, string: str = None, password: str = None):
        super().process_input(string, password=password)
        if not self.string:
            raise VigenereArgError(code=1)
        self.password = unidecode(self.password)
        self.string = unidecode(self.string)

    def encipher(self, string: str = None, password: str = None):
        self.result = ''
        self.process_input(string=string, password=password)
        password_index = 0

        for char in self.string:
            if not char.isalpha():
                self.result += char
                continue

            i_password = self.password_offset(password_index)
            if char.islower():
                alphabet = self.lower
            else:
                alphabet = self.upper

            self.result += alphabet[(alphabet.index(char) + i_password) % 26]
            password_index += 1
        return self.return_result()

    def decipher(self, string: str = None, password: str = None):
        self.result = ''
        self.process_input(string=string, password=password)
        password_index = 0

        for char in self.string:
            if not char.isalpha():
                self.result += char
                continue

            i_password = self.password_offset(password_index)
            if char.islower():
                alphabet = self.lower
            else:
                alphabet = self.upper

            original_pos = (alphabet.index(char) - i_password) % len(alphabet)
            self.result += alphabet[original_pos]
            password_index += 1

        return self.return_result()
