import warnings

class CipherArgError(Exception):
    def __init__(self, message=None, code=None):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"CipherArgError: {self.message}"


class Cipher:
    def __init__(self, string: str = '', **kwargs):
        self.description = "Base Cipher"
        self.string = str(string)
        self.result = ''
        self.kwargs = kwargs
        self._error = CipherArgError

    def __str__(self):
        return self.string

    def __repr__(self):
        return repr(self.__str__())

    def return_class(self):
        return self.__class__(self.string, **self.kwargs)

    def return_result(self):
        return self.__class__(self.result, **self.kwargs)

    def process_input(self, string: str = '', **kwargs):
        if string:
            self.string = str(string)
        if not self.string:
            raise self._error("Input string is required.")
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)

    def encipher(self, string: str = '', **kwargs):
        self.result = ''
        self.process_input(string=string, **kwargs)
        raise NotImplementedError("Encipher method must be implemented in child classes.")

    def decipher(self, string: str = '', **kwargs):
        self.result = ''
        self.process_input(string=string, **kwargs)
        raise NotImplementedError("Decipher method must be implemented in child classes.")

    def encrypt(self, *args, **kwargs):
        """
        Here we are encrypting
        """
        return self.encipher(*args, **kwargs)

    def decrypt(self, *args, **kwargs):
        """
        Here we are decrypting
        """
        return self.decipher(*args, **kwargs)

    def encode(self, *args, **kwargs):
        """
        Here we are encrypting, **not encoding** !!
        So change this function call please
        """
        warnings.warn("Vocabulary Warning ! Change this function call please (replace it with '.encrypt()' or '.encipher()')", UserWarning)
        return self.encipher(*args, **kwargs)

    def decode(self, *args, **kwargs):
        """
        Here we are decrypting, **not decoding** !!
        So change this function call please
        """
        warnings.warn("Vocabulary Warning ! Change this function call please (replace it with '.decrypt()' or '.decipher()')", UserWarning)

        return self.decipher(*args, **kwargs)
