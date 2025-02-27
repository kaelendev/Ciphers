import string as s
from unidecode import unidecode
from .base import Cipher, CipherArgError
from .registry import registry

class CaesarArgError(CipherArgError):
    def __init__(self, message=None, code=None):
        self.message = message
        self.exceptions_code = {
            1: "",
            2: "The shift must not exceed 26"
        }
        if code:
            self.message = self.exceptions_code.get(code)

        super().__init__(self.message)

    def __str__(self):
        return f"CesarArgError: {self.message}"

@registry.register(
    name="caesar",
    description="Rotating the 26 letters of the alphabet with a shift",
    fullname="Caesar Cipher"
)
class Caesar(Cipher):
    def __init__(self, string: str = '', shift: int = 13, options: [str]=None):
        """
        Caesar Code: Rotating the 26 letters of the alphabet with a shift
        :param string: string to encipher
        :param shift: shift must be between **0** and **26**
        :param options: *["digits"]* to rotate digits
                        *["specials"]* to rotate classic special chars
        """
        super().__init__(string, shift=shift)
        if options is None:
            options = []
        self.lower = s.ascii_lowercase
        self.upper = s.ascii_uppercase
        self.digits = s.digits
        self.specials = s.punctuation
        self.options = options
        self.shift = shift

    def check_input(self, string: str = '', shift: int = 0, options: [str] = None):
        if string:
            self.string = string
        if not self.string:
            raise CaesarArgError(code=1)
        if options:
            self.options = options
        if shift:
            self.shift = shift
        if self.shift > 26:
            return CaesarArgError(code=2)

    def encipher(self, string: str = '', shift: int = 0, options: [str] = None):
        self.result = ''
        self.check_input(shift=shift, string=string, options=options)

        for char in unidecode(self.string):
            if char in self.lower:
                self.result += self.lower[(self.lower.index(char) + self.shift) % 26]
            elif char in self.upper:
                self.result += self.upper[(self.upper.index(char) + self.shift) % 26]
            elif "digits" in self.options and char in self.digits:
                self.result += self.digits[(self.digits.index(char) + self.shift) % 10]
            elif "specials" in self.options and char in self.specials:
                self.result += self.specials[(self.specials.index(char) + self.shift) % len(self.specials)]
            else:
                self.result += char

        return self.return_result()

    def decipher(self, string: str='', shift: int=0):
        self.result = ''
        self.check_input(shift=shift, string=string)

        for char in unidecode(self.string):
            if char in self.lower:
                self.result += self.lower[(self.lower.index(char) - self.shift) % 26]
            elif char in self.upper:
                self.result += self.upper[(self.upper.index(char) - self.shift) % 26]
            elif "digits" in self.options and char in self.digits:
                self.result += self.digits[(self.digits.index(char) - self.shift) % 10]
            elif "specials" in self.options and char in self.specials:
                self.result += self.specials[(self.specials.index(char) - self.shift) % len(self.specials)]
            else:
                self.result += char


        return self.return_result()